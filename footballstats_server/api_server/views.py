import graphene

from api_server.graphql.query import Query
from api_server.graphql.mutation import Mutation


schema: graphene.Schema = graphene.Schema(query=Query, mutation=Mutation)