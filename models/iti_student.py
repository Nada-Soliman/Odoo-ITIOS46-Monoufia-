from odoo import models, fields, api
from odoo.exceptions import  ValidationError
from datetime import date
class ITIStudent(models.Model):
    _name = 'iti.student'

    # _rec_name = 'age'
    name = fields.Char()
    age = fields.Integer(compute='_compute_age')
    graduate_age = fields.Integer(compute='_compute_age')
    info = fields.Text()
    is_accepted = fields.Boolean()
    birth_date = fields.Date()
    image = fields.Binary()
    gender = fields.Selection([('female','F'),('male','M')])

    salary = fields.Float("")
    is_working = fields.Boolean("")
    cv = fields.Html()

    track_id  = fields.Many2one("iti.track")

    track_capacity = fields.Integer(related='track_id.capacity')
    levels = fields.Selection([('level1','Level1'),('level2','Level2'),('level3','Level3')])

    level_log_ids = fields.One2many('iti.student.log','student_id' )
    roll_id = fields.Integer()

    _sql_constraints = [('unique_id','UNIQUE(roll_id)',"Roll Id can't be duplicated ")]

    @api.onchange('is_working')
    def change_salary(self):
        if self.is_working:
            self.salary = 10000
        else:
            self.salary = 0
        return {
            'warning':{
                'title':('State Changed'),
                'message':'Working state is changed to %s'%(self.is_working)
            }
        }

    def action_confirm(self):
        self.levels = 'level3'
        print("at action_confirm")

    def create_level_logs(self):
        vals = {
            'description':"Level Changed to %s"%(self.levels),
            'student_id':self.id
        }
        self.env['iti.student.log'].create(vals)

    @api.constrains('age')
    def check_age(self):
        if self.age<0:
            raise ValidationError("Age must be greater than 0")
        elif self.age==0:
            raise ValidationError("Age can't be zero")

    @api.depends('age', 'graduate_age', 'birth_date')
    def _compute_age(self):
        for rec in self:
            if rec.birth_date:
                today = date.today()
                rec.age = today.year - rec.birth_date.year - (
                        (today.month, today.day) < (rec.birth_date.month, rec.birth_date.day)
                )
                rec.graduate_age = rec.age + 5
            else:
                rec.age = 0
                rec.graduate_age = rec.age + 5




