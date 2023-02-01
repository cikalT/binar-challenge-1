import sqlite3

def insert_text_to_db(text):
    conn = sqlite3.connect("databases/pure.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS clean_text (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT)""")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clean_text (text) VALUES (?)", (text,))
    conn.commit()
    conn.close()

def insert_to_db_from_csv(frame):
    conn = sqlite3.connect("databases/pure.db")
    frame.to_sql('clean_text', conn, if_exist='replace', index=False)