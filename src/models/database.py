import mysql.connector
from mysql.connector import errorcode
def connect():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="mvc"
        )
        return mydb
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

# input name,surname,email,feedback


def insert(timestamp, name, surname, email, feedback, rfid, status):
    mydb = connect()
    mycursor = mydb.cursor()
    sql = "INSERT INTO feedback (timestamp, name, surname, email, feedback, rfid, status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (timestamp, name, surname, email, feedback, rfid, status)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()

# get all feedbacks


def get_all_feedbacks():
    mydb = connect()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM feedback")
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult

# get feedback by status


def get_feedback_by_status(status):
    mydb = connect()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM feedback WHERE status = %s"
    val = (status,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult

# Status Open, Close, Escalated


def update_status(status, id):
    mydb = connect()
    mycursor = mydb.cursor()
    sql = "UPDATE feedback SET status = %s WHERE id = %s"
    val = (status, id)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()

# get feedback by timestamp


def get_feedback_by_timestamp(timestamp):
    mydb = connect()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM feedback WHERE timestamp = %s"
    val = (timestamp,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult

# get feedback by email


def get_feedback_by_email(email):
    mydb = connect()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM feedback WHERE email = %s"
    val = (email,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult

# get all data from feedback
def get_all_data():
    mydb = connect()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM feedback")
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult

print(connect())
