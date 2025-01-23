{
    'name': 'App One',
    'version': '17.0',
    'category': '',
    'summary': 'Internal Machinery Sales and Management',
    'description': """
                    This module provides comprehensive features for managing sales and internal machinery within an eCommerce environment.
                    It includes functionalities for tracking inventory,
                    handling sales orders, managing customer interactions,
                    and supporting eCommerce operations.""",
    'depends': ['base', 'sale', 'account', 'mail', 'contacts', 'web'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'data/sequence.xml',

        'views/base_menu.xml',
        'views/property_view.xml',
        'views/owner_view.xml',
        'views/tag_view.xml',
        'views/sale_order_view.xml',
        'views/account_move_view.xml',
        'views/res_partner_view.xml',
        'views/building_view.xml',
        'views/property_history_view.xml',

        'reports/property_report.xml',

        'wizard/change_state_wizard_view.xml',


    ],
    'assets': {
        'web.assets_backend': [
            'app_one/static/src/css/property.css'
        ]
    },
    'demo': [],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
