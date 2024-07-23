from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    second_email = fields.Char(string='Second Email')
    related_email = fields.Char(string='Related Email', compute='_compute_related_email')

    @api.depends('parent_id.email')
    def _compute_related_email(self):
        for partner in self:
            partner.related_email = partner.parent_id.email if partner.parent_id else False

