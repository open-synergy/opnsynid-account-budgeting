# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class CrossoveredBudget(models.Model):
    _name = "crossovered.budget"
    _inherit = [
        "crossovered.budget",
        "mixin.policy",
    ]

    # policy fields
    confirm_ok = fields.Boolean(
        string="Can Confirm",
        compute="_compute_policy",
    )
    approve_ok = fields.Boolean(
        string="Can Approval",
        compute="_compute_policy",
    )
    reject_ok = fields.Boolean(
        string="Can Rejected",
        compute="_compute_policy",
    )
    done_ok = fields.Boolean(
        string="Can Done",
        compute="_compute_policy",
    )
    cancel_ok = fields.Boolean(
        string="Can Cancel",
        compute="_compute_policy",
    )
    restart_ok = fields.Boolean(
        string="Can Restart",
        compute="_compute_policy",
    )

    @api.onchange(
        "budget_tmpl_id",
    )
    def onchange_policy_template_id(self):
        policy_template_id = self._get_template_policy()
        for document in self:
            document.policy_template_id = policy_template_id
