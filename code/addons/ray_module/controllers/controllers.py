# -*- coding: utf-8 -*-
from odoo import http


class RayModule(http.Controller):

    @http.route('/wallets', auth='public', website=True)
    def index(self, **kw):
        wallets = http.request.env['ray_module.wallet']
        return http.request.render(
            'ray_module.index', 
            {
                'wallets': wallets.search([])
            }
        )

