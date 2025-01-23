from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    property_id = fields.Many2one('property.property')


    def action_confirm(self):
        res = super(SaleOrder,self).action_confirm()
        print("Haaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        return res


class ResPartner(models.Model):
    _inherit = 'res.partner'

    price = fields.Float()
