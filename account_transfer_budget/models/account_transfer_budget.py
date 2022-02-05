# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError


class AccountTransferBudget(models.Model):
    _name = "account.transfer_budget"
    _description = "Account Transfer Budget"
    _inherit = [
        "mail.thread",
        "mixin.multiple_approval",
        "mixin.sequence",
        "mixin.policy",
        "mixin.state_change_history",
        "mixin.status_check",
        "mixin.state_change_constrain",
    ]

    _approval_from_state = "draft"
    _approval_to_state = "valid"
    _approval_state = "confirm"

    name = fields.Char(
        string="# Document",
        default="/",
        required=True,
    )

    type_id = fields.Many2one(
        string="Type",
        comodel_name="account.budget_transfer_type",
        ondelete="restrict",
        required=True,
    )

    user_id = fields.Many2one(
        string="Responsible",
        comodel_name="res.users",
        ondelete="restrict",
        required=True,
    )

    origin_budget_id = fields.Many2one(
        string="# Origin Budget",
        comodel_name="crossovered.budget",
        ondelete="restrict",
        required=True,
    )

    origin_budget_line_id = fields.Many2one(
        string="Origin Budget Lines",
        comodel_name="crossovered.budget.lines",
        ondelete="restrict",
        required=True,
    )

    target_budget_id = fields.Many2one(
        string="# Target Budget",
        comodel_name="crossovered.budget",
        ondelete="restrict",
        required=True,
    )

    target_budget_line_id = fields.Many2one(
        string="Target Budget Lines",
        comodel_name="crossovered.budget.lines",
        ondelete="restrict",
        required=True,
    )

    notes = fields.Text(
        string="Notes",
    )

    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting for Approval"),
            ("valid", "Valid"),
            ("reject", "Rejected"),
            ("cancel", "Cancelled"),
        ],
        default="draft",
    )

    confirm_ok = fields.Boolean(
        string="Can Confirm",
        compute="_compute_policy",
    )

    cancel_ok = fields.Boolean(
        string="Can Cancelled",
        compute="_compute_policy",
    )

    approve_ok = fields.Boolean(
        string="Can Approved",
        compute="_compute_policy",
    )

    reject_ok = fields.Boolean(
        string="Can Rejected",
        compute="_compute_policy",
    )

    restart_ok = fields.Boolean(
        string="Can Restart",
        compute="_compute_policy",
    )

    @api.multi
    def action_confirm(self):
        for document in self:
            document.write({"state": "confirm"})
            document.action_request_approval()

    @api.multi
    def action_cancel(self):
        for document in self:
            document.write({"state": "cancel"})

    @api.multi
    def action_restart(self):
        for document in self:
            document.write({"state": "draft"})

    @api.multi
    def action_valid(self):
        for document in self:
            document.write({"state": "valid"})

    @api.multi
    def unlink(self):
        strWarning = _("You can only delete data on draft state")
        for document in self:
            if document.state != "draft":
                if not self.env.context.get("force_unlink", False):
                    raise UserError(strWarning)
        _super = super(AccountTransferBudget, self)
        _super.unlink()

    def action_approve_approval(self):
        _super = super(AccountTransferBudget, self)
        _super.action_approve_approval()
        for document in self:
            if document.approved:
                document.action_valid()

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            if record.name == "/":
                name = "*" + str(record.id)
            else:
                name = record.name
            result.append((record.id, name))
        return result

    @api.model
    def create(self, values):
        _super = super(AccountTransferBudget, self)
        result = _super.create(values)
        sequence = result._create_sequence()
        result.write(
            {
                "name": sequence,
            }
        )
        return result
