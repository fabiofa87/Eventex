from django.contrib import admin
from django.utils.html import format_html

from eventex.core.models import Speaker, Contact, Talk


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1



class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'website_link', 'photo_img', 'description', "email", "phone")

    def website_link(self, obj):
        return format_html('<a href="{0}">{0}</a>', obj.website)

    website_link.short_description = 'website'

    def photo_img(self, obj):
        return format_html('<img width="32px" src="{}">', obj.photo)

    photo_img.short_description = 'foto'

    def email(self, obj):
        return obj.contact_set.emails().first()

    email.short_description = 'e-mail'

    def phone(self, obj):
        return obj.contact_set.phones().first()

    phone.short_description = 'telefone'


# Register your models here.
admin.site.register(Speaker, SpeakerModelAdmin)
admin.site.register(Talk)
