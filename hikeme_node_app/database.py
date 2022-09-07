import re
import sqlite3

def connectToDB():
    db = sqlite3.connect("hikeme_database.sqlite3")
    cur = db.cursor()
    return db, cur


def getUserLoginDetails(cur, username):
    query = f"SELECT username, password, is_superuser, id FROM auth_user WHERE username='{username}';"
    cur.execute(query)
    result = cur.fetchall()
    grabbedUsername, grabbedPassword, grabbedSuperuserStatus, grabbedID = result[[0][0]]
    return grabbedUsername, grabbedPassword, grabbedSuperuserStatus, grabbedID


def getUserDetails(cur, grabbedID):
    query = f"SELECT first_name, last_name, contact_number, emergency_contact_number, address, current_status_id, current_trail_checkpoint_id FROM hikeme_app_person WHERE auth_user_id='{grabbedID}';"
    cur.execute(query)
    result = cur.fetchall()
    grabbedFirstName, grabbedLastName, grabbedContactNumber, grabbedEmergencyContactNumber, grabbedAddress, grabbedCurrentStatusID, grabbedCurrentTrailCheckpointID = result[[0][0]]

    return grabbedFirstName, grabbedLastName, grabbedContactNumber, grabbedEmergencyContactNumber, grabbedAddress, grabbedCurrentStatusID, grabbedCurrentTrailCheckpointID


def getTrailDetails(cur):
    query = f"SELECT * FROM hikeme_app_trail;"
    cur.execute(query)
    result = cur.fetchall()
    return result[[0][0]]


def getTrailCheckpointDetails(cur):
    query = f"SELECT * FROM hikeme_app_trail_checkpoints;"
    cur.execute(query)
    result = cur.fetchall()
    return result[[0][0]]


def getNumPersonID(cur, n):
    query = f"SELECT id FROM hikeme_app_person ORDER BY id LIMIT '{n}';"
    cur.execute(query)
    result = cur.fetchall()
    return result