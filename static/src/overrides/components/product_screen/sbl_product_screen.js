/** @odoo-module */

import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";

patch(ProductScreen.prototype, {
  getNumpadButtons() {
    const buttons = super.getNumpadButtons(...arguments);
    const employee = this.pos.cashier || {};

    for (const button of buttons) {
      if (button.value === "quantity") {
        button.disabled =
          button.disabled || Boolean(employee.sbl_disable_pos_qty);
      }
      if (button.value === "price") {
        button.disabled =
          button.disabled || Boolean(employee.sbl_disable_pos_change_price);
      }
      if (button.value === "discount") {
        button.disabled =
          button.disabled || Boolean(employee.sbl_disable_pos_discount_button);
      }
      if (button.value === "-") {
        button.disabled =
          button.disabled ||
          Boolean(employee.sbl_disable_pos_numpad_plus_minus);
      }
      if (button.value === "Backspace") {
        button.disabled =
          button.disabled || Boolean(employee.sbl_disable_pos_line_delete);
      }
    }

    const clickButton = buttons.find(
      (button) => button.value === this.pos.numpadMode,
    );
    if (clickButton) {
      for (const button of buttons) {
        if (
          !["quantity", "discount", "price", "-", "Backspace"].includes(
            button.value,
          )
        ) {
          button.disabled = clickButton.disabled;
        }
      }
    }
    return buttons;
  },

  async _setValue(val) {
    const employee = this.pos.cashier || {};
    const { numpadMode } = this.pos;

    // Enforce Disable Orderline Deletion / Zero Quantity via Backspace
    if (
      numpadMode === "quantity" &&
      employee.sbl_disable_pos_line_delete &&
      (val === "remove" || val === "" || Number(val) <= 0)
    ) {
      this.notification?.add(
        _t("You do not have permission to delete order lines."),
        { type: "warning" },
      );
      this.numberBuffer?.reset();
      return;
    }

    // Enforce Maximum Allowed Discount %
    const maxDisc = Number(employee.sbl_pos_max_discount_pct || 0);
    if (numpadMode === "discount" && maxDisc > 0 && Number(val) > maxDisc) {
      this.notification?.add(
        _t("Maximum allowed discount for your role is %s%%.", maxDisc),
        { type: "warning" },
      );
      this.numberBuffer?.reset();
      return super._setValue(String(maxDisc));
    }

    return super._setValue(...arguments);
  },
});
