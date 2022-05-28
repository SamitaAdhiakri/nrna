from django.contrib import admin
from .models import NewUser,About,Slider, Event, Project, News,Partner, AboutTiles, Team, Contact,  Upcomming_Event, Testomonial,Gallery,Comment

from django.contrib.auth.admin import UserAdmin
from django.forms import PasswordInput, TextInput, Textarea


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email',  'first_name',)
    list_filter = ('email',  'username','first_name', 'address',
                   'country', 'year_in_school', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'username', 'first_name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name',
         'address', 'country', 'year_in_school')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about','avatar')}),
    )
    formfield_overrides = {
        NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
        NewUser.password:{'widget':PasswordInput(attrs={'class': 'form-control'})}
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',  'first_name', 'password1', 'password2', 'address', 'country', 'year_in_school','avatar' ,'is_active', 'is_staff')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)
admin.site.register(Slider)
admin.site.register(About)
admin.site.register(Event)
admin.site.register(Project)
admin.site.register(News)
admin.site.register(AboutTiles)
admin.site.register(Partner)
admin.site.register(Team)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Upcomming_Event)
admin.site.register(Testomonial)
admin.site.register(Gallery)
