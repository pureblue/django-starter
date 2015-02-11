from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(regex=r'^$',
        view=TemplateView.as_view(template_name='pager/base.html'),
        name='single-pager'
    )
]
