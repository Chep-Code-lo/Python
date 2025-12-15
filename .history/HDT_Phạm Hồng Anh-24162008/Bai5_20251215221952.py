from __future__ import annotations
from datetime import date
from typing import List, Dict, Optional
class Employee:
    _count = 0  
    def __init__(self, id: str, name: str, dob: date, phone: str,department: str, base_salary: float, type: int):
        self.__id, self.__name, self.__dob, self.__phone,  = id, name, dob, phone
        self.__department = department
        self.__base_salary = float(base_salary)
        self.__emp_type = int(type)

        Employee._count += 1
    @property
    def emp_id(self) -> str:
        return self.__id

    @property
    def full_name(self) -> str:
        return self.__name
    @full_name.setter
    def full_name(self, value: str) -> None:
        if not value.strip():
            raise ValueError("Họ tên không được rỗng")
        self.__name = value.strip()

    @property
    def dob(self) -> date:
        return self.__dob

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, value: str) -> None:
        if not value.strip():
            raise ValueError("SĐT không được rỗng")
        self.__phone = value.strip()

    @property
    def department(self) -> str:
        return self.__department

    @property
    def base_salary(self) -> float:
        return self.__base_salary

    @base_salary.setter
    def base_salary(self, value: float) -> None:
        if value < 0:
            raise ValueError("Lương cơ bản phải >= 0")
        self.__base_salary = float(value)

    @property
    def emp_type(self) -> int:
        return self.__emp_type

    def update_department(self, new_department: str) -> None:
        if not new_department.strip():
            raise ValueError("Phòng ban không được rỗng")
        self.__department = new_department.strip()

    def compute_salary(self) -> float:
        return self.base_salary

    def show_info(self) -> None:
        print(
            f"ID: {self.emp_id} | Name: {self.full_name} | DOB: {self.dob.isoformat()} | "
            f"Phone: {self.phone} | Dept: {self.department} | Base: {self.base_salary:.2f} | "
            f"Type: {self.emp_type} | Salary: {self.compute_salary():.2f}"
        )

    @classmethod
    def count_employees(cls) -> int:
        return cls._count
    
class Manager(Employee):
    def __init__(self, id: str, name: str, dob: date, phone: str, department: str,
                 base_salary: float, bonus: float = 0.0, allowance: float = 0.0,
                 overtime_hours: float = 0.0, overtime_rate: float = 0.0):
        super().__init__(id, name, dob, phone, department, base_salary, type=0)
        self.bonus = float(bonus)
        self.allowance = float(allowance)
        self.overtime_hours = float(overtime_hours)
        self.overtime_rate = float(overtime_rate)

    def compute_salary(self) -> float:
        return self.base_salary + self.allowance + self.bonus + (self.overtime_hours * self.overtime_rate)

    def show_info(self) -> None:
        print("Manager", end=" ")
        super().show_info()
class Developer(Employee):
    def __init__(self, id: str, name: str, dob: date, phone: str, department: str,
                 base_salary: float, project: str = "", project_bonus: float = 0.0,
                 overtime_hours: float = 0.0, overtime_rate: float = 0.0):
        super().__init__(id, name, dob, phone, department, base_salary, type=1)
        self.project = project
        self.project_bonus = float(project_bonus)
        self.overtime_hours = float(overtime_hours)
        self.overtime_rate = float(overtime_rate)

    def compute_salary(self) -> float:
        return self.base_salary + self.project_bonus + (self.overtime_hours * self.overtime_rate)

    def show_info(self) -> None:
        print(f"Developer | Project: {self.project}]", end=" ")
        super().show_info()


class Tester(Employee):
    def __init__(self, id: str, name: str, dob: date, phone: str, department: str,
                 base_salary: float, specialty: str = "", qa_bonus: float = 0.0,
                 overtime_hours: float = 0.0, overtime_rate: float = 0.0):
        super().__init__(id, name, dob, phone, department, base_salary, type=2)
        self.specialty = specialty
        self.qa_bonus = float(qa_bonus)
        self.overtime_hours = float(overtime_hours)
        self.overtime_rate = float(overtime_rate)

    def compute_salary(self) -> float:
        return self.base_salary + self.qa_bonus + (self.overtime_hours * self.overtime_rate)

    def show_info(self) -> None:
        print(f"Tester | Specialty: {self.specialty}]", end=" ")
        super().show_info()

class EmployeeManager:
    def __init__(self):
        self._employees: List[Employee] = []

    def add_employee(self, emp: Employee) -> None:
        if any(e.emp_id == emp.emp_id for e in self._employees):
            raise ValueError(f"ID {emp.emp_id} đã tồn tại")
        self._employees.append(emp)

    def find_by_id(self, emp_id: str) -> Optional[Employee]:
        for e in self._employees:
            if e.emp_id == emp_id:
                return e
        return None

    def update_department(self, emp_id: str, new_dept: str) -> bool:
        emp = self.find_by_id(emp_id)
        if not emp:
            return False
        emp.update_department(new_dept)
        return True
    
    def print_payroll(self) -> None:
        print("=== PAYROLL ===")
        for e in self._employees:
            e.show_info()

    def total_payroll_cost(self) -> float:
        return sum(e.compute_salary() for e in self._employees)

    def count_by_type(self) -> Dict[int, int]:
        stats: Dict[int, int] = {}
        for e in self._employees:
            stats[e.emp_type] = stats.get(e.emp_type, 0) + 1
        return stats

    def payroll_by_department(self) -> Dict[str, float]:
        stats: Dict[str, float] = {}
        for e in self._employees:
            stats[e.department] = stats.get(e.department, 0.0) + e.compute_salary()
        return stats
    def list_all(self) -> List[Employee]:
        return list(self._employees)