/** @odoo-module */

import { usePos } from "@point_of_sale/app/hooks/pos_hook";
import { ListContainer } from "@point_of_sale/app/components/list_container/list_container";
import { patch } from "@web/core/utils/patch";

patch(ListContainer.prototype, {
    setup() {
        super.setup(...arguments);
        this.pos = usePos();
    },
});
