from django.shortcuts import render
from root.models import Category


def posts(request):
    cat = Category.objects.all()
    context = {
        'cat': cat,
    }

    return render(request,'blog/blog.html',context=context)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def posts_detail(request):
    return render(request,'blog/blog-details.html')

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@