from fakejira import schema
import graphene

from graphene_django.debug import DjangoDebug


class Query(
    schema.Query,
    graphene.ObjectType,
):
    debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query)