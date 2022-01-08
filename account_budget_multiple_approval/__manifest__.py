# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Account Budget Multiple Approval",
    "version": "11.0.1.1.0",
    "category": "Accounting",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "account_budget",
        "ssi_multiple_approval_mixin",
    ],
    "data": [
        "data/approval_template_data.xml",
        "views/account_budget_views.xml",
    ],
}
