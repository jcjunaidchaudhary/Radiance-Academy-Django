from django.contrib import admin
from home.models import Contact, Gallery, Notice, Pdf, Result,Stories
# Register your models here.
admin.site.register(Contact)
admin.site.register(Gallery)
admin.site.register(Stories)
admin.site.register(Pdf)
admin.site.register(Notice)
admin.site.register(Result)