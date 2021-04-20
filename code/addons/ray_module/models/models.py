# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class ray_module(models.Model):
#     _name = 'ray_module.ray_module'
#     _description = 'ray_module.ray_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class Wallet(models.Model):
    _name='ray_module.wallet'

    name = fields.Char()
    balance = fields.Integer()