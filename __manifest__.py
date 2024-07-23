{
    'name': 'Custom mail Contact Fields',
    'version': '1.0',
    'summary': 'Add second email field to contacts',
    'description': 'This module adds a second email field to the contact model',
    'author': 'Icloud Solutions',
    'depends': ['base', 'contacts'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
}
