class Trainee:
    name: str
    surname: str
    __score: int
    passing_grade: int
    
    def __init__(self, name: str, surname: str, score: int = 0, passing_grade: int = 10) -> None:
        self.name = name
        self.surname = surname
        self.__score = score
        self.passing_grade = passing_grade

    def do_homework(self) -> None:
        self.score += 1
        """Increases score by 1"""
        
    def miss_homework(self) -> None:
        self.score -= 1
        """Decreases score by 1"""
        
    def visit_lecture(self) -> None:
        self.score += 1
        """Increases score by 1"""
        
    def miss_lecture(self) -> None:
        self.score -= 1
        """Decreases score by 1"""
        
    def is_passing(self) -> bool:
        if (self.score >= self.passing_grade): 
            return True
        else:
            return False
         
    @property
    def score(self) -> int:
        return self.__score
        
    @score.setter
    def score(self, value) -> None:
        if not isinstance(value, int):
            raise ValueError(f"Expected value of type int, got {type(value)}")  
        elif(value < 0):
            raise ValueError ("The score shouldn't be less than 0!")
        else:
            self.__score = value

print("=== ПРОВЕРКА УСПЕВАЕМОСТИ СТАЖЕРА ===")
# 1. Создание стажера с начальным баллом 9 и проходным баллом 10
trainee = Trainee(name="Иван", surname="Иванов", score=9, passing_grade=10)
# 2. Выполнение домашнего задания и проверка статуса
trainee.do_homework()
print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")
# 3. Пропуск лекции и проверка статуса
trainee.miss_lecture()
print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")
# 4. Проверка валидации (попытка задать неверный тип или отрицательное значение)
try:
    trainee.score = -5
except ValueError as e:
    print(f"Ошибка: {e}")
  