from django.contrib import admin
from .models import Tags,Category,News


from django.utils.safestring import mark_safe


admin.site.register(Tags)
admin.site.register(Category)
# admin.site.register(News)



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk','name', 'views', 'category',  'is_active','is_banner','is_weekly','get_image')
    list_display_links = ('pk','name',)
    list_editable = ('category','is_active','is_banner','is_weekly')


    def get_image(self,news):
        if news.image:
            return mark_safe(f'<img src="{news.image.url}" width ="75">')
        else:
            return mark_safe(f'<img src="https://demofree.sirv.com/nope-not-here.jpg" width ="75">')
    get_image.short_description = 'Rasmi'

    prepopulated_fields = {"slug":("name",)}