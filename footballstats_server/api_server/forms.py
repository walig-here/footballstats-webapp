from django import forms

from api_server.models import Team, League, LeagueSeason, Match, PlayerInMatch, Player, Country, MatchEvent


class ModifyEventForm(forms.Form):
    class Meta:
        model = MatchEvent
        fields = ("player", "occurrence_minute")

    event_id = forms.IntegerField(required=True)


class RemoveEventForm(forms.Form):
    event_id= forms.IntegerField(required=True)


class RemovePlayerFromTeam(forms.Form):
    player_id = forms.IntegerField(required=True)
    match_id = forms.IntegerField(required=True)


class ModifyLeagueSeasonForm(forms.ModelForm):
    class Meta:
        model = LeagueSeason
        fields = ("name", )

    league_season_id = forms.IntegerField(required=True)


class ModifyLeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = "__all__"

    league_id = forms.IntegerField(required=True)


class ModifyCountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"

    country_id = forms.IntegerField()


class RemoveTeamForm(forms.Form):
    team_id = forms.IntegerField(required=True)


class ModifyTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"

    team_id = forms.IntegerField(required=True)


class ModifyMatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = "__all__"

    match_id = forms.IntegerField(required=True)


class RemoveMatchForm(forms.Form):
    match_id = forms.IntegerField(required=True)


class ModifyPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = "__all__"

    player_id = forms.IntegerField(required=True)


class RemovePlayerFromMatchForm(forms.ModelForm):
    class Meta:
        model = PlayerInMatch
        fields = ("player", "match")


class RemovePlayerForm(forms.Form):
    player_id = forms.IntegerField(required=True)


class AddEventToMatchForm(forms.ModelForm):
    class Meta:
        model = MatchEvent
        fields = "__all__"


class CreateCountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"


class AddNewPlayerToMatchForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = "__all__"

    match_id = forms.IntegerField(required=True)
    team_id = forms.IntegerField(required=True)


class ModifyPlayerMatchContributionForm(forms.ModelForm):
    class Meta:
        model = PlayerInMatch
        fields = ("team", "minutes_played")

    match_id = forms.IntegerField(required=True)
    player_id = forms.IntegerField(required=True)


class AddExistingPlayerToMatchForm(forms.ModelForm):
    class Meta:
        model = PlayerInMatch
        fields = "__all__"


class CreateMatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = "__all__"

    home_score = forms.IntegerField(required=True)
    home_team_id = forms.IntegerField(required=True)
    away_score = forms.IntegerField(required=True)
    away_team_id = forms.IntegerField(required=True)


class CreateLeagueSeasonForm(forms.ModelForm):
    class Meta:
        model = LeagueSeason
        fields = "__all__"


class CreateLeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = "__all__"


class AddTeamToMatchForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"

    match_id = forms.IntegerField(required=True)