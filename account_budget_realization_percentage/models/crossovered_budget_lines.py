# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class CrossoveredBudgetLines(models.Model):
    _name = "crossovered.budget.lines"
    _inherit = "crossovered.budget.lines"

    @api.multi
    def _compute_realization_percentage(self):
        for record in self:
            result = 0.0
            if record.planned_amount != 0.0:
                result = (record.practical_amount / record.planned_amount) * 100.00
            record.realization_percentage = result

    realization_percentage = fields.Float(
        string="Realization Percentage",
        compute="_compute_realization_percentage",
        store=False,
    )
