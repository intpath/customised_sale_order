
from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    text1 = fields.Text('Text 1')
    text2 = fields.Text('Text 2')
