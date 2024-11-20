from odoo import models, fields, api

class CustomerRequirement(models.Model):
    _name = 'customer.requirement'
    _description = 'Customer Requirement'

    name = fields.Char(string='Nombre Requerimiento')
    predefined_category_ids = fields.Many2many(
        'customer.requirement.category', string="Categorias predefinidas",
    )
