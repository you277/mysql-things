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


def get_teacher_schedule(teacher_id):
    return sql_exec(connection, f"CALL get_teacher_schedule({teacher_id})")


def get_query():
    print("Are you a student or a teacher?")
    print("1. Student")
    print("2. Teacher")

    is_student = input("> ") == "1"
    user_type = "Student" if is_student else "Teacher"

    print()
    user_id = input(f"{user_type} ID: ")
    return is_student, user_id


def display_schedule(schedule, pd_display):
    periods = {}
    for pd in schedule:
        periods[pd[4]] = pd
    for i in range(10):
        period_num = i + 1
        pd_display(period_num, periods[period_num] if period_num in periods else None)


def display_student_schedule(pd_num, period):
    print()
    print(f"Period: {pd_num}")
    if period:
        print(f"Course: {period[0]}")
        print(f"Room: {period[1]}")
        print(f"Teacher: {period[2]} {period[3]}")
    else:
        print("(None)")


def display_teacher_schedule(pd_num, period):
    print()
    print(f"Period: {pd_num}")
    if period:
        print(f"Course: {period[0]}")
        print(f"Room: {period[1]}")
    else:
        print("(None)")


connection = get_connection()
is_student, user_id = get_query()

if is_student:
    schedule = get_student_schedule(user_id)
    display_schedule(schedule, display_student_schedule)
else:
    schedule = get_teacher_schedule(user_id)
    display_schedule(schedule, display_teacher_schedule)


connection.close()
