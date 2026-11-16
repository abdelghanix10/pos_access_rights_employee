/** @odoo-module */

import { Navbar } from "@point_of_sale/app/components/navbar/navbar";
import TotalSession from "./total_session";

Navbar.components = Object.assign({}, Navbar.components, { TotalSession });

export default Navbar;