from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

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
                ('category_ids.name', '=', 'Embarques')
            ])
            order.customer_requirement_ids = requirements

    def generate_specification_report(self):
        data = {'lines':[]}
        for line in self.customer_requirement_ids:
            data['lines'].append({
                'question':line.requirement_id.name,
                'comments':line.description
            })
        return self.env.ref('customer_requirements_specification.action_specification_report').report_action([], data=data)