from django.shortcuts import render,redirect, get_object_or_404
from .models import Services,Category,PortFolio,Team,Pricing
from .forms import ContactUsForm
from django.contrib import messages
from blogs.models import Post


def home(request,category_id = None):
    service = Services.objects.filter(status = True)
    team = Team.objects.all()
    price = Pricing.objects.all()
    cat = Category.objects.all()
    if category_id:
        selected_category = get_object_or_404(Category,pk =category_id)
        porto = PortFolio.objects.filter(category = selected_category,status=True)
    else:
        porto = PortFolio.objects.filter(status = True)


    port_count = PortFolio.objects.filter(status = True).count()
    post_count = Post.objects.filter(status = True).count()
    last_three_posts = Post.objects.filter(status = True)[:3]

    context = {
        'service': service,
        'cat': cat,
        'three_post':last_three_posts,
        'porto': porto,
        'team':team,
        'price':price,
        'rc':port_count,
        'sc':post_count,
        'selected_category':int(category_id) if category_id else None,
    }
    return render(request,'root/index.html',context=context)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def port_folio(request,id):
    cat = Category.objects.all()
    porto = PortFolio.objects.filter(id=id,status = True)
            

    context = {
        'cat':cat,
        'porto':porto,

    }
    return render(request,'root/portfolio-details.html',context=context)
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def contact(request):
    if request.method == 'GET':
        cat = Category.objects.all()
        context = {'cat': cat}
        return render(request,"root/contact.html",context=context)
    elif request.method == 'POST' and len(request.POST) > 2:
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your message sent and we will answer to it soon')
            return redirect('root:contact')
        else:
            messages.add_message(request,messages.ERROR,'invalid input data')
            return redirect('root:contact')
        
def info(req):
    return  render(req, 'root/site.html')