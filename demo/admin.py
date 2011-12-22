from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from .forms import RequiredFormSet, AlwaysChangedModelForm

class MInline(admin.TabularInline): # StackedInline
    model = M
    can_delete = False
    max_num = 1
    formset = RequiredFormSet
    form = AlwaysChangedModelForm


class CustomUserAdmin(UserAdmin):
    list_display = ('f', 'f')
    list_filter = ('f', )
    search_fields = ('f', )
    filter_horizontal = ('f', )
    readonly_fields = ('f', )
    fieldsets = (
        (_('Name'), {
            'classes': ('collapse',), 
            'fields': (('f', 'f'), 'f',)
        }),
    )
    add_fieldsets = (
        ("Name", {
            'classes': ('collapse open',),
            'fields': ( ('f', 'f'), 'f')
        }),
    )
    add_form = UserCreationForm
    inlines = [MInline] # enable it if you need to set Organization or Privacy
    
    class Media:
        css = {
            "all": ("x.css",)
        }
    
    def get_readonly_fields(self, request, obj=None):
        pass
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        pass
    
    def get_form(self, request, obj=None, **kwargs):
        pass
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def queryset(self, request):
        qs = super(CustomUserAdmin, self).queryset(request)
        return qs
    
    def save_model(self, request, obj, form, change):
        obj.save()

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
