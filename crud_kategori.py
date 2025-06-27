from koneksi import get_mysql

def create(id_kategori,jenis_kategori,created_at,updated_at):
    connection = get_mysql()
    cursor = connection.cursor()
    sql = ("INSERT INTO kategori (id_kategori, jenis_kategori, created_at, updated_at)" 
           "VALUES (%s,%s,%s,%s)")
    cursor.execute(sql,(id_kategori, jenis_kategori, created_at, updated_at))
    connection.commit()
    connection.close()

def read():
    connection = get_mysql()
    cursor = connection.cursor()
    cursor.execute("SELECT * from kategori")
    data = cursor.fetchall()
    print("Data dari database: ", data)
    connection.close()
    return data

def update(id_kategori,jenis_kategori,created_at,updated_at):
    connection = get_mysql()
    cursor = connection.cursor()
    sql = ("UPDATE kategori SET jenis_kategori=%s, created_at=%s, updated_at=%s"
           "WHERE id_kategori=%s")
    cursor.execute(sql,(jenis_kategori, created_at, updated_at,id_kategori))
    connection.commit()
    connection.close()

def delete(id_kategori):
    connection = get_mysql()
    cursor = connection.cursor()
    sql = "DELETE FROM kategori WHERE id_kategori= %s"
    cursor.execute(sql,id_kategori)
    connection.commit()
    connection.close()


