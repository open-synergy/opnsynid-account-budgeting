# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Account Budget Variance",
    "version": "8.0.1.0.0",
    "summary": "Adds variance amount and percent",
    "category": "Accounting",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": False,
    "application": False,
    "depends": [
        "account_budget",
    ],
    "data": [
        "views/account_budget_post_view.xml",
        "views/crossovered_budget_view.xml",
        "views/crossovered_budget_line_view.xml"
    ],
}
