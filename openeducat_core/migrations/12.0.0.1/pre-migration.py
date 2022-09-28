# -*- coding: utf-8 -*-
# Copyright 2017 Tecnativa - Vicent Cubells
# Copyright 2017-2018 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import logging

from odoo import api, SUPERUSER_ID

logger = logging.getLogger(__name__)


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    logger.debug('pre-migration {}'.format(version))
    env.cr.execute('update res_partner set first_name=btrim(first_name), last_name=btrim(last_name)')
    env.cr.execute('update res_partner set firstname=first_name, lastname=last_name')