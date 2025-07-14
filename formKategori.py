import sys
import datetime

# Mengimport library PyQt5
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import *

from PYTHON_2310010325.crud_kategori import *

class FormKategori(QMainWindow):
    def __init__(self):
        super(FormKategori, self).__init__()
        uic.loadUi('formKategori.ui', self)

        # Inisialisasi tabel kategori
        self.model = QStandardItemModel(0, 4)  # 0 baris awal, 4 kolom
        self.model.setHorizontalHeaderLabels(['ID Kategori', 'Jenis Kategori', 'Created At', 'Updated At'])

        self.tb_output.setModel(self.model)

        self.btnTambah.clicked.connect(self.tambah_teks)
        self.btnUbah.clicked.connect(self.ubah_teks)
        self.btnHapus.clicked.connect(self.hapus_teks)
        self.btnRead.clicked.connect(self.baca_teks)
        self.btnClear.clicked.connect(self.bersih_teks)

    def tambah_teks(self):
        id_kategori = self.txt_idKategori.text()
        jenis_kategori = self.txt_jenisKategori.text()
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            pesan = create(id_kategori, jenis_kategori, created_at, updated_at)

            # Tambahkan baris baru
            row = [
                QStandardItem(id_kategori),
                QStandardItem(jenis_kategori),
                QStandardItem(created_at),
                QStandardItem(updated_at)
            ]

            self.model.appendRow(row)

            # Tampilkan pesan sukses (Ketika data berhasil disimpan)
            if pesan:
                pesan = "Data berhasil disimpan"
                QMessageBox.information(self, "Sukses", pesan)

        except Exception as e:
            pesanError = f"Terjadi kesalahan: {e}"
            QMessageBox.information(self, "Error", pesanError)

    def baca_teks(self):
        try:
            pesan = read()

            for row_data in pesan:
                row_items = [QStandardItem(str(item)) for item in row_data]
            self.model.appendRow(row_items)

            if pesan:
                pesan = "Data berhasil ditampilkan"
                QMessageBox.information(self, "Sukses", pesan)

        except Exception as e:
            QMessageBox.critical(self,"Error",f"Gagal menampilkan pesan {e}")

    def ubah_teks(self):
        id_kategori = self.txt_idKategori.text()
        jenis_kategori = self.txt_jenisKategori.text()
        created_at = datetime.now().strftime("%Y-%m-%d")
        updated_at = datetime.now().strftime("%Y-%m-%d")

        # Buat baris baru
        try:
            pesan = update(id_kategori,jenis_kategori,created_at,updated_at)

            if pesan:
                pesan = "Data berhasil disimpan"
                QMessageBox.information(self, "Sukses", pesan)

            row = [
                QStandardItem(id_kategori),
                QStandardItem(jenis_kategori),
                QStandardItem(created_at),
                QStandardItem(updated_at)
            ]
            self.model.appendRow(row)

            # Tampilkan pesan sukses (Ketika data berhasil dirubah)
            QMessageBox.information(self, "Info ubah", "Data berhasil terubah")

        except ValueError as ve:
            QMessageBox.critical(self, "Input Error", f"Format input salah: {ve}")
            return

    def hapus_teks(self):
        delete_id_kategori = self.txt_idKategori.text()
        try:
            if not delete_id_kategori:
                QMessageBox.warning(self, 'Info', 'Pilih data yang dihapus dari tabel')
                return

            # Konfirmasi penghapusan
            info = QMessageBox.question(self, 'Konfirmasi', 'Anda yakin ingin menghapus data ini?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if info == QMessageBox.No:
                return

            # Memanggil fungsi delete dari crud_kategori.py
            delete(delete_id_kategori)

            # Kosongkan tabel output
            self.model.setRowCount(0)

            # Tampilkan pesan sukses (Ketika data berhasil dihapus)
            QMessageBox.information(self, "Sukses", "Data berhasil dihapus")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menghapus data: {e}")

        # self.tb_output.clear()

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

