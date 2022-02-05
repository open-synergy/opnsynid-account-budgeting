# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AccountBudgetTransferType(models.Model):
    _name = "account.budget_transfer_type"
    _description = "Account Budget Transfer Type"
    _order = "id"

    name = fields.Char(
        string="# Document",
        required=True,
    )
    code = fields.Char(
        string="Code",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
        required=True,
    )
    description = fields.Text(
        string="Description",
    )

    allow_transfer_accross_budget = fields.Boolean(
        string="Allow Transfer Accross Budget"
    )

    @api.model
    def name_search(self, name="", args=None, operator="ilike", limit=100):
        res = super(AccountBudgetTransferType, self).name_search(
            name=name, args=args, operator=operator, limit=limit
        )
        args = list(args or [])
        if name:
            criteria = ["|", ("code", operator, name), ("name", operator, name)]
            criteria = criteria + args
            project_ids = self.search(criteria, limit=limit)
            if project_ids:
                return project_ids.name_get()
        return res
