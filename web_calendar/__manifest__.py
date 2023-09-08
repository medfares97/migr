# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Web Calendar',
    'category': 'Hidden',
    'version': '2.0',
    'author': 'Odoo SA, Valentino Lab (Kalysto)',
    'depends': ['web'],
    'data': [
        'views/web_calendar_templates.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'auto_install': True,
    'application': False,  # Remplace auto_install
}

