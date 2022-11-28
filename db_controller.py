from db import get_db

def insert_abonado(nombre, servicio_id):
    db = get_db()
    cur = db.cursor()
    statement = "INSERT INTO abonados(nombre, servicio_id) VALUES (?, ?)"
    cur.execute(statement, [nombre, servicio_id])
    db.commit()
    return True

def insert_servicio(tipo, precio):
    db = get_db()
    cur = db.cursor()
    statement = "INSERT INTO servicios(tipo, precio) VALUES (?, ?)"
    cur.execute(statement, [tipo, precio])
    db.commit()
    return True

def update_abonado(id, nombre, servicio_id):
    db = get_db()
    cur = db.cursor()
    statement = "UPDATE abonados SET nombre = ?, servicio_id = ? WHERE id = ?"
    cur.execute(statement, [nombre, servicio_id, id])
    db.commit()
    return True

def update_servicio(id, tipo, precio):
    db = get_db()
    cur = db.cursor()
    statement = "UPDATE servicios SET tipo = ?, precio = ? WHERE id = ?"
    cur.execute(statement, [tipo, precio, id])
    db.commit()
    return True

def delete_abonado(id):
    db = get_db()
    cur = db.cursor()
    statement = "DELETE FROM abonados WHERE id = ?"
    cur.execute(statement, [id])
    db.commit()
    return True

def delete_servicio(id):
    db = get_db()
    cur = db.cursor()
    statement = "DELETE FROM servicios WHERE id = ?"
    cur.execute(statement, [id])
    db.commit()
    return True

def get_abonado_by_id(id):
    db = get_db()
    cur = db.cursor()
    statement = "SELECT * FROM abonados WHERE id = ?"
    cur.execute(statement, [id])
    return cur.fetchone()

def get_servicio_by_id(id):
    db = get_db()
    cur = db.cursor()
    statement = "SELECT * FROM servicios WHERE id = ?"
    cur.execute(statement, [id])
    return cur.fetchone()

def get_abonados():
    db = get_db()
    cur = db.cursor()
    query = "SELECT * FROM abonados"
    cur.execute(query)
    return cur.fetchall()

def get_servicios():
    db = get_db()
    cur = db.cursor()
    query = "SELECT * FROM servicios"
    cur.execute(query)
    return cur.fetchall()