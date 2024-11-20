from odoo import models, fields

class CustomerRequirementCategory(models.Model):
    _name = 'customer.requirement.category'
    _description = 'Customer Requirement Category'

    name = fields.Char(string='Nombre Categoria')
