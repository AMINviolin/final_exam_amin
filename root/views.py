from django.shortcuts import render, get_object_or_404
from .models import Services,Category,PortFolio



def home(request,category_id = None):
    service = Services.objects.filter(status = True)
    cat = Category.objects.all()
    if category_id:
        selected_category = get_object_or_404(Category,pk =category_id)
        porto = PortFolio.objects.filter(category = selected_category,status=True)
    else:
        porto = PortFolio.objects.filter(status = True)

    context = {
        'service': service,
        'cat': cat,
        'porto': porto,
        'selected_category':int(category_id) if category_id else None,
    }
    return render(request,'root/index.html',context=context)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def port_folio(request,id):
    cat = Category.objects.all()
    portos = get_object_or_404(PortFolio,pk=id)
    porto = PortFolio.objects.filter(status = True)

    context = {
        'cat':cat,
        'portos':portos,
        'porto':porto,
    }
    return render(request,'root/portfolio-details.html',context=context)

