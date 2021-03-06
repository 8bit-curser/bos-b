from graphene import ObjectType, Schema

from creator.schemas import Mutation as MCreator, Query as QCreator


class Query(QCreator, ObjectType):
    pass


class Mutation(MCreator, ObjectType):
    pass


schema = Schema(query=Query, mutation=Mutation)
