import sqlalchemy
from sqlalchemy import create_engine, text

print(sqlalchemy.__version__)

engine = create_engine('sqlite+pysqlite:///:memory:', echo=True)

with engine.connect() as conn:
    result = conn.execute(text("SELECT 'hello world'"))
    print(result.all())

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE points (x int, y int)"))
    conn.execute(text("INSERT INTO points (x, y) VALUES (:x, :y)"), [
        {'x': 1, 'y': 1}, {'x': 2, 'y': 4}
    ])
    conn.commit()

with engine.begin() as conn:
    conn.execute(text("INSERT INTO points (x, y) VALUES (:x, :y)"), [
        {'x': 6, 'y': 8}, {'x': 9, 'y': 10}
    ])

with engine.begin() as conn:
    result = conn.execute(text("SELECT x, y FROM points"))
    for x, y in result:
        print(f"x: {x}, y: {y}")
    # for row in result:
    #     print(f"x: {row[0]}, y: {row[1]}")
    # for dict_row in result.mappings():
    #     print(f"x: {dict_row['x']}, y: {dict_row['y']}")

with engine.begin() as conn:
    result = conn.execute(
        text("SELECT x, y FROM points WHERE y > :y"), {"y": 4})
    for row in result:
        print(f"x: {row.x}, y: {row.y}")
