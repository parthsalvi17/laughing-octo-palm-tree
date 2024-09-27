from ariadne import QueryType, make_executable_schema, gql
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from service3.models import Order

type_defs = gql("""
    type Query {
        orders: [Order]
    }

    type Order {
        id: Int
        user_id: Int
        product_id: Int
        quantity: Int
    }
""")

query = QueryType()

engine = create_engine("postgresql://postgres:password@db:5432/mydatabase")
Session = sessionmaker(bind=engine)
session = Session()

@query.field("orders")
def resolve_orders(_, __):
    return session.query(Order).all()

schema = make_executable_schema(type_defs, query)
