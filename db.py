import sqlite3

DATABASE = "empresa.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS abonados(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(255) NOT NULL,
                servicio_id INT NOT NULL,
                FOREIGN KEY (servicio_id) REFERENCES servicios(id)
            )
        """,
        """CREATE TABLE IF NOT EXISTS servicios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo VARCHAR(255) NOT NULL,
                precio INT NOT NULL
            )
        """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)

