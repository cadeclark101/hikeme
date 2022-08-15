import sqlite3

def connectToDB():
    db = sqlite3.connect("hikeme_database.sqlite3")
    cur = db.cursor()
    return db, cur

def getUserDetails(db, cur, username):
    query = f"SELECT username, password, is_superuser, id from auth_user WHERE username='{username}';"
    cur.execute(query)
    result = cur.fetchall()
    grabbedUsername, grabbedPassword, grabbedSuperuserStatus, grabbedID = result[[0][0]]
    return grabbedUsername, grabbedPassword, grabbedSuperuserStatus, grabbedID
        
