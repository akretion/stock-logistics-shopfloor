# Copyright 2020 Akretion (http://www.akretion.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Shopfloor Inventory",
    "summary": "Manage stock inventories with barcode scanners",
    "version": "18.0.1.0.0",
    "development_status": "Beta",
    "category": "Inventory",
    "website": "https://github.com/OCA/stock-logistics-shopfloor",
    "author": "Akretion, Odoo Community Association (OCA)",
    "maintainers": ["FranzPoize", "bguillot"],
    "license": "AGPL-3",
    "application": False,
    "depends": [
        # OCA/stock-logistics-shopfloor
        "shopfloor",
        # OCA/stock-logistics-warehouse
        "stock_inventory",
        "stock_inventory_restriction",
        "stock_inventory_location_state",
    ],
    "data": [
        "data/shopfloor_scenario_data.xml",
        "views/shopfloor_menu.xml",
        "views/stock_inventory.xml",
    ],
    "demo": [
        "demo/shopfloor_menu_demo.xml",
    ],
    "installable": True,
    "post_init_hook": "post_init_hook",
    "uninstall_hook": "uninstall_hook",
}
