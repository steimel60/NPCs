import sqlite3 as sql, os
import npcs, settlements as stlm
from relations import npc_settlement

def world_exists(world_name: str) -> bool:
    db_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Worlds')),f"{world_name}.world")
    if not os.path.exists(db_path):
        print(f"No world {world_name} found!\nCheck path {db_path}")
        return False
    else:
        print(f"{world_name} found!")
        return True

def connect_to_world(world_name: str) -> sql.Connection:
    world_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..','Worlds')),f"{world_name}.world")
    if not os.path.exists(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..','Worlds'))):
        os.mkdir(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..','Worlds')))
    conn = sql.connect(world_path)
    return conn

def create_all_tables(connection: sql.Connection, make_npcs = True, make_stlm = True, make_hometowns = True):
    if make_npcs: npcs.create_table(connection)
    if make_stlm: stlm.create_table(connection)
    if make_hometowns: npc_settlement.create_table(connection)

def drop_all_tables(connection: sql.Connection, drop_npcs = True, drop_stlm = True, drop_hometowns = True):
    if drop_hometowns: npc_settlement.drop_table(connection)
    if drop_npcs: npcs.drop_table(connection)
    if drop_stlm: stlm.drop_table(connection)
    
