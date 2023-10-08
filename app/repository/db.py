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

cursor.execute("INSERT INTO TB_STATUS(NOME_STATUS) VALUES ('CRIADO')")
cursor.execute("INSERT INTO TB_STATUS(NOME_STATUS) VALUES ('CONCLUIDO')")
cursor.execute("INSERT INTO TB_STATUS(NOME_STATUS) VALUES ('CANCELADO')")

# cursor.execute("INSERT INTO TB_GERENCIAMENTO(DESCRICAO, ID_STATUS, DATA) VALUES ('OI', 1, '01/01/2000')")
connection.commit()

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

def lista_status_por_id(id):
    try:
        rows = cursor.execute(
            "SELECT * FROM TB_STATUS WHERE ID_STATUS = ?",
            (id,),
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

def deleta_status_por_id(id):
    try:
        rows = cursor.execute(
            "DELETE FROM TB_STATUS WHERE ID_STATUS = ?",
            (id,),
        )
    except:
        raise


def obtem_todas_tarefas():
    try:
        rows = cursor.execute(
            """SELECT * FROM TB_GERENCIAMENTO G
                INNER JOIN TB_STATUS S
                ON G.ID_STATUS = S.ID_STATUS
            """, ()
        ).fetchall()

        return rows
    except:
        raise

def obtem_tarefa_por_id(id):
    try:
        rows = cursor.execute(
            """SELECT * FROM TB_GERENCIAMENTO G
                INNER JOIN TB_STATUS S
                ON G.ID_STATUS = S.ID_STATUS
                WHERE G.ID = ?
            """, (id,)
        ).fetchone()

        return rows
    except Exception as e:
        raise

def cria_tarefa(tarefa):
    try:
        cursor = connection.cursor()

        id_status = obtem_status_by_name("CRIADO")[0][0]

        cursor.execute(
            "INSERT INTO TB_GERENCIAMENTO (DESCRICAO, ID_STATUS, DATA) VALUES (?, ?, ?)", (tarefa.get("descricao"), id_status, tarefa.get("data"),)
        )
        id = cursor.lastrowid
        connection.commit()
        

        return obtem_tarefa_por_id(id=id)
    except Exception as e:
        raise


def deleta_tarefa_por_id(id):
    try:
        cursor.execute("DELETE FROM TB_GERENCIAMENTO WHERE ID = ?", (id,))
    except Exception as e:
        raise