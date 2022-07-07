import datetime


class Company:

    def __init__(self, cname="Rabota", position="Работник", salary=6000):
        if cname == "Rabota":
            self._CName = cname
            self._Position = position
            self._Salary = salary
        else:
            self._Position = position
            self._Salary = salary

    @property
    def Salary(self):
        return self._Salary


class Worker:

    def __init__(self, name="Иван", year=2020, month=9, cname="", pos="", sal=""):
        self._Sname = name
        self._Year = year
        self._Month = month
        if cname == "":
            self._WorkPlace = Company()
        else:
            self._WorkPlace = Company()
            self._WorkPlace._CName = cname
            self._WorkPlace._Position = pos
            self._WorkPlace._Salary = sal

    def get_Name(self):
        return self._Sname

    def set_Name(self, name):
        self._Sname = name

    def get_Year(self):
        return self._Year

    def set_Year(self, year):
        self._Year = year

    def get_Month(self):
        return self._Month

    def set_Month(self, month):
        self._Month = month

    def get_CName(self):
        return self._WorkPlace._CName

    def set_CName(self, cname):
        self._WorkPlace._CName = cname

    def get_Position(self):
        return self._WorkPlace._Position

    def set_Position(self, position):
        self._WorkPlace._Position = position

    def get_Salary(self):
        return self._WorkPlace.Salary

    def set_Salary(self, salary):
        self._WorkPlace._Salary = salary

    def GetWorkExperience(self):
        now = datetime.datetime.now()
        G_Month = now.month
        G_Year = now.year
        S_Month = self._Month
        S_Year = self._Year
        sum = G_Year - S_Year
        sum = sum * 12
        sum = sum - S_Month + G_Month
        print("В общем сотрудник проработал в компании", sum, "месяця")

    def GetWorkExperience2(self):
        now = datetime.datetime.now()
        G_Month = now.month
        G_Year = now.year
        S_Month = self._Month
        S_Year = self._Year
        sum = G_Year - S_Year
        sum = sum * 12
        sum = sum - S_Month + G_Month
        return sum

    def GetTotalMoney(self):
        now = datetime.datetime.now()
        G_Month = now.month
        G_Year = now.year
        S_Month = self._Month
        S_Year = self._Year
        sum = G_Year - S_Year
        sum = sum * 12
        sum = sum - S_Month + G_Month
        sum1 = sum * self._WorkPlace.Salary
        print("В общем за", sum, "месяцев, было заработано:", sum1, "грн")


class Program:

    def ReadWorkersArray(self, List, i, size):
        now = datetime.datetime.now()
        b = i
        while i < b + size:
            List[i] = Worker()
            print("Введите имя", i+1,  "-го сотрудника")
            temp = input("Имя сотрудника:")
            if temp != "":
                List[i].set_Name(temp)

            while True:
                temp = input("Год начала работы сотдрудника сотрудника:")
                if temp == "":
                    break
                else:
                    temp2 = int(temp)

                if temp2 < 1900 or temp2 > now.year:
                    print("Неверно указан год")
                else:
                    List[i].set_Year(temp2)
                    break

            while True:
                temp = input("Месяц начала работы сотрудника:")
                if temp == "":
                    break
                else:
                    temp2 = int(temp)

                if temp2 < 1 or temp2 > 12:
                    print("Неверно указан Месяц")
                else:
                    List[i].set_Month(temp2)
                    break

            temp = input("Название компании сотрудника:")
            if temp != "":
                List[i].set_CName(temp)
            temp = input("Должность сотрудника:")
            if temp != "":
                List[i].set_Position(temp)

            temp = input("Зарплата сотрудника:")
            while True:
                if temp == "":
                    break
                else:
                    temp2 = int(temp)

                if temp2 < 0:
                    print("Неверно указана Зарплата")
                else:
                    List[i].set_Salary(temp2)
                    break

            i += 1

    def PrintWorker(self, List, i):
        print(List[i].get_Name(), List[i].get_Year(), List[i].get_Month(), List[i].get_CName(), List[i].get_Position(),
              List[i].get_Salary())

    def PrintWorkers(self, List, size):
        i = 0
        while i < size:
            print(List[i].get_Name(), List[i].get_Year(), List[i].get_Month(), List[i].get_CName(),
                  List[i].get_Position(),
                  List[i].get_Salary())
            i += 1

    def GetWorkersInfo(self, List, size):
        Salary = 0
        max = 0
        min = 0
        p1 = 0
        p2 = 0
        Salary = List[0].get_Salary()
        max = Salary
        min = Salary
        for i in range(size):
            Salary = List[i].get_Salary()
            if max < Salary:
                max = Salary
                p1 = i

            if min > Salary:
                min = Salary
                p2 = i

        print("Самая болшая зарпалата у сотрудника", p1 + 1, max)
        print("Самая болшая зарпалата у сотрудника", p2 + 1, min)

    def SortWorkerBySalary(self, List, size):

        temp = Worker()
        i = 0
        while i < size:
            j = size - 1
            while j >= (i + 1):

                salary1 = List[j].get_Salary()
                salary2 = List[j - 1].get_Salary()

                if salary1 > salary2:

                    temp = List[j]
                    List[j] = List[j - 1]
                    List[j - 1] = temp
                    j -= 1
                else:
                    j -= 1
            i += 1

    def SortWorkerByWorkExperience(self, List, size):
        temp = Worker()
        i = 0
        while i < size:
            j = size - 1
            while j >= (i + 1):

                sum1 = List[j].GetWorkExperience2()
                sum2 = List[j - 1].GetWorkExperience2()

                if sum1 < sum2:

                    temp = List[j]
                    List[j] = List[j - 1]
                    List[j - 1] = temp
                    j -= 1
                else:
                    j -= 1
            i += 1


List = ["Такого сотрудника не существует"] * 50
Current = Program()
size = 0
Add = False
while True:
    print("------------------------------------------------------------------")
    print("|1 - Ввести сотрудника                                           |")
    print("|2 - Вывести список сотрудников на экран                         |")
    print("|3 - Узнать информацию он зарпалтах сотрудников                  |")
    print("|4 - Сортировка                                                  |")
    print("|5 - Узнать стаж работы сотрудника                               |")
    print("|6 - Узнать общее количетсво заработаных средств сотрудника      |")
    print("|0 - Выход                                                       |")
    print("------------------------------------------------------------------")
    str1 = input()
    choise1 = int(str1)
    if choise1 == 1:
        while True:
            print("Сколько сотрудников хотите ввести?")
            str1 = input()
            temp = int(str1)
            if temp <= 0:
                print("Введите коректное число")
            else:
                Current.ReadWorkersArray(List, size, temp)
                size += temp
                Add = True
                break
    elif choise1 == 2 and Add == True:
        while True:
            print("--------------------------------------------")
            print("|1 - Подробная информацуия о сотруднике    |")
            print("|2 - Вывод всего списка сотрудников        |")
            print("|0 - Выход в главное меню                  |")
            print("--------------------------------------------")
            str2 = input()
            choise2 = int(str2)
            if choise2 < 0 or choise2 > 2:
                print("Неверно указана операция")
            else:
                break
        if choise2 == 1:
            for i in range(size):
                print(i + 1, ".", List[i].get_Name())

            print("Введите номер сотрудника о котором хотите узнать подробную информацию")
            while True:
                num1 = input()
                num = int(num1)
                if num <= 0 or num > size:
                    print("Неверно указан номер работника")
                else:
                    break
            num = num - 1
            Current.PrintWorker(List, num)
            continue
        elif choise2 == 2:
            Current.PrintWorkers(List, size)
            continue
    elif choise1 == 3 and Add == True:
        Current.GetWorkersInfo(List, size)
        continue
    elif choise1 == 4 and Add == True:
        while True:
            print("------------------------------------------")
            print("|1 - Сортировать по зарплате             |")
            print("|2 - Сортировать по стажу                |")
            print("|0 - Выход в главное меню                |")
            print("------------------------------------------")
            str3 = input()
            choise3 = int(str3)
            if choise3 < 0 or choise3 > 2:
                print("Неверно указана операция")
            else:
                break
        if choise3 == 1:
            Current.SortWorkerBySalary(List, size)
            continue
        elif choise3 == 2:
            Current.SortWorkerByWorkExperience(List, size)
            continue
    elif choise1 == 5 and Add == True:
        for i in range(size):
            print(i + 1, ".", List[i].get_Name())
        while True:
            str4 = input()
            a = int(str4)
            if a <= 0 or a > size:
                print("Неверно указан номер работника")
            else:
                break

        List[a - 1].GetWorkExperience()
        continue
    elif choise1 == 6 and Add == True:
        for i in range(size):
            print(i + 1, ".", List[i].get_Name())

        while True:
            str4 = input()
            a = int(str4)
            if a <= 0 or a > size:
                print("Неверно указан номер работника")
            else:
                break

        List[a - 1].GetTotalMoney()
        continue

    elif choise1 == 0:
        break

    elif Add == False or choise1 < 0 or choise1 > 6:
        print("Введите верный номер операции или попробуйте добавить элемент ")
        continue
