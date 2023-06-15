from odoo import api, fields, models

class Student(models.Model):
    _name = "student.student"
    _inherit = ['mail.thread']
    _description = "Student Info"


    name = fields.Char(string='Name', tracking=True)
    department = fields.Char(string="Department")
    
