from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResPassenger(models.Model):
    _name = 'res.passenger'
    _description = 'Passenger'

    name = fields.Char(string='Name')
    weight = fields.Float(string='Weight(kg)')
    height = fields.Float(string='Height(kg)')
    born_date = fields.Date(string='Born Date')