import sqlite3

def connectToDB():
    db = sqlite3.connect("hikeme_database.sqlite3")
    cur = db.cursor()
    return db, cur


def getUserLoginDetails(cur, username):
    query = f"SELECT username, password, is_superuser, id from auth_user WHERE username='{username}';"
    cur.execute(query)
    result = cur.fetchall()
    grabbedUsername, grabbedPassword, grabbedSuperuserStatus, grabbedID = result[[0][0]]
    return grabbedUsername, grabbedPassword, grabbedSuperuserStatus, grabbedID


def getUserDetails(cur, grabbedID):
    query = f"SELECT first_name, last_name, contact_number, emergency_contact_number, address, current_status_id, current_trail_checkpoint_id from hikeme_app_person WHERE auth_user_id='{grabbedID}';"
    cur.execute(query)
    result = cur.fetchall()
    grabbedFirstName, grabbedLastName, grabbedContactNumber, grabbedEmergencyContactNumber, grabbedAddress, grabbedCurrentStatusID, grabbedCurrentTrailCheckpointID = result[[0][0]]

    return grabbedFirstName, grabbedLastName, grabbedContactNumber, grabbedEmergencyContactNumber, grabbedAddress, grabbedCurrentStatusID, grabbedCurrentTrailCheckpointID


def getTrailDetails(cur):
    query = f"SELECT * from hikeme_app_trail;"
    cur.execute(query)
    result = cur.fetchall()
    print(result)



def getTrailCheckpointDetails(cur):
    query = f"SELECT * from hikeme_app_trail_checkpoints;"
    cur.execute(query)
    result = cur.fetchall()
    for i in result:
        print(i[1])



class Trail:
    def __init__(self, id, trailName):
        self.trailID = id
        self.trailName = trailName
        self.checkpoints = []

    def addCheckpoint(self, checkpointID):
        self.checkpoints.append(checkpointID)

class TrailCheckpoint:
    def __init__(self, id, checkpointName, trailID):
        self.trailCheckpointID = id
        self.checkpointName = checkpointName
        self.trailID = trailID