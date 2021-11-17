# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


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

    state = fields.Selection(selection_add=[("reject", "Rejected")])

    @api.multi
    def action_budget_confirm(self):
        for document in self:
            document.write({"state": "confirm"})
            document.action_request_approval()

    def action_approve_approval(self):
        _super = super(AccountBudgetMultipelApproval, self)
        _super.action_approve_approval()
        for document in self:
            if document.approved:
                document.action_budget_validate()
