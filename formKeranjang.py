import sys
from datetime import datetime

# Mengimport library PyQt5
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from PYTHON_2310010325.crud_keranjang import *

class FormKeranjang(QMainWindow):
    def __init__(self):
        super(FormKeranjang, self).__init__()
        uic.loadUi('formKeranjang.ui', self)

        # Inisialisasi tabel keranjang
        self.model = QStandardItemModel(0, 6)
        self.model.setHorizontalHeaderLabels([
            'ID Keranjang', 'Nama Menu', 'Qty', 'Catatan',
            'Created At', 'Updated At'
        ])
        self.tb_output.setModel(self.model)

        # Hubungkan tombol ke fungsi
        self.btnTambah.clicked.connect(self.tambah_teks)
        self.btnUbah.clicked.connect(self.ubah_teks)
        self.btnHapus.clicked.connect(self.hapus_teks)
        self.btnRead.clicked.connect(self.baca_teks)
        self.btnClear.clicked.connect(self.bersih_teks)

    def tambah_teks(self):
        id_keranjang = self.txt_idKeranjang.text()
        nama_menu = self.txt_namaMenu.text()
        qty = self.txt_qty.text()
        catatan = self.txt_catatan.text()
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            pesan = create(id_keranjang, nama_menu, qty, catatan, created_at, updated_at)
            QMessageBox.information(self, "Sukses", pesan)

            row = [
                QStandardItem(id_keranjang),
                QStandardItem(nama_menu),
                QStandardItem(qty),
                QStandardItem(catatan),
                QStandardItem(created_at),
                QStandardItem(updated_at),
            ]
            self.model.appendRow(row)

        except Exception:
            QMessageBox.critical(self, "fgagal menyimpan DATA",pesan)

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
        id_keranjang = self.txt_idKeranjang.text()
        nama_menu = self.txt_namaMenu.text()
        qty = self.txt_qty.text()
        catatan = self.txt_catatan.text()

        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            pesan = update(id_keranjang,nama_menu,qty,catatan,created_at,updated_at)
            QMessageBox.information(self,'Sukses',pesan)

            row = [
                QStandardItem(id_keranjang),
                QStandardItem(nama_menu),
                QStandardItem(qty),
                QStandardItem(catatan),
                QStandardItem(created_at),
                QStandardItem(updated_at),
            ]
            self.model.appendRow(row)

            # Tampilkan pesan sukses (Ketika data berhasil dirubah)
            QMessageBox.information(self, "Info ubah", "Data berhasil terubah")

        except ValueError as ve:
            QMessageBox.critical(self, "Input Error", f"Format input salah: {ve}")
            return

    def hapus_teks(self):
        delete_id_keranjang = self.txt_idKeranjang.text()
        try:
            if not delete_id_keranjang:
                QMessageBox.warning(self, 'Info', 'Pilih data yang dihapus dari tabel')
                return

            # Konfirmasi penghapusan
            info = QMessageBox.question(self, 'Konfirmasi', 'Anda yakin ingin menghapus data ini?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if info == QMessageBox.No:
                return

            # Panggil fungsi delete dari crud_keranjang.py
            delete(delete_id_keranjang)

            # Kosongkan isi tabel
            self.model.setRowCount(0)

            # Tampilkan pesan sukses (Ketika data berhasil dihapus)
            QMessageBox.information(self, "Sukses", "Data berhasil dihapus")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menghapus data: {e}")


    def bersih_teks(self):
        self.txt_idKeranjang.clear()
        self.txt_namaMenu.clear()
        self.txt_qty.clear()
        self.txt_catatan.clear()
        self.txt_createdAt.clear()
        self.txt_updatedAt.clear()
        QMessageBox.information(self, "Info", "Form telah dibersihkan")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormKeranjang()
    window.show()
    sys.exit(app.exec_())