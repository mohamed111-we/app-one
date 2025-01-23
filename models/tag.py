from odoo import models, fields, api, _


class Tag(models.Model):
    _name = 'tag.tag'

    name = fields.Char(string="Name", required=1)


