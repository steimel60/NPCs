import sqlite3 as sql

def create_table(connection: sql.Connection):
    with connection:
        c = connection.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS npcs (
            id INTEGER NOT NULL PRIMARY KEY,
            name TEXT NOT NULL,
            race TEXT NOT NULL,
            level INTEGER NOT NULL
        )""")

def drop_table(connection: sql.Connection):
    with connection:
        c = connection.cursor()
        c.execute("DROP TABLE IF EXISTS npcs")

def insert_npc(connection: sql.Connection, name: str, race: str, level: int) -> bool:
    try:
        with connection:
            c = connection.cursor()
            c.execute("SELECT COUNT(id) FROM npcs")
            id = c.fetchone()[0]
            c.execute("INSERT INTO npcs VALUES (:id, :name, :race, :level)"
            ,{'id':id, 'name':name, 'race':race, 'level':level})
            return True
    except Exception as e:
        print(e)
        return False

def select_by_id(connection: sql.Connection, id: int):
    with connection:
        c = connection.cursor()
        c.execute("""SELECT name FROM npcs WHERE id =:id""",
                    {'id':id})
        return c.fetchone()[0]
