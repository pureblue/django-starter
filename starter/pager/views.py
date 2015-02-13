from django.shortcuts import render
from django.views.generic import TemplateView
from . import models

# Template Views
class Pager(TemplateView):
	""" Pager template """
	template_name = "pager/base.html"

	def get_context_data(self, **kwargs):
		context = super(Pager, self).get_context_data(**kwargs)
		context['pager_blocks'] = models.PagerBlock.objects.all()
		context['portfolio_cards_list'] = models.PortfolioCard.objects.all()
		return context