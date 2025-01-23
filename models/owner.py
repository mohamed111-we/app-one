from odoo import models, fields, api, _


class Owner(models.Model):
    _name = 'owner.owner'

    name = fields.Char(string="Name", required=1)
    phone = fields.Char(string="Phone", required=1)
    address = fields.Char(string="Address")

    property_ids = fields.One2many('property.property','owner_id')