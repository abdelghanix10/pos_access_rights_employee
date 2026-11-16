# POS Access Rights Employee (Odoo 20)

**Module Name:** `pos_access_rights_employee`  
**Version:** `20.0.2.0.0`  
**License:** LGPL-3  

## Overview

The **POS Access Rights Employee** module for **Odoo 20** provides granular, per-employee permission controls over the Point of Sale (POS) interface. Administrators can enable or disable specific buttons, numpad actions, pricing rules, and menu items for each cashier or employee—either individually or using one-click role presets.

---

## Features

### 1. One-Click Role Presets
Quickly configure employee permissions from the **POS Access Rights** tab on the Employee form:
- **Grant Full POS Access**: Clears all restrictions so the employee has full POS access.
- **Preset: Standard Cashier**: Restricts Delete Order, Change Price, Discount, Cash In/Out, Create Product, Backend, Close Register, and Total Session.
- **Preset: Order Taker (No Payment)**: Applies Standard Cashier restrictions plus hides Payment, disables Orderline Backspace/Delete, and restricts the Ticket Screen to the employee's own orders.

### 2. Order Management & Navbar Controls
- **Hide POS Orders Button**: Hides the New Order (`+`) and Ticket Screen buttons.
- **Hide POS Delete Order Button**: Prevents employees from deleting orders on the Ticket Screen.
- **Show Only Own Orders in Ticket Screen**: Restricts the Ticket Screen list so employees only see orders assigned to them.
- **Hide POS Customer Selection Button**: Prevents selecting or changing the customer on an order.
- **Hide POS Actions Button**: Hides the *Actions* (`More`) button.
- **Hide POS Payment**: Hides the *Payment* button on the Product Screen and Actionpad.
- **Hide POS Note Button**: Hides the *Internal Note* button.
- **Hide POS Transfer Order Button**: Hides the *Save / Transfer Order* button.
- **Hide POS Barcode Button**: Hides the Barcode Scanner button in the navbar.
- **Hide POS Search Input**: Hides the *Search products...* bar in the navbar.
- **Hide POS Customer Display**: Hides the Customer Display button.
- **Hide POS Product Info Popup**: Prevents opening the Product Info popup on product cards.

### 3. Numpad & Pricing Controls
- **Hide POS Numpad**: Completely hides the Numpad on the Product Screen.
- **Disable POS Change Price**: Disables the `Price` button on the Numpad.
- **Disable POS Quantity (QTY) Button**: Disables the `Qty` button on the Numpad.
- **Disable Orderline Backspace / Delete**: Disables the `⌫` (Backspace) button and prevents reducing an orderline's quantity to `0` or removing lines.
- **Disable POS Numpad Plus-Minus (`+/-`) Buttons**: Disables sign-switching (`+/-`) on the Numpad.
- **Disable POS Discount Button**: Disables the `%` (Discount) button on the Numpad.
- **Max Allowed Discount (%)**: When the Discount button is enabled, caps the maximum discount percentage an employee can apply (e.g., `10%`), displaying a warning if exceeded.

### 4. Dropdown Navbar Menu Controls
- **Hide POS Dropdown Navbar**: Hides the entire top-right burger menu in the POS navbar.
- **Individual Menu Item Controls** *(when Dropdown Navbar is visible)*:
  - **Hide Install App**
  - **Hide Cash In/Out**
  - **Hide Reload Data**
  - **Hide Create Product**
  - **Hide Barcode Scanner**
  - **Hide Print Report**
  - **Hide Backend**
  - **Hide Close Register**
  - **Hide Total Session (Register)**: Controls visibility of the live *Total Session* cash counter inside the dropdown menu.

---

## Configuration

1. Navigate to the **Employees** app (**Employees → Employees**).
2. Open an employee profile.
3. Click on the **POS Access Rights** tab.
4. Click one of the **Preset** buttons at the top, or toggle individual switches under:
   - **Order Management & Navbar**
   - **Numpad & Pricing Controls**
   - **Dropdown Navbar Menu**
5. Save the employee record and reload/open the POS session.

---

## Technical Details (Odoo 20)

- **Odoo Version**: `20.0.2.0.0`
- **Dependencies**: `pos_hr` (which includes `point_of_sale` and `hr`)
- **Odoo 20 Architecture**:
  - **Unified Security**: Uses `security/ir.access.csv` (`ir.access` model).
  - **OWL 3 Frontend**: Uses `proxy()` reactive state, mandatory `this.` template bindings, and `t-out` QWeb directives.
  - **POS Data Loader**: Extends `_load_pos_data_fields` on both `hr.employee` and `res.users`.

---

## Installation

1. Copy the `pos_access_rights_employee` folder into your Odoo 20 `addons` directory.
2. Restart the Odoo server.
3. Enable **Developer Mode** and navigate to **Apps → Update Apps List**.
4. Search for **POS Access Rights Employee** and click **Activate**.

---

## License

LGPL-3