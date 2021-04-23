from django.contrib import admin
from .models import Babysitter, Group, Activity, Sitting, Baby

admin.site.register(Babysitter)
admin.site.register(Group)
admin.site.register(Activity)
admin.site.register(Sitting)
admin.site.register(Baby)

