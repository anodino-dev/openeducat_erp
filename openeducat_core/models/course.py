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

from odoo import models, fields


class OpCourse(models.Model):
    _name = 'op.course'
    _inherit = ['website.seo.metadata']
    
    name = fields.Char('Name', required=True)
    code = fields.Char('Code', size=16, required=True)
    parent_id = fields.Many2one('op.course', 'Parent Course')
    section = fields.Char('Section', size=32)
    evaluation_type = fields.Selection(
        [('normal', 'Normal'), ('GPA', 'GPA'), ('CWA', 'CWA'), ('CCE', 'CCE')],
        'Evaluation Type', default="normal", required=True)
    subject_ids = fields.One2many(
        'op.subject', 'course_id', string='Subject(s)')
    batch_ids = fields.One2many(
        'op.batch', 'course_id', string='Batch(es)')
    faculty_ids = fields.Many2many('op.faculty','faculty_course_rel')
    
    fullname = fields.Char(required=True)
    
    summary = fields.Html()
    
    category_ids = fields.Many2many('product.category')
       
    topic_ids = fields.One2many('op.course.topic','course_id')
    
    max_unit_load = fields.Float("Maximum Unit Load")
    min_unit_load = fields.Float("Minimum Unit Load")

    _sql_constraints = [
        ('unique_course_code',
        'unique(code)', 'Code should be unique per course!')]


class OpCourseTopic(models.Model): 
    _name='op.course.topic'
    
    name = fields.Char()
    course_id = fields.Many2one('op.course', required=True)
    sequence = fields.Integer()
    
    