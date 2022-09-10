import sqlite3
import random
import utils

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



def insertWarning(selectedCheckpoints, grabbedUserIDsLength, warningFile):
    randCheckpointID = int(len(selectedCheckpoints) * random.random())
    randPersonID = int(grabbedUserIDsLength * random.random())
    randWarningRating = int(5 * random.random())
    randWarning = random.choice(warningFile)

    with sqlite3.connect("hikeme_database.sqlite3") as conn:
        cur = conn.cursor()
        query = f"INSERT INTO hikeme_app_warning (warning, warning_rating, trail_checkpoint_id, person_id) VALUES ('{randWarning}', '{randWarningRating}', '{selectedCheckpoints[randCheckpointID]}', '{randPersonID}');"
        cur.execute(query)
        conn.commit()



def insertCheckIn(selectedCheckpoints, grabbedUserIDsLength):
    # randStatus = int(3 * random.random()) CHANGE TO RANDOM SELECTION FROM TEXT FILE AND ADD IT TO DB AND SET THE ID OF ADDED STATUS TO PERSON
    randCheckpointID = int(len(selectedCheckpoints) * random.random())
    randPersonID = int(grabbedUserIDsLength * random.random())

    with sqlite3.connect("hikeme_database.sqlite3") as conn:
        cur = conn.cursor()
        query = f"UPDATE hikeme_app_person SET (current_status_id = '{randStatusID}', current_trail_checkpoint_id = '{selectedCheckpoints[randCheckpointID]}') WHERE person_id = '{randPersonID};"
        cur.execute(query)
        conn.commit()
