from odoo import models, fields, api

class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    product_brand = fields.Char(string="Brand")

