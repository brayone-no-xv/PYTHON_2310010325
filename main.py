import ast
import datetime
import sys

from crud_kategori import *
# Mengimport library PyQt5
from PyQt5 import uic
from PyQt5.QtGui import *
# from PyQt5.uic import *
from PyQt5.QtWidgets import *
# from PyQt5.uic.Compiler.qtproxies import QtWidgets
from datetime import *

class FormKategori(QMainWindow):
    def __init__(self):
        super(FormKategori, self).__init__()
        uic.loadUi('formKategori.ui', self)

        # Inisialisasi model untuk QTableView
        self.model = QStandardItemModel(0, 4)  # 0 baris awal, 4 kolom
        self.model.setHorizontalHeaderLabels(['ID Kategori', 'Jenis Kategori', 'Created At', 'Updated At'])

        # Set model ke QTableView
        self.tb_output.setModel(self.model)

        self.btnTambah.clicked.connect(self.tambah_teks)
        self.btnUbah.clicked.connect(self.ubah_teks)
        self.btnHapus.clicked.connect(self.hapus_teks)
        self.btnRead.clicked.connect(self.baca_teks)
        self.btnClear.clicked.connect(self.bersih_teks)

    def tambah_teks(self):
        try:
            id_kategori = self.txt_idKategori.text()
            jenis_kategori = self.txt_jenisKategori.text()
            created_at_str = self.txt_createdAt.text()
            updated_at_str = self.txt_updatedAt.text()

            # Konversi ke datetime
            created_at = datetime.strptime(created_at_str, "%Y-%m-%d")
            updated_at = datetime.strptime(updated_at_str, "%Y-%m-%d")

            formatted_created = created_at.strftime("%Y-%m-%d")
            formatted_updated = updated_at.strftime("%Y-%m-%d")

        except ValueError as ve:
            QMessageBox.critical(self, "Input Error", f"Format input salah: {ve}")
            return

        # Buat baris baru
        row = [
            QStandardItem(id_kategori),
            QStandardItem(jenis_kategori),
            QStandardItem(formatted_created),
            QStandardItem(formatted_updated)
        ]

        # Tambahkan baris ke model
        self.model.appendRow(row)

        # Tampilkan pesan sukses
        QMessageBox.information(self, "Info tambah", "Data berhasil tersimpan")

    def baca_teks(self):
        def cvt(datas):
            try:
                return ast.literal_eval(datas)
            except Exception:
                return str(datas)

        db_mysql = read()
        return tuple(map(cvt,db_mysql))

    def ubah_teks(self):
        try:
            id_kategori = self.txt_idKategori.text()
            jenis_kategori = self.txt_jenisKategori.text()
            created_at_str = self.txt_createdAt.text()
            updated_at_str = self.txt_updatedAt.text()

            # Konversi ke datetime
            created_at = datetime.strptime(created_at_str, "%Y-%m-%d")
            updated_at = datetime.strptime(updated_at_str, "%Y-%m-%d")

            formatted_created = created_at.strftime("%Y-%m-%d")
            formatted_updated = updated_at.strftime("%Y-%m-%d")

        except ValueError as ve:
            QMessageBox.critical(self, "Input Error", f"Format input salah: {ve}")
            return

    def hapus_teks(self):
        self.tableWidget.clear()

    def bersih_teks(self):
        try:
            self.txt_idKategori.clear()
            self.txt_jenisKategori.clear()
            self.txt_createdAt.clear()
            self.txt_updatedAt.clear()
        except ValueError:
            self.close()
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormKategori()
    window.show()

    sys.exit(app.exec_())

# Menampilkan layar Aplikasi Form UTS

