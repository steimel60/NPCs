import sqlite3 as sql

def create_table(connection: sql.Connection):
    with connection:
        c = connection.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS npc_race (
            nid INTEGER NOT NULL,
            rid INTEGER NOT NULL,
            CONSTRAINT PK_npc_race PRIMARY KEY (nid, rid),
            CONSTRAINT FK_npc_id FORIEGN KEY (nid)
                REFERENCES npcs (id)
            CONSTRAINT FK_race_id FORIEGN KEY (rid)
                REFERENCES races (id)
        )""")

def drop_table(connection: sql.Connection):
    with connection:
        c = connection.cursor()
        c.execute("DROP TABLE IF EXISTS npc_race")

def insert_npc_race(connection: sql.Connection, npc_id: str, race_id: int) -> bool:
    try:
        with connection:
            c = connection.cursor()
            c.execute("INSERT INTO npc_race VALUES (:npc_id, :race_id)"
            ,{'npc_id':npc_id, 'race_id':race_id})
            return True
    except Exception as e:
        print(e)
        return False
