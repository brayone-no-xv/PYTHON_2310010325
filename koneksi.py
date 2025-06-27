import pymysql
def get_mysql():
    return pymysql.connect(
        host = 'localhost',
        user = 'root',
        password= '',
        database= 'python_2310010325',
        cursorclass= pymysql.cursors.Cursor
    )