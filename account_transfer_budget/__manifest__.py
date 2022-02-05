# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Account Transfer Budget",
    "version": "11.0.1.0.0",
    "category": "Administrator",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        "account_budget_multiple_approval",
        "ssi_sequence_mixin",
        "ssi_policy_mixin",
        "ssi_state_change_history_mixin",
        "ssi_status_check_mixin",
        "ssi_state_change_constrain_mixin",
    ],
    "data": [
        "views/account_budget_transfer_type_view.xml",
        "views/account_transfer_budget_view.xml",
    ],
}
