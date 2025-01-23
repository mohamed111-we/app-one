from odoo import _, api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    property_id = fields.Many2one('property.property')
    # price = fields.Float(related='property_id.selling_price')  #  1 way
    price = fields.Float(compute="_compute_price")               #  2 way

    @api.depends('property_id')
    def _compute_price(self):
        for rec in self:
            rec.price = rec.property_id.selling_price