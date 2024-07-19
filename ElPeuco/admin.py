from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import usuarioRegistrado
from .forms import FormularioRegistrousuarioRegistrado

class usuarioRegistradoAdmin(UserAdmin):
    add_form = FormularioRegistrousuarioRegistrado
    model = usuarioRegistrado
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('email', 'is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone', 'birth_date', 'address', 'postal_code')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'phone', 'birth_date', 'address', 'postal_code', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(usuarioRegistrado, usuarioRegistradoAdmin)