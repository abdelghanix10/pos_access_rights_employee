/** @odoo-module */

import { Component, proxy, onMounted } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/hooks/pos_hook";

export class TotalSession extends Component {
    static template = "pos_access_rights_employee.TotalSession";

    setup() {
        super.setup(...arguments);
        this.pos = usePos();
        // OWL 3 in Odoo 20 uses proxy() instead of useState()
        this.state = proxy({ amount: null });

        onMounted(() => {
            this.pos
                .getClosePosInfo()
                .then((info) => {
                    this.state.amount =
                        info?.default_cash_details?.amount ??
                        info?.orders_details?.amount ??
                        0;
                })
                .catch(() => {
                    this.state.amount = 0;
                });
        });
    }
}

export default TotalSession;