import mysql.connector as mysql

# Establish a connection to the database
conn = mysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='usiuclinic'
)

cursor = conn.cursor()


# To register patients
def user_login(tup):
        cursor.execute('SELECT * FROM `users` WHERE  `StaffID`=%s AND`FirstName`= %s AND `LastName`= %s AND `Position`= %s AND `Password`= %s', tup)
        return cursor.fetchone()

