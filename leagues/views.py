from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"Baseball":League.objects.filter(sport='Baseball'),
		"Womens" : League.objects.filter(name__contains='Womens') ,
		"Hockey" :League.objects.filter(name__contains='Hockey')|League.objects.filter(sport__contains='Hockey') ,
		"NoFootball" :League.objects.exclude(sport='Football') ,
		"Conference" :League.objects.filter(name__contains='Conference') ,
		"Atlantic": League.objects.filter(name__contains='Atlantic') ,
		"Dallas":Team.objects.filter(location__contains='Dallas')	,
		"Raptors": Team.objects.filter(team_name__contains='Raptors') ,
		"City" :Team.objects.filter(location__contains='City') ,
		"NameT":Team.objects.filter(team_name__startswith='T') ,
		"Locations":Team.objects.order_by('location') ,
		"Inverso": Team.objects.order_by('-team_name') ,
		"Cooper": Player.objects.filter(last_name='Cooper') ,
		"Joshua" : Player.objects.filter(first_name='Joshua') ,
		"Cooper2" : Player.objects.filter(last_name='Cooper').exclude(first_name='Joshua') ,
		"Alexander"	: Player.objects.filter(first_name='Alexander')|Player.objects.filter(first_name='Wyatt') ,
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")