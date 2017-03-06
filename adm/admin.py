from django.contrib import admin
from .models import currency
from .models import broker
from .models import brokeraccount

admin.site.register(currency)
admin.site.register(broker)
admin.site.register(brokeraccount)
