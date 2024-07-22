# -*- coding: utf-8 -*-
# from odoo import http


# class LmwWriterManagement(http.Controller):
#     @http.route('/lmw_writer_management/lmw_writer_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lmw_writer_management/lmw_writer_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lmw_writer_management.listing', {
#             'root': '/lmw_writer_management/lmw_writer_management',
#             'objects': http.request.env['lmw_writer_management.lmw_writer_management'].search([]),
#         })

#     @http.route('/lmw_writer_management/lmw_writer_management/objects/<model("lmw_writer_management.lmw_writer_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lmw_writer_management.object', {
#             'object': obj
#         })

