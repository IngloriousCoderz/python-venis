from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

engine = create_engine('sqlite+pysqlite:///:memory:', echo=True)

with engine.begin() as conn:
    conn.execute(text("CREATE TABLE points (x int, y int)"))
    conn.execute(text("INSERT INTO points (x, y) VALUES (:x, :y)"), [
        {'x': 1, 'y': 1},
        {'x': 2, 'y': 4},
        {'x': 6, 'y': 8},
        {'x': 9, 'y': 10},
        {'x': 11, 'y': 12},
        {'x': 13, 'y': 14}
    ])


def print_points():
    stmt = text("SELECT x, y FROM points WHERE y > :y ORDER BY x, y")
    with Session(engine) as session:
        result = session.execute(stmt, {"y": 8})
        for row in result:
            print(f"x: {row.x}, y: {row.y}")
        session.commit()


print_points()

with Session(engine) as session:
    result = session.execute(text("UPDATE points SET y=:y WHERE x=:x"), [
        {"x": 9, "y": 11},
        {"x": 13, "y": 15}
    ])
    session.commit()

print_points()
