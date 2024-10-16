import sqlite3
from datetime import datetime
from modules import Utils
# Will be used soon!

def initialize_db():
    Utils.DBLogger.log("Initializing Database", style="execution")
    with sqlite3.connect('data/servers.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS servers (
                            server_id INT UNIQUE,
                            welcome INT,
                            leave INT,
                            warnlog INT,
                            logging INT)''')
        conn.commit()

initialize_db()

def add_server(server_id: int, welcome=0, leave=0, warnlog=0, logging=0):
    
    try: 
        with sqlite3.connect('data/servers.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT OR REPLACE INTO servers (server_id, welcome, leave, warnlog, logging)
                            VALUES (?, ?, ?, ?, ?)''',
                        (server_id, welcome, leave, warnlog, logging))
            conn.commit()
        Utils.DBLogger.log("Added server", style="success")
    except Exception as e:
        Utils.DBLogger.log(e, style="error")
        

def edit_server(server_id: int, **kwargs):
    try:
        with sqlite3.connect('data/servers.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM servers WHERE server_id = ?', (server_id,))
            exists = cursor.fetchone()[0] > 0
            
            if exists:
                update_parts = []
                params = []
                
                for column, value in kwargs.items():
                    if value is not None:
                        update_parts.append(f"{column} = ?")
                        params.append(value)
                
                if update_parts:
                    update_query = f"UPDATE servers SET {', '.join(update_parts)} WHERE server_id = ?"
                    params.append(server_id)
                    cursor.execute(update_query, params)
                    conn.commit()

                else:
                    Utils.DBLogger.log("No fields to update in edit_server",style="warning")
            else:
                add_server(server_id, **kwargs)
        if Utils.dev_mode: Utils.DBLogger.log("Sucessfully edited server", style="sucess")
    except Exception as e:
        Utils.DBLogger.log(e, style="error")
def serverExists(server_id):
    connection = sqlite3.connect('data/servers.db')
    cursor = connection.cursor()
    query = "SELECT COUNT(*) FROM servers WHERE server_id = ?"
    cursor.execute(query, (server_id,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result[0] > 0

def getData(server_id: int, column_name: str):
    with sqlite3.connect('data/servers.db') as conn:
        cursor = conn.cursor()
        cursor.execute('PRAGMA table_info(servers)')
        columns = [row[1] for row in cursor.fetchall()]
        
        if column_name not in columns:
            raise ValueError(f"Invalid column name: {column_name}")
        
        cursor.execute(f'SELECT {column_name} FROM servers WHERE server_id = ?', (server_id,))
        result = cursor.fetchone()
        
        return result[0] if result else None

def printDB():
    conn = sqlite3.connect("data/servers.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    final="==========================\n"
    for table_name in tables:
        table_name = table_name[0]
        final += f"Table: {table_name}\n"

        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        
        column_names = [description[0] for description in cursor.description]
        final+=f"Columns: {', '.join(column_names)}\n"

        for row in rows:
            final+=str(row)+"\n"
        
        final +="\n"
    final+="==========================\n"
    conn.close()
    return final


def get_column_data(look):
    connection = sqlite3.connect('data/servers.db')
    cursor = connection.cursor()
    
    query = f"SELECT server_id, {look} FROM servers"
    cursor.execute(query)
    rows = cursor.fetchall()
    
    result = {row[0]: row[1] for row in rows}
    
    connection.close()
    return result
def add_column_to_table():
    connection = sqlite3.connect('data/servers.db')
    cursor = connection.cursor()
    
    # Define the SQL statement to add a new column
    sql = "ALTER TABLE servers ADD COLUMN coins INTEGER"
    
    # Execute the SQL statement
    cursor.execute(sql)
    
    # Commit the changes and close the connection
    connection.commit()
    cursor.close()
    connection.close()
