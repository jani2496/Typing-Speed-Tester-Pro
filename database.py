import sqlite3
from datetime import datetime


DATABASE_NAME = "typing_results.db"



def create_database():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        date TEXT,

        wpm REAL,

        accuracy REAL,

        errors INTEGER,

        time_taken REAL,

        difficulty TEXT

    )
    """)


    connection.commit()
    connection.close()



def save_result(
    wpm,
    accuracy,
    errors,
    time_taken,
    difficulty
):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()


    cursor.execute("""
    INSERT INTO results
    (date,wpm,accuracy,errors,time_taken,difficulty)

    VALUES (?,?,?,?,?,?)

    """,

    (

        datetime.now().strftime("%d-%m-%Y %H:%M"),

        wpm,

        accuracy,

        errors,

        time_taken,

        difficulty

    ))


    connection.commit()

    connection.close()



def get_results():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()


    cursor.execute(
        "SELECT * FROM results"
    )


    results = cursor.fetchall()


    connection.close()


    return results