from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm  import declarative_base


SQLALCHEMY_DATABASE_URL ='postgresql://aktanbro2010:1@localhost:5432/todo'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False,autoflush=False, bind=engine)

Base = declarative_base()