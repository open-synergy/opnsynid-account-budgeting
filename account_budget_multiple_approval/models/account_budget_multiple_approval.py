# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models

# from odoo.exceptions import UserError, ValidationError
# from odoo.tools.safe_eval import safe_eval


class AccountBudgetMultipelApproval(models.Model):
    _name = "crossovered.budget"
    _inherit = [
        "crossovered.budget",
        "mixin.multiple_approval",
    ]

    _approval_state_field = "state"
    _approval_from_state = "draft"
    _approval_to_state = "validate"
    _approval_cancel_state = "cancel"
    _approval_reject_state = "reject"
    _approval_state = "confirm"

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("cancel", "Cancelled"),
            ("confirm", "Waiting for Approval"),
            ("validate", "Validated"),
            ("done", "Done"),
            ("reject", "Rejected"),
        ],
        "Status",
        default="draft",
        index=True,
        required=True,
        readonly=True,
        copy=False,
        track_visibility="always",
    )

    @api.multi
    def action_budget_confirm(self):
        for rec in self:
            # rec.action_budget_confirm()
            rec.write({"state": "confirm"})
            rec.action_request_approval()

    def action_open(self):
        for document in self:
            document.write({"state": "validate"})

    def action_approve_approval(self):
        _super = super(AccountBudgetMultipelApproval, self)
        _super.action_approve_approval()
        for document in self:
            if document.approved:
                document.action_open()

    @api.multi
    def action_reject_approval(self):
        for rec in self:
            rec._action_validate("rejected")
            rec.write({"state": "draft"})

    @api.multi
    def _action_validate(self, state):
        self.ensure_one()
        approval_ids = self.active_approval_ids
        user_approves = approval_ids.filtered(
            lambda r: self.env.user.id in r.approver_user_ids.ids
        )
        if user_approves:
            user_approves.write(
                {
                    "status": state,
                    "date": fields.Datetime.now(),
                    "user_id": self.env.user.id,
                }
            )
            if state == "approved":
                self.set_active(self.next_approval_ids)
            elif state == "rejected":
                self.write({"state": "reject"})

    @api.multi
    def action_request_approval(self):
        obj_approval_template = self.env["approval.template"]
        approver_ids = False
        for rec in self:
            if getattr(rec, self._approval_state_field) == self._approval_from_state:
                if rec.approval_template_id:
                    if self._evaluate_approval(rec.approval_template_id):
                        rec.write({"approval_template_id": rec.approval_template_id.id})
                    else:
                        rec.write({"approval_template_id": False})
                if not rec.approval_template_id:
                    criteria_definition = [
                        ("model", "=", self._name),
                    ]
                    template_ids = obj_approval_template.search(
                        criteria_definition,
                        order="sequence desc",
                    )
                    if template_ids:
                        for template in template_ids:
                            if self._evaluate_approval(template):
                                rec.write({"approval_template_id": template.id})
                                break
                approver_ids = rec.create_approver()
                rec.set_active(approver_ids)
        return approver_ids
