import mysql.connector


def get_connection():
    return mysql.connector.connect(user='',
                                         password='',
                                         host='10.8.37.226',
                                         database='')


def sql_exec(connection, cmd):
    cursor = connection.cursor()
    cursor.execute(cmd)
    result = []

    for row in cursor:
        result.append(row)

    cursor.close()
    return result


def get_student_schedule(student_id):
    return sql_exec(connection, f"CALL get_student_schedule({student_id})")


connection = get_connection()

student_id = input("Enter student ID: ")
schedule = get_student_schedule(student_id)

pd = 0
for data in schedule:
    pd += 1
    print()
    print(f"Period: {pd}")
    print(f"Course: {data[0]}")
    print(f"Room: {data[1]}")
    print(f"Teacher: {data[2]} {data[3]}")

connection.close()
