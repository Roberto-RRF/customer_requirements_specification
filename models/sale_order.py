from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    customer_requirement_ids = fields.One2many(
        'customer.requirement.detail', 'partner_id', string='Customer Requirements', 
        compute='_compute_customer_requirements', store=False)

    @api.depends('partner_id')
    def _compute_customer_requirements(self):
        for order in self:
            # Search for customer requirements where the partner_id matches the customer
            # and category_ids contains 'Ventas'
            requirements = self.env['customer.requirement.detail'].search([
                ('partner_id', '=', order.partner_id.id),
                ('category_ids.name', '=', 'Ventas')
            ])
            order.customer_requirement_ids = requirements