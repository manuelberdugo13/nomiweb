from django.shortcuts import redirect


def redirect_by_role(user):
    role_views = {
        'administrator': 'admin_dashboard',
        'accountant': 'accountant_dashboard',
        'employee': 'login:prueba',
        'entrepreneur': 'companies:index_companies',
    }
    role = user
    return redirect(role_views.get(role, 'error_page'))