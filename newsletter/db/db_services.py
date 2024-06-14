import sqlite3
from pathlib import Path
from newsletter.schemas.inscrito import InscritoOUT


DB_PATH = Path(__file__).parent / 'inscritos.db'


def criar_db():
  try:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE newsletter (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nome TEXT,
      email TEXT
    )
    ''')
  except Exception as err:
    print(err)

def gravar_inscrito_db(nome: str, email: str):
  conn = sqlite3.connect(DB_PATH)
  cur = conn.cursor()
  cur.execute('''
  INSERT INTO newsletter (nome, email) VALUES(?, ?)
  ''', (nome, email))
  conn.commit()
  id = cur.lastrowid
  conn.close()
  return id

def get_inscritos_db():
  conn = sqlite3.connect(DB_PATH)
  cur = conn.cursor()
  cur.execute('''
  SELECT id, nome, email FROM newsletter
  ''')
  inscritos = []
  for row in cur.fetchall():
    inscritos.append(InscritoOUT(
      id    = row[0],
      nome  = row[1],
      email = row[2]
    ))
  
  return inscritos

def get_inscrito_db(id: int):
  conn = sqlite3.connect(DB_PATH)
  cur = conn.cursor()
  try:
    cur.execute('''SELECT id, nome, email FROM newsletter WHERE id = ?''', (id,))
    user_db = cur.fetchone()

    if not user_db:
      return {"message": "usuario não encontrado!"}
      
    user = InscritoOUT(
      id    = user_db[0],
      nome  = user_db[1],
      email = user_db[2]
    )
    return user
  except sqlite3.Error as err:
    print(err)
  finally:
    cur.close()
    conn.close()

def atualizar_inscrito_db(id: int, nome: str, email: str):
  conn = sqlite3.connect(DB_PATH)
  curr = conn.cursor()
  try:
    curr.execute('''SELECT * FROM newsletter WHERE id = ?''', (id,))
    user = curr.fetchone()

    if not user:
      return {"message": f"não há usuario cadastrado com este id = {id}"}
    curr.execute('''
    UPDATE newsletter
    SET nome = ?, email = ?
    WHERE id = ?
    ''', (nome, email, id,))
    conn.commit()
  except sqlite3.Error as err:
    return {"message": f'Houver um error, {err}'}
  finally:
    curr.close()
    conn.close()
    return get_inscrito_db(id)

def delete_inscrito_db(id):
  conn = sqlite3.connect(DB_PATH)
  curr = conn.cursor()
  try:
    curr.execute('''SELECT * FROM newsletter WHERE id = ?''', (id,))
    user = curr.fetchone()
    if not user:
      return {"message": "usuario não encontado"}
    
    curr.execute('''DELETE FROM newsletter WHERE id = ?''', (id,))
    conn.commit()
    return {"message": "usuario deletado com sucesso!"}
    
  except sqlite3.Error as err:
    return { "message": f'Houver um error ao deletar usuario, {err}'}
    
  finally:
    curr.close()
    conn.close()


if __name__ == "__main__":
  criar_db()