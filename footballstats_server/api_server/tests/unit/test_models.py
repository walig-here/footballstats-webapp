from django.test import TestCase


class TestDatabaseContains5MatchesAnd2Admins(TestCase):
    fixtures = ["initial_data"]


class TestMatchWhenDatabaseContains0Matches(TestCase):
    ...