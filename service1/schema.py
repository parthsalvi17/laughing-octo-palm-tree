from ariadne import QueryType, make_executable_schema, gql
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from service1.models import User

type_defs = gql("""
    type Query {
        users: [User]
    }

    type User {
        id: Int
        name: String
        email: String
    }
""")

query = QueryType()

engine = create_engine("postgresql://postgres:password@db:5432/mydatabase")
Session = sessionmaker(bind=engine)
session = Session()

@query.field("users")
def resolve_users(_, __):
    return session.query(User).all()

schema = make_executable_schema(type_defs, query)
