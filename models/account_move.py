from odoo import _, api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_do_something(self):
        print(self, 'action_do_something')