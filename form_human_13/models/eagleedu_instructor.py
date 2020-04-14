# -*- coding: utf-8 -*-

from eagle import fields, models, api, _

class EagleeduInstructor(models.Model):
    _name = 'eagleedu.instructor'
    # _inherit = ['mail.thread']
    _description = 'All Teachers Details'

    @api.model
    def create(self, vals):
        """Over riding the create method to assign
        the sequence for newly creating records"""
        vals['instructor_id'] = self.env['ir.sequence'].next_by_code('eagleedu.instructor')
        res = super(EagleeduInstructor, self).create(vals)
        return res

    name = fields.Char(string="Instructor Name", required=True)
    instructor_id = fields.Char(string="Instructor ID No.", readonly=True )
    ins_father_name = fields.Char(string="Father Name")
    ins_mother_name = fields.Char(string="Mother Name")
    ins_mobile_no = fields.Char(string="Mobile no.")
    ins_email = fields.Char(string="Email Address")
    ins_present_address = fields.Char(string="Present Address")
    ins_permanent_address = fields.Char(string="Permanent Address")
    ins_image = fields.Binary(string="Instructor Image")
    ins_gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                                string='Gender', required=False, track_visibility='onchange',
                                help="Your Gender is")
    ins_date_of_birth = fields.Date(string="Date Of birth", help="Enter your DOB")

