from koneksi import get_mysql

def create(id_keranjang,nama_menu,qty,catatan,created_at,updated_at):
    connection = get_mysql()
    mycursor = connection.cursor()
    sql = ("INSERT INTO keranjang (id_keranjang, nama_menu,qty,catatan, created_at, updated_at)" 
           "VALUES (%s,%s,%s,%s,%s,%s)")
    mycursor.execute(sql,(id_keranjang,nama_menu,qty,catatan,created_at,updated_at))
    connection.commit()
    connection.close()

def read():
    connection = get_mysql()
    cursor = connection.cursor()
    cursor.execute("SELECT * from keranjang")
    datas = cursor.fetchall()

    for data in datas:
        print("Data dari database: ", data)
    connection.close()
    return datas

def update(id_keranjang,nama_menu,qty,catatan,created_at,updated_at):
    connection = get_mysql()
    cursor = connection.cursor()
    sql = ("UPDATE keranjang SET nama_menu=%s, qty=%s, catatan=%s, created_at=%s, updated_at=%s"
           "WHERE id_keranjang=%s")
    cursor.execute(sql,(nama_menu,qty,catatan,created_at,updated_at,id_keranjang))
    connection.commit()
    connection.close()

def delete(id_keranjang):
    connection = get_mysql()
    cursor = connection.cursor()
    sql = "DELETE FROM keranjang WHERE id_keranjang= %s"
    cursor.execute(sql,id_keranjang)
    connection.commit()
    connection.close()



