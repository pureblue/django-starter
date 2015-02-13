from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [

    url(regex=r'^$',
		view=views.Pager.as_view(),
		name='single-pager',
	),
]
