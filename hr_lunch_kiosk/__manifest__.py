# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Hr Attendance Lunch Time Kiosk Mode',
    'version': '14.0.3.0',
    'category': 'Human Resources/Attendances',
    'author': 'Dev JS',
    'sequence': 99,
    'summary': 'Lunch Start Time And End Time  Hr Attendance In Kiosk Mode',
    'depends': [
        'hr_lunch_time',
    ],
    'data': [
        'menu/menu.xml'
    ],
    'demo': [],
    'images': [
        'static/description/banner.png'
    ],
    'installable': True,
    'auto_install': False,
    'qweb': [
        'static/src/xml/attendance.xml',
    ],
    'application': True,
    'price': 20,
    'currency': 'EUR',
    'license': 'LGPL-3',
}
