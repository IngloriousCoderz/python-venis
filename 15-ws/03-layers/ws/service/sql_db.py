from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select
from ..model.task import Base, Task
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(model_class=Base)


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


def create_tasks():
    Base.metadata.create_all(engine)


Session = sessionmaker(engine)

# with engine.begin() as conn:
#     conn.execute(
#         text("CREATE TABLE tasks (id INT, text VARCHAR, completed BOOL)"))


def read_tasks():
    with Session.begin() as session:
        return session.execute(select(Task))
