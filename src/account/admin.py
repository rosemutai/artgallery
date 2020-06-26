from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account,Profile

# Register your models here.

class AccountAdmin(UserAdmin):
  """docstring for AccountAdmin"""
  list_display      = ('email', 'username','date_joined','last_login','is_admin','is_staff')
  search_fields     = ('email', 'username')
  readonly_fields   = ('date_joined','last_login')
  filter_horizontal = ()
  list_filter       = ()
  fieldsets         = ()


class ProfileAdmim(admin.ModelAdmin):
  list_display  = ('full_name','profile_image','date_created','bio')
  search_fields = ('full_name',)
  filter_horizontal =()
  list_filter = ()
  fieldsets =()
admin.site.register(Account, AccountAdmin)
admin.site.register(Profile,ProfileAdmim)

