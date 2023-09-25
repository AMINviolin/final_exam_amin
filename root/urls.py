from django.urls import path
from .views import *

app_name = 'root'

urlpatterns = [
    path("",home,name="home"),
    path("portfolio/<int:id>",port_folio,name="portfolio"),
    path('category/<int:category_id>',home,name='portfilter'),

]