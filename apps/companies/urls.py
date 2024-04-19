from django.urls import path
from .views.ContractsList import ContractsList
from .views.newEmployee import newEmployee
from .views.EditEmployee import EditEmployee
from .views.editContract import editContract
from .views.newContract import newContract


urlpatterns = [
    ##todo novedades de nomina 
    path('companies/contract', ContractsList.startCompanies , name='startcompanies'),
    
    path('companies/new/employee', newEmployee.newEmployee , name='newemployee'),
    path('companies/edit/employee',  EditEmployee.EditEmployeeSearch , name='editemployeesearch'),
    path('companies/edit/employee/<str:idempleado>',  EditEmployee.EditEmployeeVisual , name='editemployeevisual'),
    
    path('companies/edit/contrac',editContract.EditContracsearch , name='editcontracsearch'),
    path('companies/edit/contrac/<str:idempleado>',editContract.EditContracVisual , name='editcontracvisual'),
    
    path('companies/edit/contract',editContract.EditContracsearch , name='editcontracsearch'),
    path('companies/edit/contract/<str:idempleado>',editContract.EditContracVisual , name='editcontracvisual'),
    
    
    
    ##! empleados 
    
    ##! parametros 
    
    ##! contabilidad 
    
    
    #* ## server -- errores 
    
    ##// admin login 
    # path('logout/', views.Logout, name='logout'),
]

# EditResume
