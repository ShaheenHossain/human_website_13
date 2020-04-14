# -*- coding: utf-8 -*-

{
    'name': "Eagle Human form",
    'version': '1.1',
    'summary': """This is a e education manament system""",
    'description': """
This module for This is a e education manament system 
    """,
    'author': "Eagle ERP",
    'website': "http://www.eagle-erp.com",
    'support': 'info@eagle-erp.com',
    'category': 'Human',
    'depends': [ 'base', ],
    'data':[
            'views/eagleedu_application.xml',
            'views/eagleedu_student.xml',
            'views/eagleedu_instructor.xml',
            'views/eagleedu_academic_year.xml',
            'security/ir.model.access.csv',
            'reports/print_reports.xml',
            'reports/report_eagleedu_registration.xml',
            # 'data/eagleedu.bddivision.csv',
    ],
    'installable' : True,
    'application' : False,
}

