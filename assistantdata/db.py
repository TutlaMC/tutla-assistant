import sqlite3
from datetime import datetime
from modules import Utils
# Create table (should be done once during setup)

def initialize_db():
    Utils.DBLogger.log("Initializing Database", style="execution")
    with sqlite3.connect('assistantdata/users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            user_id INT UNIQUE,
                            member BOOLEAN,
                            premium BOOLEAN,
                            banned BOOLEAN,
                            mod INTEGER,
                            aura INTEGER,
                            slowmode DATETIME,
                            last_command TEXT,
                            daily DATETIME,
                            xp INTEGER,
                            coins INTEGER)''')
        conn.commit()

initialize_db()

def add_user(user_id: int, member=False, premium=False, banned=False, mod=0, aura=1000, slowmode=None, last_command=" ",daily=None,xp=10,coins=0):
    if slowmode is None:
        slowmode = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if daily is None:
        daily = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    try: 
        if last_command == " ": last_command = getData(user_id, "last_command")
        with sqlite3.connect('assistantdata/users.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT OR REPLACE INTO users (user_id, member, premium, banned, mod, aura, slowmode, last_command, daily, xp, coins)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )''',
                        (user_id, member, premium, banned, mod, aura, slowmode, last_command,daily,xp,coins))
            conn.commit()
        Utils.DBLogger.log("Added user", style="success")
    except Exception as e:
        Utils.DBLogger.log(e, style="error")
        

def edit_user(user_id: int, **kwargs):
    try:
        with sqlite3.connect('assistantdata/users.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM users WHERE user_id = ?', (user_id,))
            exists = cursor.fetchone()[0] > 0
            
            if exists:
                update_parts = []
                params = []
                
                for column, value in kwargs.items():
                    if value is not None:
                        update_parts.append(f"{column} = ?")
                        params.append(value)
                
                if update_parts:
                    update_query = f"UPDATE users SET {', '.join(update_parts)} WHERE user_id = ?"
                    params.append(user_id)
                    cursor.execute(update_query, params)
                    conn.commit()

                else:
                    Utils.DBLogger.log("No fields to update in edit_user",style="warning")
            else:
                add_user(user_id, **kwargs)
        if Utils.dev_mode: Utils.DBLogger.log("Sucessfully edited user", style="sucess")
    except Exception as e:
        Utils.DBLogger.log(e, style="error")
def userExists(user_id):
    connection = sqlite3.connect('assistantdata/users.db')
    cursor = connection.cursor()
    query = "SELECT COUNT(*) FROM users WHERE user_id = ?"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result[0] > 0
def add_coins(user_id,coins):
    if userExists(user_id):
        if getData(user_id,"coins") != None:
            edit_user(user_id,coins=getData(user_id,"coins")+coins)
        else: edit_user(user_id,coins=coins)
    else: add_user(user_id)
def getData(user_id: int, column_name: str):
    with sqlite3.connect('assistantdata/users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('PRAGMA table_info(users)')
        columns = [row[1] for row in cursor.fetchall()]
        
        if column_name not in columns:
            raise ValueError(f"Invalid column name: {column_name}")
        
        cursor.execute(f'SELECT {column_name} FROM users WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()
        
        return result[0] if result else None

def printDB():
    conn = sqlite3.connect("assistantdata/users.db")
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
    connection = sqlite3.connect('assistantdata/users.db')
    cursor = connection.cursor()
    
    query = f"SELECT user_id, {look} FROM users"
    cursor.execute(query)
    rows = cursor.fetchall()
    
    result = {row[0]: row[1] for row in rows}
    
    connection.close()
    return result
def add_column_to_table():
    connection = sqlite3.connect('assistantdata/users.db')
    cursor = connection.cursor()
    
    # Define the SQL statement to add a new column
    sql = "ALTER TABLE users ADD COLUMN coins INTEGER"
    
    # Execute the SQL statement
    cursor.execute(sql)
    
    # Commit the changes and close the connection
    connection.commit()
    cursor.close()
    connection.close()
