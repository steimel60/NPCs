import sqlite3 as sql

def create_table(connection: sql.Connection):
    with connection:
        c = connection.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS settlements (
            id INTEGER NOT NULL PRIMARY KEY,
            name TEXT NOT NULL,
            pop INTEGER NOT NULL
        )""")

def drop_table(connection: sql.Connection):
    with connection:
        c = connection.cursor()
        c.execute("DROP TABLE IF EXISTS settlements")

def insert_settlement(connection: sql.Connection, name: str, pop: int) -> bool:
    try:
        with connection:
            c = connection.cursor()
            c.execute("SELECT COUNT(id) FROM settlements")
            id = c.fetchone()[0]
            c.execute("INSERT INTO settlements VALUES (:id, :name, :pop)"
            ,{'id':id, 'name':name, 'pop':pop})
            return True
    except Exception as e:
        print(e)
        return False