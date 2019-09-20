# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class OpFaculty(models.Model):
    _name = 'op.faculty'
    _inherits = {
#                'res.partner': 'partner_id',
                'hr.employee': 'emp_id'
                 }
    _inherit =[ 'mail.thread' ]

    active = fields.Boolean(track_visibility='onchange',default=True)
    partner_id = fields.Many2one(
        'res.partner', 'Partner', related='address_home_id', ondelete="restrict")
    emp_id = fields.Many2one('hr.employee', 'Employee',required=True, ondelete="cascade")
    first_name = fields.Char('First Name', size=128, required=True)
#     middle_name = fields.Char('Middle Name', size=128)
    last_name = fields.Char('Last Name', size=128, required=True)
#     birth_date = fields.Date('Birth Date', required=True)
#     blood_group = fields.Selection(
#         [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
#          ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
#         'Blood Group')
#     gender = fields.Selection(
#          [('male', 'Male'), ('female', 'Female')], 'Gender', required=True)
#     nationality = fields.Many2one('res.country', 'Nationality')
#     emergency_contact = fields.Many2one(
#         'res.partner', 'Emergency Contact')
#     visa_info = fields.Char('Visa Info', size=64)
#     id_number = fields.Char('ID Card Number', size=64)
#     login = fields.Char(
#         'Login', related='emp_id.user_id.login', readonly=1)
#     last_login = fields.Datetime(
#         'Latest Connection', related='emp_id.user_id.login_date',
#         readonly=1)
    faculty_subject_ids = fields.Many2many('op.subject', string='Subject(s)' ,track_visibility='onchange')
    course_ids =  fields.Many2many('op.course', 'faculty_course_rel', string='Course(s)' ,track_visibility='onchange')
    contact_address = fields.Char(related="address_home_id.contact_address")
    work_function = fields.Char()
    career = fields.Char()
    curriculum = fields.Html()
    batch_ids = fields.Many2many('op.batch','batch_faculty_rel',string="Batch(es)" ,track_visibility='onchange')
    street =fields.Char(related='address_home_id.street')
    street2 =fields.Char(related='address_home_id.street2')
    city =fields.Char(related='address_home_id.city')
    zip =fields.Char(related='address_home_id.zip')
    state_id =fields.Many2one(related='address_home_id.state_id')
    country_id =fields.Many2one(related='address_home_id.country_id')
        
    @api.onchange('first_name','last_name')
    def _onchange_name(self):
        if self.first_name and self.last_name:
            self.name = u'{} {}'.format(self.first_name,self.last_name)

    @api.model
    def create(self,data):
        if not data.get("name") and 'first_name' in data and 'last_name' in data:
            data.update(name=u'{} {}'.format(data['first_name'],data['last_name']))
        record=super(OpFaculty, self).create(data)
        vals = data
        vals.update(
            phone=record.work_phone,
            mobile = record.mobile_phone,
            vat = record.identification_id,
            email = record.work_email,
            supplier = True,
            employee = True,
            customer = False,
                        
            )
        partner = self.env['res.partner'].create(vals)
        record.write({'address_home_id': partner.id})
        return record
