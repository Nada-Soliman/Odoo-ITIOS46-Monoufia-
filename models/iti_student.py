from odoo import models, fields

class ITIStudent(models.Model):
    _name = 'iti.student'

    name = fields.Char()
    age = fields.Integer()
    info = fields.Text()
    is_accepted = fields.Boolean()
    birth_date = fields.Date()
    image = fields.Binary()
    gender = fields.Selection([('female','F'),('male','M')])
