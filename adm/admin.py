from django.contrib import admin
from .models import currency
from .models import broker
from .models import broker_account
from .models import invest_date
from .models import entry_code
from .models import user_account
from .models import invest_plan
from .models import user_profile

class BrokerAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
class BrokerAccountAdmin(admin.ModelAdmin):
    list_display = ('broker','number','server','type','currency')
    list_filter = ['broker']
class InvestDateAdmin(admin.ModelAdmin):
    list_display = ('week','year')
    list_filter = ['week','year']
class InvestPlanAdmin(admin.ModelAdmin):
    list_display = ('invest_date','broker_account','balance_in','balance_out','open_pl','close_pl','dd')
    list_filter = ['invest_date','broker_account']

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('id','invest_date','user','code','text','amount','balance')
    list_filter = ['user','invest_date','code']

class EntryCodeAdmin(admin.ModelAdmin):
    list_display = ('id','text')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','referral','einlage','auszahlung','profit','balance','deposit','currency','invest_date','pay_date','days')

admin.site.register(currency)
admin.site.register(broker, BrokerAdmin)
admin.site.register(broker_account, BrokerAccountAdmin)
admin.site.register(invest_date, InvestDateAdmin)
admin.site.register(entry_code, EntryCodeAdmin)
admin.site.register(user_account, UserAccountAdmin)
admin.site.register(invest_plan, InvestPlanAdmin)
admin.site.register(user_profile, UserProfileAdmin)