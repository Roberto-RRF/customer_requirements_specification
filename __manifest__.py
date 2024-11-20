{
    'name': 'Customer Requirements',
    'version': '1.0',
    'author':'ANFEPI: Roberto Requejo Jimenez',
    'depends': ['contacts', 'sale', 'stock', 'mrp'],
    'description': """
    """,
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'reports/specification_report.xml',
        'views/customer_requirements_menu.xml',
        'views/customer_requirements_category_view.xml',
        'views/customer_requirements_view.xml',
        'views/res_partner_view.xml',
        'views/sale_order_view.xml',
        'views/mrp_production_view.xml',
        'views/stock_picking_view.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'auto_install': False,
    "license": "AGPL-3",
}