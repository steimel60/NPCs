import sqlite3 as sql

def create_table(connection: sql.Connection):
    with connection:
        c = connection.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS npc_settlement (
            nid INTEGER NOT NULL,
            sid INTEGER NOT NULL,
            CONSTRAINT PK_npc_settlement PRIMARY KEY (nid, sid),
            CONSTRAINT FK_npc_id FOREIGN KEY (nid)
                REFERENCES npcs (id)
            CONSTRAINT FK_s_id FOREIGN KEY (sid)
                REFERENCES settlements (id)
        )""")

def drop_table(connection: sql.Connection):
    with connection:
        c = connection.cursor()
        c.execute("DROP TABLE IF EXISTS npc_settlement")

def insert_npc_settlement(connection: sql.Connection, npc_id: str, stlm_id: int) -> bool:
    try:
        with connection:
            c = connection.cursor()
            c.execute("INSERT INTO npc_settlement VALUES (:npc_id, :stlm_id)"
            ,{'npc_id':npc_id, 'stlm_id':stlm_id})
            return True
    except Exception as e:
        print(e)
        return False

def get_hometown(connection: sql.Connection, npc_id: int) -> str:
    with connection:
        c = connection.cursor()
        c.execute("""SELECT s.name FROM settlements AS s
                    WHERE s.id IN (SELECT sid FROM npc_settlement WHERE nid =:npc_id)""",
                    {'npc_id':npc_id})
        return c.fetchone()[0]