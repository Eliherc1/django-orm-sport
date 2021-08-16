from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

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

def index2(request):
	context = {
		"Atlantic": Team.objects.filter(league__name__contains='Atlantic Soccer Conference') ,
		"Boston" : Player.objects.filter(curr_team__team_name='Penguins',curr_team__location='Boston') ,
		"Inter" :Player.objects.filter(curr_team__league__name='International Collegiate Baseball Conference') ,
		"Amateur": Player.objects.filter(curr_team__league__name='American Conference of Amateur Football',last_name='Lopez') ,
		"Football": Player.objects.filter(curr_team__league__sport='Football') ,
		"Sophia" :Team.objects.filter(curr_players__first_name='Sophia') ,
		"Sophia2": League.objects.filter(teams__curr_players__first_name='Sophia'),
		"Flores":Player.objects.filter(last_name='Flores').exclude(curr_team__location='Washington',curr_team__team_name='Roughriders') ,
		"Samuel": Team.objects.filter(all_players__first_name='Samuel',all_players__last_name='Evans') ,
		"Manitoba":Player.objects.filter(all_teams__team_name='Tiger-Cats',all_teams__location='Manitoba') ,
		"Vikings": Player.objects.filter(all_teams__team_name='Vikings',all_teams__location='Wichita').exclude(curr_team__team_name='Vikings',curr_team__location='Wichita') ,
		"Jacob": Team.objects.filter(all_players__first_name='Jacob',all_players__last_name='Gray').exclude(location='Oregon',team_name='Colts') ,
		"Joshua": Player.objects.filter(first_name='Joshua', all_teams__league__name='Atlantic Federation of Amateur Baseball Players') ,
		"Doce" : Team.objects.annotate(players=Count('all_players')).filter(players__gt=11) ,
		"Ultimo":Player.objects.annotate(eqp=Count('all_teams')).order_by('-eqp')
	}
	return render(request, "leagues/index2.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")