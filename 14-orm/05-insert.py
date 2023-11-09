from tables import engine, user_table, address_table
from classes import User
from sqlalchemy import insert, select


stmt = insert(user_table).values(
    name="spongebob", fullname="Spongebob Squarepants")

with engine.begin() as conn:
    result = conn.execute(stmt)

print(result.inserted_primary_key)

print(insert(user_table))

with engine.begin() as conn:
    result = conn.execute(insert(user_table).return_defaults(), [
        {"name": "sandy", "fullname": "Sandy Cheeks"},
        {"name": "patrick", "fullname": "Patrick Star"}
    ])

print(result.inserted_primary_key_rows)


print(insert(user_table))
print(insert(user_table).values())
print(insert(user_table).values().compile(engine))

insert_stmt = insert(address_table).returning(
    address_table.c.id, user_table.c.name + "@aol.com")
print(insert_stmt)

select_stmt = select(user_table.c.id, user_table.c.name + "@aol.com")
print(select_stmt)

insert_stmt = insert(address_table).from_select(
    ["user_id", "email_address"], select_stmt)
print(insert_stmt)

print(insert(User))
print(insert(User).values())
print(insert(User).values().compile(engine))
