import sqlite3

connection = sqlite3.connect(":memory:")

# Step 3: Perform database operations
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE TB_STATUS (
        ID_STATUS INTEGER PRIMARY KEY AUTOINCREMENT,
        NOME_STATUS TEXT
    )
    """
)

# Create a table
cursor.execute(
    """CREATE TABLE TB_GERENCIAMENTO (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    DESCRICAO TEXT,
                    ID_STATUS INTEGER NOT NULL,
                    DATA DATETIME,
                    FOREIGN KEY (ID_STATUS) REFERENCES TB_STATUS (ID_STATUS)
                )"""
)

def insere_status(status):

    try:
        cursor.execute(
            "INSERT INTO TB_STATUS (NOME_STATUS) VALUES (?)", (status,)
        )
    
        return obtem_status_by_name(status=status)[0]
    except:
        raise


def obtem_todos_status():
    try:
        rows = cursor.execute(
            "SELECT * FROM TB_STATUS", ()
        ).fetchall()

        return rows
    except:
        raise


def obtem_status_by_name(status):
    try:
        rows = cursor.execute(
            "SELECT * FROM TB_STATUS WHERE NOME_STATUS = ?",
            (status,),
        ).fetchall()

        return rows
    except:
        raise
