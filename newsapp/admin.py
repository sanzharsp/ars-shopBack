from django.contrib import admin

from .models import *

from .utils import html_tags_delete # кастомная функция для удаления html тегов

from django.contrib.auth.admin import UserAdmin

from captcha.models import CaptchaStore




class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('get_author','date_add')
    
    
    @admin.display(ordering='title', description='News')
    def get_author(self, obj):
        return html_tags_delete(obj.title)

class Last_News_Date_Admin(admin.ModelAdmin):
    list_display = ('last_news_date',)



class Author_Admin(UserAdmin):
    model = Author
    list_display = ('username', 'is_superuser','is_staff')
    list_filter = ('username', 'is_superuser', 'first_name','last_name')
    fieldsets = (
        ('Негізгі ақпарат', {'fields': ('username', 'password', 'first_name','last_name','surname','email',)}),
        ('Қол жеткізу құқықтары және растау', {'fields': ('is_staff','is_superuser')}),
        
    )
    add_fieldsets = (
        ('Негізгі ақпарат', {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name','last_name','surname','email',)},
            
        ),
         ('Қол жеткізу құқықтары және растау', {'fields': ('is_staff','is_superuser')}),
    )
    search_fields = ('username',)
    ordering = ('username',)


class CaptchaStoreAdmin(admin.ModelAdmin):
    CaptchaStore._meta.verbose_name ="captcha"
    CaptchaStore._meta.verbose_name_plural ="captcha"


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','ordered', 'ver_order', 'totalPrice')
    list_filter = ('ordered', 'ver_order', 'totalPrice')


# Register your models here.
admin.site.register(News)
admin.site.register(Order,OrderAdmin)
admin.site.register(Author,Author_Admin)
admin.site.register(last_News_date,Last_News_Date_Admin)
admin.site.register(CaptchaStore,CaptchaStoreAdmin)
admin.site.register(Category,CategoryAdmin)

admin.site.site_header="ARS-SHOP" # Шапка приложения

admin.site.site_title="ARS-SHOP" # Титулка приложения





