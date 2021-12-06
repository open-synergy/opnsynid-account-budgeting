# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Account Budget Workflow Policy",
    "version": "11.0.1.0.0",
    "category": "Administrator",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        "account_budget",
        "ssi_policy_mixin",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/account_budget_views.xml",
    ],
}
