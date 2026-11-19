/** @odoo-module */

import { BurgerMenuDialog } from "@point_of_sale/app/components/navbar/burger_menu/burger_menu_dialog";
import { patch } from "@web/core/utils/patch";
import TotalSession from "./total_session";

patch(BurgerMenuDialog, {
    components: { ...BurgerMenuDialog.components, TotalSession },
});