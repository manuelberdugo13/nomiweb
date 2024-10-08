from django.shortcuts import redirect


def redirect_by_role(user):
    role_views = {
        'administrator': 'admin:admin',
        'accountant': 'accountant_dashboard',
        'employees': 'employees:index_employees',
        'entrepreneur': 'companies:index_companies',
    }
    role = user
    return redirect(role_views.get(role, 'login:login'))

def redirect_by_role2(user):
    role_views = {
        'administrator': 'admin:admin',
        'accountant': 'accountant_dashboard',
        'employees': 'employees:index_employees',
        'entrepreneur': 'companies:index_companies',
    }
    role = user
    return role_views.get(role, 'error_page')

