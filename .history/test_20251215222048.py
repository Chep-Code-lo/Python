from datetime import datetime

# --- 1. Lớp Cha: Employee ---
class Employee:
    # Biến cấp lớp (Class Variable) để đếm số lượng nhân viên
    emp_count = 0

    def __init__(self, emp_id, name, dob, phone, dept, basic_salary, emp_type):
        self._id = emp_id              # String
        self._name = name              # String
        self._dob = dob                # datetime.date
        self._phone = phone            # String
        self._dept = dept              # String
        self._basic_salary = basic_salary # Float
        self._emp_type = emp_type      # Int (0: Manager, 1: Dev, 2: Tester)
        
        # Tăng biến đếm mỗi khi tạo mới nhân viên
        Employee.emp_count += 1

    # --- Getter / Setter (Đóng gói) ---
    def get_name(self):
        return self._name

    def set_department(self, new_dept):
        self._dept = new_dept
        print(f"-> Đã cập nhật phòng ban mới cho {self._name}: {self._dept}")

    def set_basic_salary(self, new_salary):
        self._basic_salary = new_salary

    # --- Phương thức tính lương (Sẽ được ghi đè - Polymorphism) ---
    def compute_salary(self):
        return self._basic_salary

    # --- Hiển thị thông tin ---
    def show_info(self):
        # Định dạng ngày sinh ra string cho dễ đọc
        dob_str = self._dob.strftime("%d/%m/%Y")
        
        # Mapping loại nhân viên
        type_str = "N/A"
        if self._emp_type == 0: type_str = "Manager"
        elif self._emp_type == 1: type_str = "Developer"
        elif self._emp_type == 2: type_str = "Tester"

        print(f"ID: {self._id:<5} | Tên: {self._name:<15} | Loại: {type_str:<10} | Phòng: {self._dept:<10}")
        print(f"   NS: {dob_str} | SĐT: {self._phone} | Lương CB: {self._basic_salary:,.0f}")

# --- 2. Các Lớp Con ---

class Manager(Employee):
    def __init__(self, emp_id, name, dob, phone, dept, basic_salary, bonus):
        # Gọi constructor lớp cha
        super().__init__(emp_id, name, dob, phone, dept, basic_salary, 0)
        self._bonus = bonus # Thưởng riêng cho Manager

    # Ghi đè tính lương: Lương CB + Bonus
    def compute_salary(self):
        return self._basic_salary + self._bonus

    def show_info(self):
        super().show_info()
        print(f"   -> Bonus lãnh đạo: {self._bonus:,.0f} | TỔNG LƯƠNG: {self.compute_salary():,.0f}")


class Developer(Employee):
    def __init__(self, emp_id, name, dob, phone, dept, basic_salary, ot_hours, project_name):
        super().__init__(emp_id, name, dob, phone, dept, basic_salary, 1)
        self._ot_hours = ot_hours      # Giờ làm thêm
        self._project_name = project_name
        self._ot_rate = 200000         # 200k/giờ OT

    # Ghi đè tính lương: Lương CB + (Giờ OT * Giá OT)
    def compute_salary(self):
        return self._basic_salary + (self._ot_hours * self._ot_rate)

    def show_info(self):
        super().show_info()
        print(f"   -> Dự án: {self._project_name} | OT: {self._ot_hours}h | TỔNG LƯƠNG: {self.compute_salary():,.0f}")


class Tester(Employee):
    def __init__(self, emp_id, name, dob, phone, dept, basic_salary, bugs_found, specialization):
        super().__init__(emp_id, name, dob, phone, dept, basic_salary, 2)
        self._bugs_found = bugs_found  # Số bug tìm được
        self._specialization = specialization # Manual/Automation
        self._bug_rate = 50000         # 50k/bug

    # Ghi đè tính lương: Lương CB + (Số Bug * Giá Bug)
    def compute_salary(self):
        return self._basic_salary + (self._bugs_found * self._bug_rate)

    def show_info(self):
        super().show_info()
        print(f"   -> Chuyên môn: {self._specialization} | Bugs: {self._bugs_found} | TỔNG LƯƠNG: {self.compute_salary():,.0f}")


# --- 3. Lớp Quản Lý Hệ Thống (Controller) ---
class QuanLyNhanSu:
    def __init__(self):
        self.ds_nhan_vien = []

    def them_nhan_vien(self, nv):
        self.ds_nhan_vien.append(nv)

    def tim_nhan_vien(self, emp_id):
        for nv in self.ds_nhan_vien:
            if nv._id == emp_id:
                return nv
        return None

    def xuat_danh_sach(self):
        print("\n=== DANH SÁCH NHÂN VIÊN ===")
        for nv in self.ds_nhan_vien:
            nv.show_info()
            print("-" * 50)

    def cap_nhat_phong_ban(self):
        emp_id = input("Nhập ID nhân viên cần chuyển phòng: ")
        nv = self.tim_nhan_vien(emp_id)
        if nv:
            new_dept = input("Nhập tên phòng ban mới: ")
            nv.set_department(new_dept) # Sử dụng Setter
        else:
            print("Không tìm thấy nhân viên!")

    def bao_cao_tong_hop(self):
        print("\n=== BÁO CÁO TỔNG HỢP ===")
        total_salary = 0
        count_mgr = 0
        count_dev = 0
        count_test = 0

        # Áp dụng Đa hình: Duyệt qua danh sách, gọi compute_salary() 
        # mà không cần quan tâm là đối tượng nào
        for nv in self.ds_nhan_vien:
            luong = nv.compute_salary()
            total_salary += luong
            
            if nv._emp_type == 0: count_mgr += 1
            elif nv._emp_type == 1: count_dev += 1
            elif nv._emp_type == 2: count_test += 1

        print(f"Tổng số nhân viên (Class Variable): {Employee.emp_count}")
        print(f" - Manager: {count_mgr}")
        print(f" - Developer: {count_dev}")
        print(f" - Tester: {count_test}")
        print(f"Tổng quỹ lương phải trả: {total_salary:,.0f} VNĐ")

# --- Hàm hỗ trợ nhập liệu để Main gọn hơn ---
def nhap_ngay_sinh():
    while True:
        try:
            d_str = input("Nhập ngày sinh (dd/mm/yyyy): ")
            return datetime.strptime(d_str, "%d/%m/%Y").date()
        except ValueError:
            print("Định dạng ngày sai. Vui lòng nhập lại!")

# --- Main Program ---
def main():
    ql = QuanLyNhanSu()

    while True:
        print("\n--- HR MANAGEMENT SYSTEM ---")
        print("1. Thêm Manager")
        print("2. Thêm Developer")
        print("3. Thêm Tester")
        print("4. Xuất danh sách nhân viên")
        print("5. Cập nhật phòng ban")
        print("6. Báo cáo tổng hợp")
        print("0. Thoát")
        
        choice = input("Chọn chức năng: ")

        if choice in ['1', '2', '3']:
            # Nhập thông tin chung
            eid = input("ID: ")
            name = input("Họ tên: ")
            dob = nhap_ngay_sinh()
            phone = input("SĐT: ")
            dept = input("Phòng ban: ")
            salary = float(input("Lương cơ bản: "))

            if choice == '1': # Manager
                bonus = float(input("Nhập tiền thưởng (Bonus): "))
                nv = Manager(eid, name, dob, phone, dept, salary, bonus)
            elif choice == '2': # Developer
                ot = float(input("Số giờ OT: "))
                proj = input("Dự án đang làm: ")
                nv = Developer(eid, name, dob, phone, dept, salary, ot, proj)
            elif choice == '3': # Tester
                bugs = int(input("Số bugs tìm được: "))
                spec = input("Chuyên môn (Manual/Automation): ")
                nv = Tester(eid, name, dob, phone, dept, salary, bugs, spec)
            
            ql.them_nhan_vien(nv)
            print("-> Thêm thành công!")

        elif choice == '4':
            ql.xuat_danh_sach()
        elif choice == '5':
            ql.cap_nhat_phong_ban()
        elif choice == '6':
            ql.bao_cao_tong_hop()
        elif choice == '0':
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()