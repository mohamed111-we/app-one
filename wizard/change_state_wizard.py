from docutils.core import default_usage
from odoo import fields, models


class ChangeState(models.TransientModel):
    _name = 'change.state'

    property_id = fields.Many2one('property.property')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
    ], default='draft')
    reason = fields.Char()

    def action_confirm(self):
        if self.property_id.state == 'closed':
            self.property_id.state = self.state
            self.property_id.create_history_record('closed', self.state, self.reason)
