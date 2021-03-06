# -*- coding: utf-8 -*-
{
    'name': "Bean Bakery Modules",

    'summary': """
        This is the custom module for Bean Bakery biz.
        """,

    'description': """
        This is the custom module for Bean Bakery biz, including:
            - VN address pre-defined (csv file)
            - Show customer phone and delivery address on sale order
            - 
        
        The master data (.csv file) note:
            - for the 'id' column always use alias ID, the system will automatically assign the real ID.
            - For the relation field, always use the alias ID
    """,

    'author': "Bean Bakery",
    'license':"LGPL-3",
    'website': "http://www.beanbakery.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Appication',
    'version': '0.1',
    "application": True,
    "installable": True,

    # any module necessary for this one to work correctly
    'depends': ['base','website','mail','sale','web_responsive','beanbakery_address','l10n_vn'],

    "images": ["static/description/icon.png"],

    # always loaded
    'data': [
        # 'views/demo_library/templates.xml',
        'views/widgets/backend/qr_widget/template.xml',
        'views/product/product.xml',
        'templates/pwa_manifest_assets.xml',
        'views/pwa/res_pwa_configs.xml',
        'views/sale_order/sale_order.xml',
        'views/vn_address/res_company_info.xml',
        'views/invoiceQR/invoice_template.xml',
        'security/groups.xml',
        'security/ir.model.access.csv',
       
        
    ],
    'assets': {
        'web.assets_backend': [
            "/bean_bakery_module/static/src/pwa/webclient.js",
        ],
    },
    # only loaded in demonstration mode
    'demo': [
         #'data/master_data.xml'
    ],
    
}
