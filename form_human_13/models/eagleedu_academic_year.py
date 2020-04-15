from eagle import fields, models, api, _
from eagle.exceptions import ValidationError
from datetime import datetime,date
from calendar import monthrange



class EagleeduAcademicYear(models.Model):
    _name = 'eagleedu.academic.year'
    _description = 'Year Information'
    _rec_name = 'name'

    name = fields.Char(string='Year Name', required=True, help='Name of academic year')
    academic_year_description = fields.Text(string='Description', help="Description about the academic year")
    active = fields.Boolean('Active', default=True,
                            help="If unchecked, it will allow you to hide the Year Information without removing it.")

    @api.model
    def create(self, vals):
        """Over riding the create method and assigning the
        sequence for the newly creating record"""
        vals['sequence'] = self.env['ir.sequence'].next_by_code('eagleedu.academic.year')
        res = super(EagleeduAcademicYear, self).create(vals)
        return res