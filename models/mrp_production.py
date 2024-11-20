from odoo import models, fields, api

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    customer_requirement_ids = fields.One2many(
        'customer.requirement.detail', 'partner_id', string='Customer Requirements', 
        compute='_compute_customer_requirements', store=False)

    @api.depends('sale_order_client')
    def _compute_customer_requirements(self):
        for production in self:
            if production.sale_order_client:
                partner_id = self.env['res.partner'].search([('name','=',production.sale_order_client)])
                requirements = self.env['customer.requirement.detail'].search([
                    ('partner_id', '=', partner_id.id),
                    ('category_ids.name', '=', 'Produccion')
                ])
                production.customer_requirement_ids = requirements

    def generate_specification_report(self):
        data = {'lines':[]}
        for line in self.customer_requirement_ids:
            data['lines'].append({
                'question':line.requirement_id.name,
                'comments':line.description
            })
        print(data)
        return self.env.ref('customer_requirements_specification.action_specification_report').report_action([], data=data)