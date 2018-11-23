from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import loader

from .models import Game, Rule, FAQ
from .forms import NameForm

# Create your views here.
# 
class IndexView(generic.ListView):
	template_name = 'therulz/index.html'
	context_object_name = 'game_list'

	def get_queryset(self):
		return Game.objects.order_by('game_name')[:]

def game(request, game_id):
	game = get_object_or_404(Game, pk=game_id)
	if (game):
		rule_list = game.rule_set.order_by('rule_order')[:]

	context = {
		'game': game,
		'rule_list': rule_list,
	}
	return render(request, 'therulz/game.html', context)

def about(request):
	faq_list = FAQ.objects.order_by('order')[:]

	context = {
		'faq_list': faq_list,
	}
	return render(request, 'therulz/about.html', context)

def search(request):
	query = request.GET['usr_query']
	game_list = Game.objects.filter(game_name__contains=query)
	rule_list = Rule.objects.filter(rule_name__contains=query)

	context = {
		'query': query,
		'game_list': game_list,
		'rule_list': rule_list,
	}
	return render(request, 'therulz/search_results.html', context)


