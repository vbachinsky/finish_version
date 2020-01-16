from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic.edit import UpdateView, FormView

YOUR_BLOCK = None
YOUR_KICK = None
GAME_OVER = None
YOU_WIN = None


class WarriorsSelect(FormView):
	model = Fight
	form_class = WarriorsSelectForm
	template_name = 'fight/select_warrior.html'
	success_url = '/fight/battle/'

	def form_valid(self, form):
		global YOUR_KICK
		global YOUR_BLOCK
		global GAME_OVER
		global YOU_WIN
		YOUR_BLOCK = None
		YOUR_KICK = None
		GAME_OVER = None
		YOU_WIN = None
		instance = super().form_valid(form)
		Fight.objects.all().delete()
		protagonist = Fight.objects.create(name='protagonist')
		protagonist.description = form.cleaned_data.get('description')
		protagonist.set_warrior()
		antagonist = Fight.objects.create(name='antagonist')
		antagonist.description = random.choice(('strong', 'healthy', 'skill'))
		antagonist.set_warrior()
		return instance


class FightView(FormView):
	model = Fight
	form_class = FightForm
	template_name = 'fight/select_kick_and_block.html'
	success_url = '/fight/battle/'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['protagonist'] = Fight.objects.get(name='protagonist')
		context['antagonist'] = Fight.objects.get(name='antagonist')
		context['your_block'] = YOUR_BLOCK
		context['your_kick'] = YOUR_KICK
		context['game_over'] = GAME_OVER
		context['you_win'] = YOU_WIN
		return context

	def form_valid(self, form):
		instance = super().form_valid(form)
		global YOUR_KICK
		global YOUR_BLOCK
		global GAME_OVER
		global YOU_WIN
		protagonist = Fight.objects.get(name='protagonist')
		antagonist = Fight.objects.get(name='antagonist')
		protagonist.kick = form.cleaned_data.get('kick')
		protagonist.block = form.cleaned_data.get('block')
		antagonist.kick = random.choice(('head', 'body', 'foot'))
		antagonist.block = random.choice(('head', 'body', 'foot'))
		if protagonist.kick != antagonist.block:
			antagonist.health = antagonist.health - protagonist.get_damage()
			YOUR_KICK = True
		else:
			YOUR_KICK = False
		print(YOUR_KICK)
		if protagonist.block != antagonist.kick:
			protagonist.health = protagonist.health - antagonist.get_damage()
			YOUR_BLOCK = True
		else:
			YOUR_BLOCK = False
		if protagonist.health <= 0:
			GAME_OVER = True
			YOU_WIN = False
		if antagonist.health <= 0:
			GAME_OVER = True
			YOU_WIN = True
		print(YOUR_BLOCK)
		protagonist.save()
		antagonist.save()
		return instance
