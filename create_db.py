import sqlite3

def create_db():
    con = sqlite3.connect(database="rms.db")
    cur = con.cursor()
    
    cur.execute("CREATE TABLE IF NOT EXISTS project(pid INTEGER PRIMARY KEY AUTOINCREMENT, name text, duration text, budget text, description text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT, empID text, name text, email text, gender text, dob text, contact text, joining text, project text, state text, city text, pin text, address text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS performance(rid INTEGER PRIMARY KEY AUTOINCREMENT, eid text, pname text, name text, communication text, productivity text, creativity text, integrity text, punctuality text, attendance text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS signup(suid INTEGER PRIMARY KEY AUTOINCREMENT, name text, lastname text, email text, dob text, secq text, secp text, password text,failed_attempts INTEGER DEFAULT 0,blocked INTEGER DEFAULT 0)")
    con.commit()
    
    con.close() 


create_db()
