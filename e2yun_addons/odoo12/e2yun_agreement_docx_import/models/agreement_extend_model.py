# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _


class Agreement(models.Model):  #合同
    _inherit = "agreement"

    # def create(self, vals_list):
    #     print(vals_list)
    #     return super(Agreement,self).create(vals_list)



class AgreementRecital(models.Model):  #叙述
    _inherit = "agreement.recital"
    doc_text = fields.Char('Doc Text')

class AgreementSection(models.Model):  #章节
    _inherit = "agreement.section"
    doc_text = fields.Char('Doc Text')



class AgreementClause(models.Model):  #条款
    _inherit = "agreement.clause"
    doc_text = fields.Text('Doc Text')
    master_word_id = fields.Integer('Master Word Id')
    the_editor = fields.Boolean('The Editor')

    # def create(self, vals_list):
    #     print(vals_list)
    #     return super(AgreementClause,self).create(vals_list)
    #
    def write(self, vals_list):
        vals_list['the_editor']=True
        return super(AgreementClause,self).write(vals_list)



class AgreementAppendix(models.Model):  #附录
    _inherit = "agreement.appendix"
    doc_style = fields.Char('Doc Style')










