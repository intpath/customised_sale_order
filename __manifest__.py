# -*- coding: utf-8 -*-
{
    # Application Information
    'name': 'Customised Sale Report',
    'category': 'Accounting/Reports',
    'version': '13.0.1.0.0',

    # Author Information
    'author': 'Er. Vaidehi Vasani',

    # Dependencies
    'depends': ['sale'],

    # Views
    'data': [
        'views/view_sale_order.xml',
        'report/customised_sale_report.xml'
    ],

    # Technical
    'installable': True,
    'application': False,
    'auto_install': False,
}
