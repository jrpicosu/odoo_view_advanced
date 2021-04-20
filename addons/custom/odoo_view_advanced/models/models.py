# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions


class CustomItem(models.Model):
    _name = 'odoo_view_advanced.custom_item'

    name = fields.Char(string='Descripción')
    unit_price = fields.Char(string='Precio unitario')










