import sqlite3 as sql, os


def connect_to_world(world_name: str) -> sql.Connection:
    world_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Worlds')),f"{world_name}.world")
    if not os.path.exists(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Worlds'))):
        os.mkdir(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Worlds')))
    conn = sql.connect(world_path)
    return conn

def create_npcs_table(connection: sql.Connection):
    with connection:
        c = connection.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS npcs (
            id INTEGER NOT NULL PRIMARY KEY,
            name TEXT NOT NULL,
            race TEXT NOT NULL,
            level INTEGER NOT NULL
        )""")

def create_settlements_table(connection: sql.Connection):
    with connection:
        c = connection.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS settlements (
            s_id INTEGER NOT NULL PRIMARY KEY,
            s_name TEXT NOT NULL,
            s_pop INTEGER NOT NULL
        )""")

def create_all_tables(connection: sql.Connection, make_npcs = True, make_stlm = True):
    if make_npcs: create_npcs_table(connection)
    if make_stlm: create_settlements_table(connection)

def drop_npcs_table(connection: sql.Connection):
    with connection:
        c = connection.cursor()
        c.execute("DROP TABLE IF EXISTS npcs")

def drop_settlements_table(connection: sql.Connection):
    with connection:
        c = connection.cursor()
        c.execute("DROP TABLE IF EXISTS settlements")

def drop_all_tables(connection: sql.Connection, drop_npcs = True, drop_stlm = True):
    if drop_npcs: drop_npcs_table(connection)
    if drop_stlm: drop_settlements_table(connection)

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

def insert_settlement(connection: sql.Connection, name: str, pop: int) -> bool:
    try:
        with connection:
            c = connection.cursor()
            c.execute("SELECT COUNT(s_id) FROM settlements")
            id = c.fetchone()[0]
            c.execute("INSERT INTO settlements VALUES (:id, :name, :pop)"
            ,{'id':id, 'name':name, 'pop':pop})
            return True
    except Exception as e:
        print(e)
        return False

def world_exists(world_name: str) -> bool:
    db_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Worlds')),f"{world_name}.world")
    if not os.path.exists(db_path):
        print(f"No world {world_name} found!\nCheck path {db_path}")
        return False
    else:
        print(f"{world_name} found!")
        return True

if __name__ == "__main__":
    world_name = "Osaunu"
    
    world_exists(world_name)
    world_conn = connect_to_world(world_name)
    
    drop_all_tables(world_conn)
    create_all_tables(world_conn)
    insert_npc(world_conn, "Dyffros", "Human", 6)
    insert_npc(world_conn, "Entei", "Hafling", 6)
    insert_npc(world_conn, "Orlyn", "Aasmir", 6)
    insert_npc(world_conn, "Wrax", "Dragonborn", 6)
    insert_settlement(world_conn, "Kapros", 25000)
    insert_settlement(world_conn, "Obron", 15000)
    
    print("Done")