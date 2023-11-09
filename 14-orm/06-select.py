from tables import engine, user_table
from classes import User, Address

from sqlalchemy import insert, select
from sqlalchemy.orm import Session

with engine.begin() as conn:
    result = conn.execute(
        insert(user_table),
        [
            {"name": "spongebob", "fullname": "Spongebob Squarepants"},
            {"name": "sandy", "fullname": "Sandy Cheeks"},
            {"name": "patrick", "fullname": "Patrick Star"}
        ]
    )

stmt = select(user_table).where(user_table.c.name == 'spongebob')
print(stmt)

with engine.begin() as conn:
    for row in conn.execute(stmt):
        print(row)

stmt = select(User).where(User.name == "spongebob")
with Session(engine) as session, session.begin():
    for user in session.execute(stmt):
        print(user)

print(select(user_table))
print(select(user_table.c.name, user_table.c.fullname))

print(select(User))
print(select(User.name, User.fullname))

with Session(engine) as session:
    row = session.execute(select(User)).first()
    print(row)
    print(row[0])
    session.commit()

with Session(engine) as session:
    row = session.scalars(select(User)).first()
    print(row)
    session.commit()

with Session(engine) as session:
    row = session.execute(select(User.name, User.fullname)).first()
    print(row)
    session.commit()

select_stmt = select(User.id, User.name + "@aol.com")
insert_stmt = insert(Address).from_select(
    ["user_id", "email_address"], select_stmt
)
with Session(engine) as session, session.begin():
    session.execute(insert_stmt)
    session.commit()

with Session(engine) as session, session.begin():
    for row in session.execute(select(Address)):
        print(row)

with Session(engine) as session, session.begin():
    row = session.execute(select(User.name, Address).where(
        User.id == Address.user_id).order_by(Address.id)).all()
    print(row)
