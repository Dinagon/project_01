import sqlite3

#создание таблицы Students
# connection = sqlite3.connect('teachers.db')
# cursor = connection.cursor()
# query = """CREATE TABLE Students (
# Student_Id INTEGER NOT NULL,
# Student_Name TEXT NOT NULL,
# School_Id INTEGER NOT NULL PRIMARY KEY);"""
# cursor.execute(query)
# connection.commit()
# connection.close()

# наполнение таблицы Students
# connection = sqlite3.connect('teachers.db')
# cursor = connection.cursor()
# query = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
# VALUES
# ('201','Иван', '1'),
# ('202', 'Петр', '2'),
# ('203', 'Анастасия', '3'),
# ('204', 'Игорь', '4');"""
# cursor.execute(query)
# connection.commit()
# connection.close()


# вывести данные о школе и студенте, используя ID студента (через JOIN)

def get_connection():
    connection = sqlite3.connect('teachers.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def get_student(student_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT Students.Student_Id, Students.Student_Name, School.School_Id, School.School_Name FROM Students JOIN School ON Students.School_Id = School.School_Id Where Students.Student_Id = ?;"
        cursor.execute(query,(student_id,))
        records = cursor.fetchall()
        for row in records:
            print ("ID студента:", row[0])
            print ("Имя студента:", row[1])
            print ("ID школы:", row[2])
            print ("Название школы:", row[3])
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print('Ошибка в получении данных', error)   

get_student(202)

# вывести данные о школе и студенте, используя ID школы (через JOIN)
# def get_connection():
#     connection = sqlite3.connect('teachers.db')
#     return connection

# def close_connection(connection):
#     if connection:
#         connection.close()

# def get_student(school_id):
#     try:
#         connection = get_connection()
#         cursor = connection.cursor()
#         query = "SELECT Students.School_Id, Students.Student_Name, School.School_Id, School.School_Name FROM Students JOIN School ON Students.School_Id = School.School_Id Where Students.School_Id = ?;"
#         cursor.execute(query,(school_id,))
#         records = cursor.fetchall()
#         for row in records:
#             print ("ID студента:", row[0])
#             print ("Имя студента:", row[1])
#             print ("ID школы:", row[2])
#             print ("Название школы:", row[3])
#         close_connection(connection)
#     except (Exception, sqlite3.Error) as error:
#         print('Ошибка в получении данных', error)   

# get_student(3)

