from django.contrib import admin
from .models import UserProfileInfo, Country, Activity, Histry,WithdrawalHistry

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Country)
admin.site.register(Activity)
admin.site.register(Histry)
admin.site.register(WithdrawalHistry)
# admin.site.register(EWallet)

