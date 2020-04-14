from eagle import fields, models, api, _

class EagleeduHuman(models.Model):
    _name = 'eagleedu.student'
    _inherits = {'res.partner': 'partner_id'}
    _description = 'This the application for Human'
    _order = 'id desc'
    _rec_name = 'name'

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if name:
            recs = self.search([('name', operator, name)] + (args or []), limit=limit)
            if not recs:
                recs = self.search([('adm_no', operator, name)] + (args or []), limit=limit)
            if not recs:
                recs = self.search([('application_no', operator, name)] + (args or []), limit=limit)
            return recs.name_get()
        return super(EagleeduHuman, self).name_search(name, args=args, operator=operator, limit=limit)

    @api.model
    def create(self, vals):
        """Over riding the create method to assign sequence for the newly creating the record"""
        vals['adm_no'] = self.env['ir.sequence'].next_by_code('eagleedu.student')
        res = super(EagleeduHuman, self).create(vals)
        return res

    partner_id = fields.Many2one(
        'res.partner', string='Partner', required=True, ondelete="cascade")
    adm_no = fields.Char(string="Admission No.", readonly=True)
    image_1920 = fields.Binary(string='Image', help="Provide the image of the Human")
    application_no = fields.Char(string='Application  No', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.user.company_id)
    academic_year = fields.Many2one('eagleedu.academic.year', string= "Year Information", help="Select Year")

    st_name_b = fields.Char(string='Human Bangla Name')
    date_of_birth = fields.Date(string="Date Of birth")
    st_gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                                string='Gender', required=False, track_visibility='onchange')
    st_blood_group = fields.Selection([('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('o+', 'O+'), ('o-', 'O-'),
                                    ('ab-', 'AB-'), ('ab+', 'AB+')], string='Blood Group', track_visibility='onchange')
    st_passport_no = fields.Char(string="Passport No.", help="Proud to say my father is", required=False)
    application_no = fields.Char(string='Registration No', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))
    registration_date = fields.Datetime('Registration Date', default=lambda
        self: fields.datetime.now())  # , default=fields.Datetime.now, required=True

    st_father_name = fields.Char(string="Father's Name", help="Proud to say my father is", required=False)
    st_father_name_b = fields.Char(string="বাবার নাম", help="Proud to say my father is")
    st_father_occupation = fields.Char(string="Father's Occupation", help="father Occupation")
    st_father_email = fields.Char(string="Father's Email", help="father Occupation")
    father_mobile = fields.Char(string="Father's Mobile No", help="Father's Mobile No")
    st_mother_name = fields.Char(string="Mother's Name", help="Proud to say my mother is", required=False)
    st_mother_name_b = fields.Char(string="মা এর নাম", help="Proud to say my mother is")
    st_mother_occupation = fields.Char(string="Mother Occupation", help="Proud to say my mother is")
    st_mother_email = fields.Char(string="Mother Email", help="Proud to say my mother is")
    mother_mobile = fields.Char(string="Mother's Mobile No", help="mother's Mobile No")

    house_no = fields.Char(string='House No.', help="Enter the House No.")
    road_no = fields.Char(string='Area/Road No.', help="Enter the Area or Road No.")
    post_office = fields.Char(string='Post Office', help="Enter the Post Office Name")
    city = fields.Char(string='City', help="Enter the City name")
    bd_division_id = fields.Many2one('eagleedu.bddivision', string= 'Division')
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict',default=19)

    if_same_address = fields.Boolean(string="Permanent Address same as above", default=True)
    per_village = fields.Char(string='Village Name', help="Enter the Village Name")
    per_po = fields.Char(string='Post Office Name', help="Enter the Post office Name ")
    per_ps = fields.Char(string='Police Station', help="Enter the Police Station Name")
    per_dist_id = fields.Many2one('eagleedu.bddistrict', string='District', help="Enter the City of District name")
    per_bd_division_id = fields.Many2one('eagleedu.bddivision', string='Division/Province', help="Enter the Division name")
    per_country_id = fields.Many2one('res.country', string='Country', ondelete='restrict', default=19)

    guardian_name = fields.Char(string="Guardian's Name", help="Proud to say my guardian is")
    guardian_mobile = fields.Char(string="Guardian's Mobile")

    religious_id = fields.Many2one('eagleedu.religious', string="Religious", help="My Religion is ")
    student_id=fields.Char('Human Id')
    email = fields.Char(string="Email", help="Enter E-mail id for contact purpose")
    phone = fields.Char(string="Phone", help="Enter Phone no. for contact purpose")
    mobile = fields.Char(string="Mobile", help="Enter Mobile num for contact purpose")
    nationality = fields.Many2one('res.country', string='Nationality', ondelete='restrict',default=19,
                                  help="Select the Nationality")
    state = fields.Selection([('draft', 'Draft'), ('approve', 'Approve'), ('done', 'Done')],
                              string='Status', required=True, default='draft', track_visibility='onchange')

    def send_to_publish(self):
        """Return the state to done if the documents are perfect"""
        for rec in self:
            rec.write({
                'state': 'approve'
            })


    def create_human(self):
        """Create student from the application and data and return the student"""
        for rec in self:
            values = {
                'name': rec.name,
                # 'st_name_b': rec.st_name_b,
                'image_1920': rec.image_1920,
                # 'application_no': rec.id,
                # 'st_father_name': rec.st_father_name,
                # 'st_father_name_b': rec.st_father_name_b,
                # 'father_mobile': rec.father_mobile,
                # 'st_father_occupation': rec.st_father_occupation,
                # 'st_mother_name': rec.st_mother_name,
                # 'st_mother_name_b': rec.st_mother_name_b,
                # 'mother_mobile': rec.mother_mobile,
                # 'st_mother_occupation': rec.st_mother_occupation,
                # 'st_gender': rec.st_gender,
                # 'date_of_birth': rec.date_of_birth,
                # 'st_blood_group': rec.st_blood_group,
                # 'st_passport_no': rec.st_passport_no,
                # 'nationality': rec.nationality.id,
                # 'academic_year': rec.academic_year.id,
                # 'standard_class': rec.standard_class.id,
                # 'group_division': rec.group_division.id,
                # 'house_no': rec.house_no,
                # 'road_no': rec.road_no,
                # 'post_office': rec.post_office,
                # 'city': rec.city,
                # 'bd_division_id': rec.bd_division_id.id,
                # 'country_id': rec.country_id.id,
                # 'per_village': rec.per_village,
                # 'per_po': rec.per_po,
                # 'per_ps': rec.per_ps,
                # 'per_dist_id': rec.per_dist_id.id,
                # 'per_bd_division_id': rec.per_bd_division_id.id,
                # 'per_country_id': rec.per_country_id.id,
                # 'guardian_name': rec.guardian_name,
                # 'religious_id': rec.religious_id.id,
                # # 'is_student': True,
                # 'student_id': rec.student_id,
                # 'roll_no': rec.roll_no,
                # 'application_no': rec.application_no,
            }
            student = self.env['product.template'].create(values)
            rec.write({
                'state': 'done'
            })
            return {
                'name': _('Human'),
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'product.template',
                'type': 'ir.actions.act_window',
                'res_id': student.id,
                'context': self.env.context
            }