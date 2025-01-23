from odoo import models, fields, api, _


class Client(models.Model):
    _name = 'client.client'
    _inherit = 'owner.owner'