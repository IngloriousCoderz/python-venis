from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, create_engine, text, insert, select

metadata_obj = MetaData()

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String)
)

print(user_table)
print(user_table.c)
print(user_table.c.keys())
print(user_table.c.name)  # user_account.name
print(user_table.primary_key)

address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", String, nullable=False)
)

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
# metadata_obj.create_all(engine)

with engine.begin() as conn:
    conn.execute(text("""\
        CREATE TABLE user_account (
        id INTEGER NOT NULL,
        name VARCHAR(30),
        fullname VARCHAR,
        password VARCHAR(30),
        PRIMARY KEY (id)
      )"""))

stmt = insert(user_table).values(
    name='antony', fullname='Matteo Antony Mistretta')
print(stmt)
print(stmt.params)
compiled = stmt.compile()
print(compiled)
print(compiled.params)

with engine.begin() as conn:
    conn.execute(stmt)

# with engine.begin() as conn:
#     conn.execute(text("""\
#                 INSERT INTO user_account (name, fullname)
#                 VALUES (:name, :fullname)
#                 """),
#                  {"name": "antony", "fullname": "Matteo Antony Mistretta"}
#                  )

stmt = select(user_table)
stmt.compile()
with engine.begin() as conn:
    result = conn.execute(stmt)
    for row in result:
        print(row)
