from datetime import datetime
from odoo import models,fields, api, exceptions, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
import logging

logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    '''
    classdocs
    '''

    _inherit ='res.partner'
    
    first_name= fields.Char()
    last_name= fields.Char()
    student = fields.Boolean()
    faculty = fields.Boolean()