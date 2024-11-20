from odoo import models, fields, api

class CustomerRequirementDetail(models.Model):
    _name = 'customer.requirement.detail'
    _description = 'Customer Requirement Detail'

    requirement_id = fields.Many2one('customer.requirement', string='Requirement')
    category_ids = fields.Many2many('customer.requirement.category', string='Categories')
    partner_id = fields.Many2one('res.partner', string='Customer')
    description = fields.Char('Description')



        
    @api.onchange('requirement_id')
    def _onchange_requirement_id(self):
        if self.requirement_id:
            self.category_ids = [(6, 0, self.requirement_id.predefined_category_ids.ids)]