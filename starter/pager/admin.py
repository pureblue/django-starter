from django.contrib import admin
from imagekit.admin import AdminThumbnail
from pager import models
# Register your models here.

class StaffImageAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'admin_thumbnail')
	admin_thumbnail = AdminThumbnail(image_field='thumbnail')

class PortfolioImageAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'admin_thumbnail')
	admin_thumbnail = AdminThumbnail(image_field='thumbnail')

class PagerBackgroundImageAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'admin_thumbnail')
	admin_thumbnail = AdminThumbnail(image_field='thumbnail')

class StaffCardAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("staff_first_name", "staff_last_name",)}

class PortfolioCardAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}

class PagerBlockAdmin(admin.ModelAdmin):
	list_display = ('title', 'order')
	list_editable = ('order',)
	prepopulated_fields = {"slug": ("title",)}

class PagerAdmin(admin.ModelAdmin):
	list_display = ('slug', 'content',)
	ordering = ('slug',)

class PagerSocialAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("service_name",)}

admin.site.register(models.StaffImage, StaffImageAdmin)
admin.site.register(models.StaffCard, StaffCardAdmin)
admin.site.register(models.PortfolioImage, PortfolioImageAdmin)
admin.site.register(models.PortfolioCard, PortfolioCardAdmin)
admin.site.register(models.PagerBackgroundImage, PagerBackgroundImageAdmin)
admin.site.register(models.PagerBlock, PagerBlockAdmin)
admin.site.register(models.Pager, PagerAdmin)
admin.site.register(models.PagerSocial, PagerSocialAdmin)