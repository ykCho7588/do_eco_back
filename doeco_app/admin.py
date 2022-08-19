from django.contrib import admin
from .models import Ecospot, FreeComment, FreePost
# Register your models here.


admin.site.register(Ecospot)

admin.site.register(FreePost)
admin.site.register(FreeComment)

