from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Comments)

admin.site.register(Replay)