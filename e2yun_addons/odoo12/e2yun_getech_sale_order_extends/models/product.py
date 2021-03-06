# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing tailsde.
from odoo import models, fields, api, exceptions
import datetime
import suds.client
import json


class ProductCategory(models.Model):
    _inherit = 'product.category'

    code = fields.Char('Code')

    @api.multi
    def name_get(self):
        return [(record.id, "%s:%s" % (record.code, record.name)) for record in self]


class Product(models.Model):
    _inherit = 'product.template'

    @api.model
    def create(self, vals):
        res = super(Product, self).create(vals)
        if res:
            if 'default_code' not in vals and not res.default_code:
                if res.categ_id:
                    if res.categ_id.code:
                        default_code = self.env['ir.sequence'].get_next_code_info_if_no_create('product', res.categ_id.code, '', 7)
                        res.default_code = default_code
                    else:
                        raise exceptions.Warning('产品类别没有配置code，请配置后重试！')
            elif 'default_code' in vals:
                res.default_code = vals['default_code']
        return res
