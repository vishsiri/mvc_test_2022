# generate rfid number to insert into database
import datetime
import random
import models.database as database
def generate_rfid():
    rfid = random.randint(1000000000, 9999999999)
    return rfid

def submit_feedback(name, surname, email, feedback):
    timestamp = datetime.datetime.now()
    rfid = generate_rfid()
    status = "Open"
    database.insert(timestamp, name, surname, email, feedback, rfid, status)


# Change status open,closed,escalated
def change_status(status, id):
    database.update_status(status, id)