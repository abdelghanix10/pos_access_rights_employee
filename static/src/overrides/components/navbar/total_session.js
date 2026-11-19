/** @odoo-module */

import { Component, onMounted, proxy } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/hooks/pos_hook";
import { formatCurrency } from "@web/core/currency";

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

    get formattedAmount() {
        if (this.state.amount === null) {
            return "-";
        }
        const currencyId = this.pos?.currency?.id || this.pos?.config?.currency_id?.id;
        try {
            return currencyId
                ? formatCurrency(this.state.amount, currencyId)
                : Number(this.state.amount).toFixed(2);
        } catch {
            return Number(this.state.amount).toFixed(2);
        }
    }
}

export default TotalSession;