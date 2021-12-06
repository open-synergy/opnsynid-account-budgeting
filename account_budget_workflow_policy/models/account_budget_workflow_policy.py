# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AccountBudgetWorkflowPolicy(models.Model):
    _name = "crossovered.budget"
    _inherit = [
        "crossovered.budget",
        "mixin.policy",
    ]

    @api.multi
    def _compute_policy(self):
        _super = super(AccountBudgetWorkflowPolicy, self)
        _super._compute_policy()

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

    # Log fields
    confirm_date = fields.Datetime(
        string="Confirm Date",
        readonly=True,
        copy=False,
    )

    confirm_user_id = fields.Many2one(
        string="Confirmed By",
        comodel_name="res.users",
        readonly=True,
        copy=False,
    )

    approval_date = fields.Datetime(
        string="Approval Date",
        readonly=True,
        copy=False,
    )

    approval_user_id = fields.Many2one(
        string="Approval By",
        comodel_name="res.users",
        readonly=True,
        copy=False,
    )

    done_date = fields.Datetime(
        string="Done Date",
        readonly=True,
        copy=False,
    )

    done_user_id = fields.Many2one(
        string="Done By",
        comodel_name="res.users",
        readonly=True,
        copy=False,
    )

    cancel_date = fields.Datetime(
        string="Cancel Date",
        readonly=True,
        copy=False,
    )

    cancel_user_id = fields.Many2one(
        string="Cancelled By",
        comodel_name="res.users",
        readonly=True,
        copy=False,
    )

    @api.multi
    def _prepare_confirm_data(self):
        self.ensure_one()
        return {
            "state": "confirm",
            "confirm_date": fields.Datetime.now(),
            "confirm_user_id": self.env.user.id,
        }

    @api.multi
    def action_budget_confirm(self):
        for document in self:
            document.write(document._prepare_confirm_data())

    @api.multi
    def _prepare_approval_data(self):
        self.ensure_one()
        return {
            "state": "validate",
            "approval_date": fields.Datetime.now(),
            "approval_user_id": self.env.user.id,
        }

    @api.multi
    def action_budget_validate(self):
        for document in self:
            document.write(document._prepare_approval_data())

    @api.multi
    def _prepare_done_data(self):
        self.ensure_one()
        return {
            "state": "done",
            "done_date": fields.Datetime.now(),
            "done_user_id": self.env.user.id,
        }

    @api.multi
    def action_budget_done(self):
        for document in self:
            document.write(document._prepare_done_data())

    @api.multi
    def _prepare_cancel_data(self):
        self.ensure_one()
        return {
            "state": "cancel",
            "cancel_date": fields.Datetime.now(),
            "cancel_user_id": self.env.user.id,
        }

    @api.multi
    def action_budget_cancel(self):
        for document in self:
            document.write(document._prepare_cancel_data())

    @api.multi
    def _prepare_restart_data(self):
        self.ensure_one()
        return {
            "state": "draft",
            "confirm_date": False,
            "confirm_user_id": False,
            "approval_date": False,
            "approval_user_id": False,
            "done_date": False,
            "done_user_id": False,
            "cancel_date": False,
            "cancel_user_id": False,
        }

    @api.multi
    def action_budget_draft(self):
        for document in self:
            document.write(document._prepare_restart_data())
