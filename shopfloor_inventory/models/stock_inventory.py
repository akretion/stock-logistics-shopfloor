# Copyright 2020 Camptocamp SA (http://www.camptocamp.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class StockInventory(models.Model):
    _inherit = "stock.inventory"

    shopfloor_validated = fields.Boolean(
        string="To validate",
        help="Shopfloor doesn't validate the inventory at the end of the process. "
        "The manager can do it manually.",
        tracking=True,
        copy=False,
    )
