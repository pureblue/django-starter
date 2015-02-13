from django.db import models
from django.contrib.sites.models import Site
from django.core.cache import cache
from django.utils import translation
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import SmartResize, ResizeToFit, Transpose

# Create your models here.
class StaffImage(models.Model):
	name = models.CharField(max_length=100, help_text="Name your image")
	image = ProcessedImageField(upload_to='staff_image', processors=[Transpose(),SmartResize(640, 640)], format='JPEG', options={'quality':40})
	display_image = ImageSpecField(source='image', processors=[Transpose(),SmartResize(320, 320)], format='JPEG', options={'quality':40})
	thumbnail = ImageSpecField(source='image', processors=[Transpose(),SmartResize(100, 100)], format='JPEG', options={'quality':40})

	class Meta:
		verbose_name = 'Staff Image'
		verbose_name_plural = 'Staff Images'

	def __str__(self):
		return self.name

class StaffCard(models.Model):
	staff_first_name = models.CharField(max_length=200)
	staff_last_name = models.CharField(max_length=200)
	slug = models.CharField(max_length=50)
	staff_short_bio = models.TextField(blank=True)
	staff_image = models.ForeignKey(StaffImage, blank=True, null=True)
	email = models.EmailField(blank=True)
	phone = models.CharField(max_length=15, blank=True)
	order = models.IntegerField(default="0")

	class Meta:
		ordering = ['order']
		verbose_name = 'Staff Card'
		verbose_name_plural = 'Staff Cards'

	def __str__(self):
		return self.staff_last_name

class PortfolioImage(models.Model):
	name = models.CharField(max_length=100, help_text="Name your image")
	image = ProcessedImageField(upload_to='portfolio_image', processors=[Transpose(),SmartResize(640, 640)], format='JPEG', options={'quality':40})
	background_display_image = ImageSpecField(source='image', processors=[Transpose(),SmartResize(1200, 900)], format='JPEG', options={'quality':40})
	display_image = ImageSpecField(source='image', processors=[Transpose(),SmartResize(320, 200)], format='JPEG', options={'quality':40})
	thumbnail = ImageSpecField(source='image', processors=[Transpose(),SmartResize(100, 100)], format='JPEG', options={'quality':40})

	class Meta:
		verbose_name = 'Portfolio Image'
		verbose_name_plural = 'Portfolio Images'

	def __str__(self):
		return self.name

class PortfolioCard(models.Model):
	title = models.CharField(max_length=200)
	slug = models.CharField(max_length=50)
	content = models.TextField(blank=True)
	portfolio_image = models.ForeignKey(PortfolioImage, blank=True, null=True)
	order = models.IntegerField(default="0")
	client = models.CharField(max_length=200, blank=True)
	client_website = models.URLField(blank=True)
	project_date = models.CharField(blank=True, max_length=50)
	service = models.CharField(blank=True, max_length=50)

	class Meta:
		ordering = ['order']
		verbose_name = 'Portfolio Card'
		verbose_name_plural = 'Portfolio Cards'

	def __str__(self):
		return self.title

class PagerBackgroundImage(models.Model):
	name = models.CharField(max_length=100, help_text="Name your image")
	image = ProcessedImageField(upload_to='background_image', processors=[Transpose(),SmartResize(640, 640)], format='JPEG', options={'quality':40})
	background_display_image = ImageSpecField(source='image', processors=[Transpose(),SmartResize(1200, 900)], format='JPEG', options={'quality':40})
	thumbnail = ImageSpecField(source='image', processors=[Transpose(),SmartResize(100, 100)], format='JPEG', options={'quality':40})

	class Meta:
		verbose_name = 'Background Image'
		verbose_name_plural = 'Background Images'

	def __str__(self):
		return self.name

class PagerBlock(models.Model):
	title = models.CharField(max_length=200)
	slug = models.CharField(max_length=50)
	content = models.TextField(blank=True)
	pager_background_image = models.ForeignKey(PagerBackgroundImage, blank=True, null=True)
	background_color = models.CharField(max_length=6, blank=True)
	portfolio_cards = models.ManyToManyField(PortfolioCard, blank=True, null=True, help_text="If this is a portfolio section, what portfolio cards do you want to include?")
	staff_cards = models.ManyToManyField(StaffCard, blank=True, null=True, help_text="If this is a staff section, what staff cards do you want to include?")
	in_nav = models.BooleanField(default=True)
	order = models.IntegerField(default="0")

	class Meta:
		ordering = ['order']
		verbose_name = 'Pager Block'
		verbose_name_plural = 'Page Blocks'

	def __str__(self):
		return self.title


class Pager(models.Model):
    slug = models.SlugField(max_length=255, unique=True,
                            help_text='The name by which the template author '
                                      'retrieves this content.')
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'Pager content'

    def __unicode__(self):
        return self.slug

    def save(self):
        super(Pager, self).save()
        cache.delete(self.key_from_slug(self.slug))

    def delete(self):
        cache.delete(self.key_from_slug(self.slug))
        super(Pager, self).delete()

    # Helper method to get key for caching
    def key_from_slug(slug, site_id=None):
        lang = translation.get_language()
        return 'pager_%s_%s' % (slug, lang)
    key_from_slug = staticmethod(key_from_slug)

    # Class method with caching
    def get(cls, slug):
        """
        Checks if key is in cache, otherwise performs database lookup and
        inserts into cache.
        """
        key = cls.key_from_slug(slug)
        cache_value = cache.get(key)
        if cache_value:
            return cache_value

        try:
            fc = cls.objects.get(slug=slug)
        except cls.DoesNotExist:
            try:
                # Fallback to the non-site specific flatcontent
                key = cls.key_from_slug(slug)
                cache_value = cache.get(key)
                if cache_value:
                    return cache_value
                fc = cls.objects.get(slug=slug)
            except:
                return ''
        cache.set(key, fc.content)
        return fc.content
    get = classmethod(get)
