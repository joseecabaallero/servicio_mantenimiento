# servicio_manteminiento/__manifest__.py
{
    'name': 'Servicio de Mantenimiento',
    'version': '1.0',
    'author': 'José David',
    'category': 'Custom',
    'summary': 'Gestión de Mantenimiento de Productos',
    'depends': ['base', 'garantia.producto'],
    'data': [
        'views/servicio_mantenimiento_views.xml',
        'security/ir.model.access.csv',
    ],
    'icon': '/garantias/static/description/icon55.png',
    'installable': True,
    'application': True,    
}