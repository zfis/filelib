# -*- coding: utf-8 -*-
{
    'name': "e2yun_customer_payment_extend",

    'summary': """
        """,

    'description': """
        宏华crm客户付款功能增强
    """,

    'author': "Li Haonan",
    'website': "www.e2yun.cn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'account',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account', 'e2yun_customer_extends'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/bank_info.xml',
        'views/customer_refund.xml',
        'views/button_to_payment.xml',
    ],
}