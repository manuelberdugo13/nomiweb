from django.shortcuts import render
from apps.companies.models import Liquidacion
from io import BytesIO
from xhtml2pdf import pisa
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from apps.components.settlementgenerator import settlementgenerator



def settlementlist(request):
    liquidaciones = Liquidacion.objects.all()
    
    
    
    
    return render(request, 'companies/settlementlist.html',{
        'liquidaciones':liquidaciones,
    } )

def settlementlistdownload(request,idliqui):
    
    context = settlementgenerator(idliqui)

    html_string = render(request, './html/liquidacion.html', context).content.decode('utf-8')
    
    fecha_actual = datetime.now().strftime('%Y-%m-%d')
    
    pdf = BytesIO()
    pisa_status = pisa.CreatePDF(html_string, dest=pdf)
    pdf.seek(0)

    if pisa_status.err:
        return HttpResponse('Error al generar el PDF', status=400)
    
    nombre_archivo = f'Certificado_{context["cc"]}_{fecha_actual}.pdf'

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{nombre_archivo}"'
    
    return response