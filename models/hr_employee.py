from odoo import api, models, fields

POS_ACCESS_FIELDS = [
    'sbl_hide_pos_new_order_button',
    'sbl_hide_pos_delete_order_button',
    'sbl_hide_pos_customer_selection_button',
    'sbl_hide_pos_actions_button',
    'sbl_hide_pos_numpad',
    'sbl_disable_pos_numpad_plus_minus',
    'sbl_disable_pos_qty',
    'sbl_disable_pos_discount_button',
    'sbl_hide_pos_payment',
    'sbl_disable_pos_change_price',
    'sbl_hide_pos_note_button',
    'sbl_hide_pos_transfer_order_button',
    'sbl_hide_pos_barcode_button',
    'sbl_hide_pos_search_input',
    'sbl_hide_pos_customer_display',
    'sbl_hide_pos_product_info',
    'sbl_hide_pos_dropdown_navbar',
    'sbl_hide_pos_dropdown_install_app',
    'sbl_hide_pos_dropdown_cash_inout',
    'sbl_hide_pos_dropdown_reload_data',
    'sbl_hide_pos_dropdown_create_product',
    'sbl_hide_pos_dropdown_barcode_scanner',
    'sbl_hide_pos_dropdown_print_report',
    'sbl_hide_pos_dropdown_backend',
    'sbl_hide_pos_dropdown_close_register',
    'sbl_hide_pos_dropdown_total_session',
    'sbl_disable_pos_line_delete',
    'sbl_pos_own_orders_only',
    'sbl_pos_max_discount_pct',
]


class ResUsers(models.Model):
    _inherit = 'res.users'

    sbl_hide_pos_new_order_button = fields.Boolean(related='employee_id.sbl_hide_pos_new_order_button', readonly=False)
    sbl_hide_pos_delete_order_button = fields.Boolean(related='employee_id.sbl_hide_pos_delete_order_button', readonly=False)
    sbl_hide_pos_customer_selection_button = fields.Boolean(related='employee_id.sbl_hide_pos_customer_selection_button', readonly=False)
    sbl_hide_pos_actions_button = fields.Boolean(related='employee_id.sbl_hide_pos_actions_button', readonly=False)
    sbl_hide_pos_numpad = fields.Boolean(related='employee_id.sbl_hide_pos_numpad', readonly=False)
    sbl_disable_pos_numpad_plus_minus = fields.Boolean(related='employee_id.sbl_disable_pos_numpad_plus_minus', readonly=False)
    sbl_disable_pos_qty = fields.Boolean(related='employee_id.sbl_disable_pos_qty', readonly=False)
    sbl_disable_pos_discount_button = fields.Boolean(related='employee_id.sbl_disable_pos_discount_button', readonly=False)
    sbl_hide_pos_payment = fields.Boolean(related='employee_id.sbl_hide_pos_payment', readonly=False)
    sbl_disable_pos_change_price = fields.Boolean(related='employee_id.sbl_disable_pos_change_price', readonly=False)
    sbl_hide_pos_note_button = fields.Boolean(related='employee_id.sbl_hide_pos_note_button', readonly=False)
    sbl_hide_pos_transfer_order_button = fields.Boolean(related='employee_id.sbl_hide_pos_transfer_order_button', readonly=False)
    sbl_hide_pos_barcode_button = fields.Boolean(related='employee_id.sbl_hide_pos_barcode_button', readonly=False)
    sbl_hide_pos_search_input = fields.Boolean(related='employee_id.sbl_hide_pos_search_input', readonly=False)
    sbl_hide_pos_customer_display = fields.Boolean(related='employee_id.sbl_hide_pos_customer_display', readonly=False)
    sbl_hide_pos_product_info = fields.Boolean(related='employee_id.sbl_hide_pos_product_info', readonly=False)
    sbl_hide_pos_dropdown_navbar = fields.Boolean(related='employee_id.sbl_hide_pos_dropdown_navbar', readonly=False)
    sbl_hide_pos_dropdown_install_app = fields.Boolean(related='employee_id.sbl_hide_pos_dropdown_install_app', readonly=False)
    sbl_hide_pos_dropdown_cash_inout = fields.Boolean(related='employee_id.sbl_hide_pos_dropdown_cash_inout', readonly=False)
    sbl_hide_pos_dropdown_reload_data = fields.Boolean(related='employee_id.sbl_hide_pos_dropdown_reload_data', readonly=False)
    sbl_hide_pos_dropdown_create_product = fields.Boolean(related='employee_id.sbl_hide_pos_dropdown_create_product', readonly=False)
    sbl_hide_pos_dropdown_barcode_scanner = fields.Boolean(related='employee_id.sbl_hide_pos_dropdown_barcode_scanner', readonly=False)
    sbl_hide_pos_dropdown_print_report = fields.Boolean(related='employee_id.sbl_hide_pos_dropdown_print_report', readonly=False)
    sbl_hide_pos_dropdown_backend = fields.Boolean(related='employee_id.sbl_hide_pos_dropdown_backend', readonly=False)
    sbl_hide_pos_dropdown_close_register = fields.Boolean(related='employee_id.sbl_hide_pos_dropdown_close_register', readonly=False)
    sbl_hide_pos_dropdown_total_session = fields.Boolean(related='employee_id.sbl_hide_pos_dropdown_total_session', readonly=False)
    sbl_disable_pos_line_delete = fields.Boolean(related='employee_id.sbl_disable_pos_line_delete', readonly=False)
    sbl_pos_own_orders_only = fields.Boolean(related='employee_id.sbl_pos_own_orders_only', readonly=False)
    sbl_pos_max_discount_pct = fields.Float(related='employee_id.sbl_pos_max_discount_pct', readonly=False)

    @api.model
    def _load_pos_data_fields(self, config):
        res = super()._load_pos_data_fields(config)
        return list(set(res + POS_ACCESS_FIELDS))


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    sbl_hide_pos_new_order_button = fields.Boolean(string='Hide POS Orders Button', default=False)
    sbl_hide_pos_delete_order_button = fields.Boolean(string='Hide POS Delete Order Button', default=False)
    sbl_hide_pos_customer_selection_button = fields.Boolean(string='Hide POS Customer Selection Button', default=False)
    sbl_hide_pos_actions_button = fields.Boolean(string='Hide POS Actions Button', default=False)
    sbl_hide_pos_numpad = fields.Boolean(string='Hide POS Numpad', default=False)
    sbl_disable_pos_numpad_plus_minus = fields.Boolean(string='Disable POS Numpad Plus-Minus Buttons', default=False)
    sbl_disable_pos_qty = fields.Boolean(string='Disable POS Quantity (QTY) Button', default=False)
    sbl_disable_pos_discount_button = fields.Boolean(string='Disable POS Discount Button', default=False)
    sbl_hide_pos_payment = fields.Boolean(string='Hide POS Payment', default=False)
    sbl_disable_pos_change_price = fields.Boolean(string='Disable POS Change Price', default=False)
    sbl_hide_pos_note_button = fields.Boolean(string='Hide POS Note Button', default=False)
    sbl_hide_pos_transfer_order_button = fields.Boolean(string='Hide POS Transfer Order Button', default=False)
    sbl_hide_pos_barcode_button = fields.Boolean(string='Hide POS Barcode Button', default=False)
    sbl_hide_pos_search_input = fields.Boolean(string='Hide POS Search Input', default=False)
    sbl_hide_pos_customer_display = fields.Boolean(string='Hide POS Customer Display', default=False)
    sbl_hide_pos_product_info = fields.Boolean(string='Hide POS Product Info Popup', default=False)
    sbl_hide_pos_dropdown_navbar = fields.Boolean(string='Hide POS Dropdown Navbar', default=False)
    sbl_hide_pos_dropdown_install_app = fields.Boolean(string='Hide Install App', default=False)
    sbl_hide_pos_dropdown_cash_inout = fields.Boolean(string='Hide Cash In/Out', default=False)
    sbl_hide_pos_dropdown_reload_data = fields.Boolean(string='Hide Reload Data', default=False)
    sbl_hide_pos_dropdown_create_product = fields.Boolean(string='Hide Create Product', default=False)
    sbl_hide_pos_dropdown_barcode_scanner = fields.Boolean(string='Hide Barcode Scanner', default=False)
    sbl_hide_pos_dropdown_print_report = fields.Boolean(string='Hide Print Report', default=False)
    sbl_hide_pos_dropdown_backend = fields.Boolean(string='Hide Backend', default=False)
    sbl_hide_pos_dropdown_close_register = fields.Boolean(string='Hide Close Register', default=False)
    sbl_hide_pos_dropdown_total_session = fields.Boolean(string='Hide Total Session (Register)', default=False)

    # New in Odoo 20 v2.0
    sbl_disable_pos_line_delete = fields.Boolean(
        string='Disable Orderline Backspace / Delete',
        help='If checked, the employee cannot delete order lines or reduce their quantity to 0 via Backspace.',
        default=False,
    )
    sbl_pos_own_orders_only = fields.Boolean(
        string='Show Only Own Orders in Ticket Screen',
        help='If checked, the employee will only see orders assigned to them on the Ticket Screen.',
        default=False,
    )
    sbl_pos_max_discount_pct = fields.Float(
        string='Max Allowed Discount (%)',
        help='Set to 0 for no limit (if Discount button is enabled), or specify a maximum discount percentage (e.g. 10.0).',
        default=0.0,
    )

    @api.model
    def _load_pos_data_fields(self, config):
        res = super()._load_pos_data_fields(config)
        return list(set(res + POS_ACCESS_FIELDS))

    def action_pos_preset_full_access(self):
        """Grant Full Access (clear all restrictions)."""
        vals = {f: False for f in POS_ACCESS_FIELDS if f != 'sbl_pos_max_discount_pct'}
        vals['sbl_pos_max_discount_pct'] = 0.0
        self.write(vals)

    def action_pos_preset_standard_cashier(self):
        """Apply Standard Cashier Preset."""
        self.action_pos_preset_full_access()
        self.write({
            'sbl_hide_pos_delete_order_button': True,
            'sbl_disable_pos_change_price': True,
            'sbl_disable_pos_discount_button': True,
            'sbl_hide_pos_dropdown_cash_inout': True,
            'sbl_hide_pos_dropdown_create_product': True,
            'sbl_hide_pos_dropdown_backend': True,
            'sbl_hide_pos_dropdown_close_register': True,
            'sbl_hide_pos_dropdown_total_session': True,
        })

    def action_pos_preset_order_taker(self):
        """Apply Order Taker / Waiter Preset."""
        self.action_pos_preset_standard_cashier()
        self.write({
            'sbl_hide_pos_payment': True,
            'sbl_disable_pos_line_delete': True,
            'sbl_pos_own_orders_only': True,
        })