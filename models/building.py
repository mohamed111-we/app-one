from odoo import models, fields, api, _


class Building(models.Model):
    _name = 'building.building'
    _description = 'Building Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    num = fields.Integer()
    code = fields.Char()
    description = fields.Text()
    active = fields.Boolean(string="Active", default=True)
    name = fields.Char()

