from datetime import date

from django.db import models
from django.contrib.auth.models import User, Permission
from api_server.constants import Metrics, MatchEvents


class Country(models.Model):
    name: models.CharField = models.CharField(max_length=255, unique=True)
    flag_url: models.CharField = models.CharField(max_length=255, blank=True, null=True)


class League(models.Model):
    name: models.CharField = models.CharField(max_length=255, unique=True)
    country_of_origin: models.ForeignKey = models.ForeignKey(Country, models.PROTECT)
    logo_url: models.CharField = models.CharField(max_length=255, blank=True, null=True)


class LeagueSeason(models.Model):
    name: models.CharField = models.CharField(max_length=255)
    league: models.ForeignKey = models.ForeignKey(League, models.PROTECT)

    class Meta:
        unique_together: list[str] = ["name", "league"]


class Match(models.Model):
    game_date: models.DateField = models.DateField()
    league_season: models.ForeignKey = models.ForeignKey(LeagueSeason, models.PROTECT)

    def get_players(self) -> models.QuerySet["Player"]:
        """
        Returns all players that participate in match.
        """
        raise NotImplementedError

    def get_teams(self) -> models.QuerySet["Team"]:
        raise NotImplementedError

    def get_events(self) -> models.QuerySet["MatchEvent"]:
        raise NotImplementedError
    
    def get_result(self) -> dict["Team", int]:
        raise NotImplementedError
    
    def get_admin_actions(self) -> models.QuerySet["MatchAdminAction"]:
        raise NotImplementedError

    def calculate_metric(
        self, metric_type: Metrics, target_event: MatchEvents, metric_params: list[int]
    ) -> float:
        raise NotImplementedError


class AdminAction(models.Model):
    action_type: models.ForeignKey = models.ForeignKey(Permission, models.PROTECT)
    user: models.ForeignKey = models.ForeignKey(User, models.CASCADE)
    action_date: models.DateField = models.DateField()


class MatchAdminAction(models.Model):
    admin_action: models.OneToOneField = models.OneToOneField(AdminAction, models.CASCADE)
    match: models.ForeignKey = models.ForeignKey(Match, models.CASCADE)


class Player(models.Model):
    name: models.CharField = models.CharField(max_length=255)
    surname: models.CharField = models.CharField(max_length=255)
    nickname: models.CharField = models.CharField(max_length=255, blank=True, null=True)
    country_of_origin: models.ForeignKey = models.ForeignKey(Country, models.PROTECT)
    profile_photo_url: models.CharField = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together: list[str] = ["name", "surname"]

    def get_matches(self, start: date, end: date) -> models.QuerySet[Match]:
        raise NotImplementedError

    def get_teams(self, start: date, end: date) -> models.QuerySet["Team"]:
        raise NotImplementedError
    
    def get_admin_actions(self) -> models.QuerySet["PlayerAdminAction"]:
        raise NotImplementedError

    def calculate_metric(
        self, match_id: int, metric_type: Metrics, target_event: MatchEvents, metric_params: list[int]
    ) -> float:
        raise NotImplementedError


class PlayerAdminAction(models.Model):
    admin_action: models.OneToOneField = models.OneToOneField(AdminAction, models.CASCADE)
    player: models.ForeignKey = models.ForeignKey(Player, models.CASCADE)


class Team(models.Model):
    name: models.CharField = models.CharField(max_length=255, unique=True)
    country_of_origin: models.ForeignKey = models.ForeignKey(Country, models.PROTECT)
    logo_url: models.CharField = models.CharField(max_length=255, blank=True, null=True)

    def get_matches(self, start: date, end: date) -> models.QuerySet[Match]:
        raise NotImplementedError

    def get_players(self, start: date, end: date) -> models.QuerySet[Player]:
        raise NotImplementedError
    
    def get_admin_actions(self) -> models.QuerySet["TeamAdminAction"]:
        raise NotImplementedError

    def calculate_metric(
        self, match_id: int, metric_type: Metrics, target_event: MatchEvents, metric_params: list[int]
    ) -> float:
        raise NotImplementedError


class TeamAdminAction(models.Model):
    admin_action: models.OneToOneField = models.OneToOneField(AdminAction, models.CASCADE)
    team: models.ForeignKey = models.ForeignKey(Team, models.CASCADE)


class PlayerInMatch(models.Model):
    player: models.ForeignKey = models.ForeignKey(Player, models.CASCADE)
    match: models.ForeignKey = models.ForeignKey(Match, models.CASCADE)
    team: models.ForeignKey = models.ForeignKey(Team, models.CASCADE)
    minutes_played: models.FloatField = models.FloatField()


class EventType(models.Model):
    name: models.CharField = models.CharField(max_length=255)


class MatchEvent(models.Model):
    player: models.ForeignKey = models.ForeignKey(Player, models.CASCADE)
    match: models.ForeignKey = models.ForeignKey(Match, models.CASCADE)
    occurrence_minute: models.FloatField = models.FloatField()
    event_type: models.ForeignKey = models.ForeignKey(EventType, models.PROTECT)
