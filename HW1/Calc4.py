#в данной задаче создадим класс калькулятора с разными возможностями, комментарии написаны через переводчик
class CalculatorHealth:
    def __init__(self, name: str = "User", weight: float = 80.0, height: float = 178.0, steps: int = 10000): #Initialize the person's data (defaulting to average values ​​for a human)
        self.name = name 
        self.weight = weight
        self.height = height
        self.steps = steps


    def BMI(self): #BMI calculator that determines whether a person's result is within the normal range.
        height_m = float(self.height) / 100
        bmi = float(self.weight / (height_m ** 2))
        bmi = round(bmi, 1)
        if bmi < 18.5:
            category = str("дефицит массы тела")
        elif 18.5 <= bmi < 25.0:
            category = str("нормальный вес")
        elif 25.0 <= bmi < 30.0:
            category = str("избыточная масса тела (предожирение)")
        else:
            category = str("ожирение")
        return f"{self.name}, у вас {category}"


    def calories(self): #Calculator for calories burned by a person in a day
        return f"{self.name}, вы сожгли примерно {round(self.steps / 10000 * 400, 0)} калорий"
        
    
print("Добро пожадовать")
print("Введите имя")
name = str(input())

while True:
    print("Выберите тип калькулятора или нажмите 3 для выхода")
    print("1: BMI - индекс массы тела")
    print("2: Calories - сожженные калории за день")
    operation = str(input())

    if operation in ("1", "BMI", "индекс", "ИМТ"):
        weight_people = int(input("Введите вес в кг: "))
        height_people = int(input("Введите рост в см: "))
        calc_people = CalculatorHealth(name, weight = weight_people, height = height_people)
        print(calc_people.BMI())
                     
    elif operation in ("2", "Calories", "калории"):
            steps_people = int(input("Введите целое число шагов: "))
            calc_people = CalculatorHealth(name,steps = steps_people)
            print(calc_people.calories())

    elif operation in ("3", "выход", "exit"):
        break;

print("Программа закончена")
