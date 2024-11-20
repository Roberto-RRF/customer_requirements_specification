from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_requirement_ids = fields.One2many(
        'customer.requirement.detail', 'partner_id', string='Customer Requirements')
    
    requirement_ids = fields.Many2many(
        'customer.requirement',
        string="Conceptos Existentes",
        compute="_compute_requirement_ids",
        store=False
    )
 
    @api.depends('customer_requirement_ids.requirement_id')
    def _compute_requirement_ids(self):
        for partner in self:
            partner.requirement_ids = partner.customer_requirement_ids.mapped('requirement_id')