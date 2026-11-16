{
    'name': 'POS Access Rights Employee',
    'version': '20.0.2.0.0',
    'category': 'Sales/Point of Sale',
    'summary': 'Granular Point of Sale permissions, numpad restrictions, and role presets per employee',
    'description': """
POS Access Rights Employee (Odoo 20)
====================================
Enhances control over the Point of Sale interface by allowing administrators
to enable or disable key functionalities for each cashier/employee:
- Order Management: Hide New Order, Delete Order, Customer Selection, Actions, Payment, Note, Transfer.
- Numpad & Pricing: Hide Numpad, Disable +/-, Qty, Price Change, Discount, Backspace/Line Delete, and Max Discount %.
- Navbar & Dropdown Menu: Hide Search, Barcode, Customer Display, Product Info, Cash In/Out, Close Register, Backend, Total Session, etc.
- Role Presets: One-click Full Access, Standard Cashier, and Order Taker presets.
    """,
    'author': 'Sensible Consulting Services',
    'website': 'https://sensiblecs.com',
    'license': 'LGPL-3',
    'depends': ['pos_hr'],
    'data': [
        'security/ir.access.csv',
        'views/hr_employee_view.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_access_rights_employee/static/src/**/*',
        ],
    },
    'images': ['static/description/banner.png'],
    'application': True,
    'installable': True,
}