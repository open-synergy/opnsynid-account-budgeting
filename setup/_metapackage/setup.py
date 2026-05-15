import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo11-addons-open-synergy-opnsynid-account-budgeting",
    description="Meta package for open-synergy-opnsynid-account-budgeting Odoo addons",
    version=version,
    install_requires=[
        'odoo11-addon-account_budget_multiple_approval',
        'odoo11-addon-account_budget_realization_percentage',
        'odoo11-addon-account_budget_workflow_policy',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 11.0',
    ]
)
