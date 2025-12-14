from datetime import date
class person:
    def __init__(self, name, yob):
        self.name, self.yob = name, yob
    def age(self):
        return date.today().year - self.yob
    def describe(self):
        print(f"Person | name : {self.name} | yob : {self.yob} | age : {self.age()}", end = "")
class student(person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade
    def describe(self):
        print("student | ", end="")
        super().describe()
        print(f"| grade : {self.grade}")
class teacher(person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject
    def describe(self):
        print("subject | ", end="")
        super().describe()
        print(f"| subject : {self.subject}")
class doctor(person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist
    def describe(self):
        print("specialist | ", end="")
        super().describe()
        print(f"| specialist : {self.specialist}")
class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []
    def addPerson(self, person):
        self.people.append(person)
    def describe(self):
        print(f"----Ward : {self.name}")
        for p in self.people:
            p.describe()
    def countDoctor(self):
        count = 0
        for p in self.people:
            if isinstance(p, doctor):
                count += 1
        return count 
    def sortAge(self): 
        self.people.sort(key=lambda p: p.age())
    def aveTeacherYearOfBirth(self):
        total = 0
        cnt = 0
        for p in self.people:
            if isinstance(p, teacher):
                total += p.yob
                cnt += 1
            if cnt == 0:
                return None
            return total / cnt 
if __name__ == "__main__":
    ward = Ward("WARD A")

    ward.addPerson(student("A", 2006, "att2"))

    ward.addPerson(teacher("B", 1985, "python"))
    ward.addPerson(teacher("C", 1993, "dsa"))

    ward.addPerson(doctor("D", 1975, "Internal Medicine"))
    ward.addPerson(doctor("E", 1980, "Internal Medicine"))

    ward.describe()

    print("Đếm doctor" , ward.countDoctor())

    ward.sortAge()
    print("Đã sắp xêp theo ....")
    ward.describe()

    print("Năm sinh trung bình : ", ward.aveTeacherYearOfBirth())