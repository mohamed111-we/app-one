from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError


class Property(models.Model):
    _name = 'property.property'
    _description = 'Property'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char("Name", required=True, default='Property', tracking=True)
    ref = fields.Char(string='Reference', copy=False, readonly=True, default=lambda x: _('New'))
    description = fields.Text("Description")
    postcode = fields.Char("Postcode", required=True, tracking=True)
    date_availability = fields.Date("Date Available", tracking=True)
    expected_selling_date = fields.Date(string="Expected Selling Date")
    is_late = fields.Boolean(string="Is Late")
    expected_price = fields.Float("Expected Price", tracking=True)
    selling_price = fields.Float("Selling Price", tracking=True)
    diff = fields.Float(string="Difference", compute="_compute_diff", store=True, tracking=True)
    bedrooms = fields.Integer("Bedrooms", required=True, tracking=True)
    living_area = fields.Integer("Living Area", tracking=True)
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area")
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string="Garden Orientation", default='north', tracking=True)
    owner_id = fields.Many2one("owner.owner", string="Owner")
    tag_ids = fields.Many2many("tag.tag", string="Tag")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        ('closed', 'Closed'),
    ],string='States', default='draft', required=True)
    owner_address = fields.Char(related='owner_id.address')
    owner_phone = fields.Char(related='owner_id.phone')
    line_ids = fields.One2many('property.line','property_id')
    active = fields.Boolean(string="Active", default=True)
    owner_count = fields.Integer(compute='_compute_owner_count')

    _sql_constraints = [
        ('uniq_name', 'UNIQUE("name")', "A tag with the same name already exists.")
    ]

    @api.depends('owner_id')
    def _compute_owner_count(self):
        for rec in self:
            if rec.owner_id:
                rec.owner_count = self.env['owner.owner'].search_count([('id', '=', rec.owner_id.id)])
            else:
                rec.owner_count = 0

    @api.depends('expected_price', 'selling_price')
    def _compute_diff(self):
        for rec in self:
            rec.diff = rec.expected_price - rec.selling_price

    @api.constrains('bedrooms')
    def _check_bedrooms(self):
        for rec in self:
            if rec.bedrooms == 0:
                raise ValidationError(
                    _("The number of bedrooms must be a positive integer greater than zero. You entered: %s") % rec.bedrooms)

    def action_draft(self):
        for rec in self:
            # rec.create_history_record(rec.state, 'draft')
            rec.state = 'draft'

    def action_pending(self):
        for rec in self:
            # rec.create_history_record(rec.state, 'pending')
            rec.state = 'pending'

    def action_sold(self):
        for rec in self:
            # rec.create_history_record(rec.state, 'sold')
            rec.state = 'sold'

    def action_closed(self):
        for rec in self:
            # rec.create_history_record(rec.state, 'closed')
            rec.state = 'closed'

    def check_expected_selling_date(self):     # ----  self = 0 values >> property.property() ------
        property_ids = self.search([])         # -----الأقواس الفارغة[] تعني عدم وجود شروط، أي جلب كل السجلات الموجودة في النموذج----
        for rec in property_ids:
            if rec.expected_selling_date and rec.expected_selling_date < fields.Date.today():
                rec.is_late = True

    def action(self):
         # search([('Field Name', 'operation', 'Value')])
         _search = self.env['property.property'].search(['|',('name', '=', 'Property 1'), ('postcode', '!=', '1234')])
         print(_search)


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('ref') or vals['ref'] == _('New'):
                vals['ref'] = self.env['ir.sequence'].next_by_code('property.property') or _('New')
        return super(Property, self).create(vals_list)

    def create_history_record(self, old_state, new_state, reason):
        for rec in self :
            rec.env['property.history'].create({
                'user_id': rec.env.user.id,
                'property_id' : rec.id,
                'old_state' : old_state,
                'new_state' : new_state,
                'reason' : reason or "" ,
            })
    def action_open_change_state_wizard(self):
        action = self.env['ir.actions.actions']._for_xml_id('app_one.change_state_wizard_action')
        action['context'] = {'default_property_id':self.id}
        return action

    def action_view_owner(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'owner.owner',
            'view_mode': 'form',
            'res_id': self.owner_id.id,
        }

class PropertyLine(models.Model):
    _name = 'property.line'

    area = fields.Float('Area')
    description = fields.Char("Description")
    property_id = fields.Many2one('property.property')
































    # -------------CRUD Methods---------------------------------------------------------------------------------------
    ########################################
    # -------------Create Methods------------
    # @api.model_create_multi
    # def create(self, vals):
    #     res = super(Property, self).create(vals)
    #     print("From Create Methods")
    #     return res

    ########################################
    # -------------Search Methods------------
    # def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
    #     res = super(Property, self)._search(domain, offset=0, limit=None, order=None, access_rights_uid=None)
    #     print("From Search Methods")
    #     return res

    ########################################
    # -------------Write Methods------------
    # def write(self, vals):
    #     res = super(Property, self).write(vals)
    #     print("From Write Methods")
    #     return res

    ########################################
    # -------------unlink Methods------------
    # def unlink(self):
    #     res = super(Property, self).unlink()
    #     print("From unlink Methods")
    #     return res

# ------------------------------------------------------------------------------------------------------------------------------------------------------


