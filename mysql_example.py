import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'university'

config = {
  'user': 'root',
  'password': 'Cic1234*',
  'host': '127.0.0.1',
  'raise_on_warnings': True
}

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8mb4'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor(buffered=True)

try:
    cnx.database = DB_NAME
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

def create_table(TABLES):
    for name, ddl in TABLES.iteritems():
        try:
            print("Creating table {}: ".format(name))
            cursor.execute(ddl)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

def generate_tables():

    TABLES = {}
    TABLES['department'] = (
        "CREATE TABLE department ("
        "  dept_name varchar(100) NOT NULL,"
        "  building varchar(100) NOT NULL,"
        "  budget decimal(12,2) NOT NULL,"
        "  PRIMARY KEY (dept_name)"
        ") ENGINE=InnoDB")
    create_table(TABLES)

    TABLES = {}
    TABLES['student'] = (
        "CREATE TABLE student ("
        "  ID varchar(10) NOT NULL,"
        "  name varchar(100) NOT NULL,"
        "  dept_name varchar(100) NOT NULL,"
        "  tot_cred decimal(3,2) NOT NULL,"
        "  PRIMARY KEY (ID),"
        "  CONSTRAINT fk_student FOREIGN KEY (dept_name) REFERENCES department (dept_name)"
        ") ENGINE=InnoDB")
    create_table(TABLES)

    TABLES = {}
    TABLES['instructor'] = (
        "CREATE TABLE instructor ("
        "  ID varchar(10) NOT NULL,"
        "  name varchar(100) NOT NULL,"
        "  dept_name varchar(100) NOT NULL,"
        "  salary decimal(8,2) NOT NULL,"
        "  PRIMARY KEY (ID),"
        "  CONSTRAINT fk_instructor FOREIGN KEY (dept_name) REFERENCES department (dept_name)"
        ") ENGINE=InnoDB")
    create_table(TABLES)

    TABLES = {}
    TABLES['course'] = (
        "CREATE TABLE course ("
        "  course_id varchar(10) NOT NULL,"
        "  title varchar(100) NOT NULL,"
        "  dept_name varchar(20) NOT NULL,"
        "  credits decimal(2,0) NOT NULL,"
        "  PRIMARY KEY (course_id),"
        "  CONSTRAINT fk_course FOREIGN KEY (dept_name) REFERENCES department (dept_name)"
        ") ENGINE=InnoDB")
    create_table(TABLES)

    TABLES = {}
    TABLES['advisor'] = (
        "CREATE TABLE advisor ("
        "  s_ID varchar(10) NOT NULL,"
        "  i_ID varchar(10) NOT NULL,"
        "  CONSTRAINT fk1_advisor FOREIGN KEY (i_ID) REFERENCES instructor (ID),"
        "  CONSTRAINT fk2_advisor FOREIGN KEY (s_ID) REFERENCES student (ID)"
        ") ENGINE=InnoDB")
    create_table(TABLES)

def insert_rows(data_department, add_department):
    for row in range(0,len(data_department)):
        cursor.execute(add_department,data_department[row])
    cnx.commit()

def insert_table():
    add_department = ("INSERT INTO department (dept_name, building, budget) VALUES (%(dept_name)s, %(building)s, %(budget)s)")
    data_department = [
        {
            'dept_name' : 'Mathematics',
            'building' : '1021',
            'budget' : '50000.00'
        },
        {
            'dept_name' : 'Physics',
            'building' : '1022',
            'budget' : '30000.00'
        },
        {
            'dept_name' : 'Software',
            'building' : '1023',
            'budget' : '100000.00'
        }
    ]
    insert_rows(data_department, add_department)

    add_student = (
        "INSERT INTO student (id, name, dept_name, tot_cred) VALUES (%(id)s, %(name)s, %(dept_name)s, %(tot_cred)s)")
    data_student = [
        {
            'id': 1,
            'name': 'Miguel Angel Chavez Ramirez',
            'dept_name': 'Mathematics',
            'tot_cred': 4
        },
        {
            'id': 2,
            'name': 'Juan Perez Perez',
            'dept_name': 'Physics',
            'tot_cred': 5
        },
        {
            'id': 3,
            'name': 'Karla Diaz Diaz',
            'dept_name': 'Software',
            'tot_cred': 6
        }
    ]
    insert_rows(data_student, add_student)

    add_instructor = (
        "INSERT INTO instructor (id, name, dept_name, salary) VALUES (%(id)s, %(name)s, %(dept_name)s, %(salary)s)")
    data_instructor = [
        {
            'id': 1,
            'name': 'Christopher Robin',
            'dept_name': 'Mathematics',
            'salary': 24000.00
        },
        {
            'id': 2,
            'name': 'Bob Esponja Square Pants',
            'dept_name': 'Physics',
            'salary': 26000.00
        },
        {
            'id': 3,
            'name': 'Juanito Escarcha salvo la navidad',
            'dept_name': 'Software',
            'salary': 30000.00
        }
    ]
    insert_rows(data_instructor, add_instructor)

    add_course = (
        "INSERT INTO course (course_id, title, dept_name, credits) VALUES (%(course_id)s, %(title)s, %(dept_name)s, %(credits)s)")
    data_course = [
        {
            'course_id': 'MA0001',
            'title': 'Modern Algebra',
            'dept_name': 'Mathematics',
            'credits': 50
        },
        {
            'course_id': 'PH0001',
            'title': 'Introduction to Physics',
            'dept_name': 'Physics',
            'credits': 60
        },
        {
            'course_id': 'SW0001',
            'title': 'Oriented Object Programming',
            'dept_name': 'Software',
            'credits': 40
        }
    ]
    insert_rows(data_course, add_course)

    add_advisor = (
        "INSERT INTO advisor (s_ID, i_ID) VALUES (%(s_ID)s, %(i_ID)s)")
    data_advisor = [
        {
            's_ID': 1,
            'i_ID': 2
        },
        {
            's_ID': 2,
            'i_ID': 3
        },
        {
            's_ID': 3,
            'i_ID': 1
        }
    ]
    insert_rows(data_advisor, add_advisor)

def executeQuery():
    print
    query = ("SELECT * from course")
    cursor.execute(query)
    for row in cursor:
        print(row)

    print
    query = ("SELECT * from student")
    cursor.execute(query)
    for row in cursor:
        print(row)

    print
    query = ("SELECT * from advisor")
    cursor.execute(query)
    for row in cursor:
        print(row)

    print
    query = ("SELECT * from instructor")
    cursor.execute(query)
    for row in cursor:
        print(row)

    print
    query = ("SELECT * from department")
    cursor.execute(query)
    for row in cursor:
        print(row)

generate_tables()
insert_table()
executeQuery()
cursor.close()
cnx.close()

# update_creditos = ("UPDATE alumnos SET Creditos = %s WHERE alumno_id = %s")
# nuevo_credito={
#     'Creditos' : 10,
#     'alumno_id' : 1
# }
# cursor.execute(update_creditos,(nuevo_credito['Creditos'],nuevo_credito['alumno_id']))
# cnx.commit()
# query = ("SELECT * from alumnos where alumno_id=1")
# cursor.execute(query)
# for row in cursor:
#     print(row)
