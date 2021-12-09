# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountBudgetWorkflowPolicy(models.Model):
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

    approval_ok = fields.Boolean(
        string="Can Approval",
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
