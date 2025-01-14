import graphene

from api_server.graphql import queries
from api_server.graphql.mutations import modify, remove, create
from api_server.auth import query as auth_query, mutation as auth_mutation 


class Query(
    auth_query.AuthQuery, 
    queries.PlayerQuery, 
    queries.MatchQuery, 
    queries.TeamQuery,
    queries.UserQuery, 
    queries.LeagueQuery,
    queries.MiscellaneousQuery
):
    pass


class Mutation(auth_mutation.AuthMutation, graphene.ObjectType):
    add_existing_player_to_match = create.AddExistingPlayerToMatch.Field()
    add_event_to_match = create.AddEventToMatch.Field()
    create_match = create.CreateMatch.Field()
    create_league =create.CreateLeague.Field()
    create_league_season = create.CreateLeagueSeason.Field()
    create_country = create.CreateCountry.Field()
    create_team = create.CreateTeam.Field()
    create_player = create.CreatePlayer.Field()

    remove_player_from_match = remove.RemovePlayerFromMatch.Field()
    remove_player = remove.RemovePlayer.Field()
    remove_match = remove.RemoveMatch.Field()
    remove_team = remove.RemoveTeam.Field()
    remove_player_from_team = remove.RemovePlayerFromTeam.Field()
    remove_event_from_match = remove.RemoveEventFromMatch.Field()

    modify_player_match_contribution = modify.ModifyPlayerMatchContribution.Field()
    modify_player = modify.ModifyPlayer.Field()
    modify_match = modify.ModifyMatch.Field()
    modify_team = modify.ModifyTeam.Field()
    modify_country = modify.ModifyCountry.Field()
    modify_league = modify.ModifyLeague.Field()
    modify_league_season = modify.ModifyLeagueSeason.Field()
    modify_event_from_match = modify.ModifyEventFromMatch.Field()


schema: graphene.Schema = graphene.Schema(query=Query, mutation=Mutation)