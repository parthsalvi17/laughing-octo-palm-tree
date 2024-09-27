from ariadne import QueryType, make_executable_schema, gql
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from service2.models import Product

type_defs = gql("""
    type Query {
        products: [Product]
    }

    type Product {
        id: Int
        name: String
        price: Float
    }
""")

query = QueryType()

engine = create_engine("postgresql://postgres:password@db:5432/mydatabase")
Session = sessionmaker(bind=engine)
session = Session()

@query.field("products")
def resolve_products(_, __):
    return session.query(Product).all()

schema = make_executable_schema(type_defs, query)
