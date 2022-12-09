from sqlalchemy import text, create_engine

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

# with engine.connect() as conn:
#     result = conn.execute(text("CREATE TABLE some_table (x int, y int)"))
#     print(result)
#     print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
#
#     result = conn.execute(text("SELECT x, y FROM some_table WHERE y > :y"), {"y": 3})
#     print(result)
#     print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
#
#     result = conn.execute(text("SELECT * FROM some_table ORDER BY y"))
#     print(result)
#     print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
#
#     result = conn.execute(text("UPDATE some_table SET x=:x WHERE y=:y"), [{"x": 1, "y": 2}, {"x": 3, "y": 4}],)
#     print(result)



