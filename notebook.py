import sqlite3

class LienLac:
    def __init__(self):
        self.conn = sqlite3.connect("sotay.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS danh_ba (id INTEGER PRIMARY KEY AUTOINCREMENT, ten TEXT, so_dien_thoai TEXT, email TEXT)")

    def __del__(self):
        self.conn.close()

    def hien_thi_danh_sach(self):
        self.cursor.execute("SELECT * FROM danh_ba")
        rows = self.cursor.fetchall()
        if not rows:
            print("Sổ tay ghi chép rỗng.")
        else:
            print("Danh sách thông tin liên lạc:")
            for row in rows:
                print(f"{row[0]}. Tên: {row[1]}, Số điện thoại: {row[2]}, Email: {row[3]}")

    def them_lien_lac(self):
        ten = input("Nhập tên: ")
        so_dien_thoai = input("Nhập số điện thoại: ")
        email = input("Nhập email: ")
        self.cursor.execute("INSERT INTO danh_ba (ten, so_dien_thoai, email) VALUES (?, ?, ?)", (ten, so_dien_thoai, email))
        self.conn.commit()
        print("Thông tin đã được thêm vào sổ tay ghi chép.")

    def xoa_lien_lac(self):
        self.hien_thi_danh_sach()
        id = input("Nhập số thứ tự người dùng muốn xóa: ")
        self.cursor.execute("DELETE FROM danh_ba WHERE id=?", (id,))
        self.conn.commit()
        print("Thông tin người dùng đã được xóa khỏi sổ tay ghi chép.")

    def chinh_sua_lien_lac(self):
        self.hien_thi_danh_sach()
        id = input("Nhập số thứ tự người dùng muốn chỉnh sửa: ")
        self.cursor.execute("SELECT * FROM danh_ba WHERE id=?", (id,))
        row = self.cursor.fetchone()
        if row:
            print("Chỉnh sửa thông tin người dùng:")
            ten_moi = input(f"Tên ({row[1]}): ")
            so_dien_thoai_moi = input(f"Số điện thoại ({row[2]}): ")
            email_moi = input(f"Email ({row[3]}): ")
            self.cursor.execute("UPDATE danh_ba SET ten=?, so_dien_thoai=?, email=? WHERE id=?", (ten_moi, so_dien_thoai_moi, email_moi, id))
            self.conn.commit()
            print("Thông tin người dùng đã được cập nhật.")
        else:
            print("Số thứ tự không hợp lệ.")

    def menu(self):
        while True:
            print("----- Cuốn Sổ Tay Ghi Chép -----")
            print("1. Hiển thị danh sách liên lạc")
            print("2. Thêm thông tin người dùng")
            print("3. Xóa thông tin người dùng")
            print("4. Chỉnh sửa thông tin người dùng")
            print("5. Thoát")
            choice = input("Nhập lựa chọn của bạn: ")

            if choice == "1":
                self.hien_thi_danh_sach()
            elif choice == "2":
                self.them_lien_lac()
            elif choice == "3":
                self.xoa_lien_lac()
            elif choice == "4":
                self.chinh_sua_lien_lac()
            elif choice == "5":
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


def main():
    sotay = LienLac()
    sotay.menu()


if __name__ == "__main__":
    main()
