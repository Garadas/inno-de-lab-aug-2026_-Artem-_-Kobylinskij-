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
            
            
class HardworkingTrainee(Trainee):
    def do_homework(self) -> None:
        self.score += 2
        """Increases score by 2"""
        
class AuditTrainee(Trainee):
    def is_passing(self) -> bool:
        return True
    
class Cohort:
    title: str
    trainees: list[Trainee]
    
    def __init__(self, title: str,trainees: list[Trainee] = []) -> None:
        self.title = title
        self.trainees = trainees if trainees is not None else []
    
    def add_trainee(self, trainee: Trainee) -> None:
        self.trainees.append(trainee)
    
    def conduct_lecture(self) -> None: 
        for t in self.trainees:
           t.visit_lecture()    
           
    def get_passing_students(self) -> list[Trainee]:
        passing_student = [] 
        for t in self.trainees:
            if t.is_passing(): 
                passing_student.append(t)
        return passing_student
        
        
# 1. Создаем учащихся разных типов
std_trainee = Trainee("Алексей", "Смирнов", score=8, passing_grade=10)
hard_trainee = HardworkingTrainee("Елена", "Петрова", score=8, passing_grade=10)
audit_trainee = AuditTrainee("Дмитрий", "Сидоров", score=0, passing_grade=10)

# 2. Создаем группу и добавляем студентов
cohort = Cohort("Python Advanced")
cohort.add_trainee(std_trainee)
cohort.add_trainee(hard_trainee)
cohort.add_trainee(audit_trainee)

# 3. Проводим лекцию для всей группы (+1 балл всем)
cohort.conduct_lecture()

# 4. Проверяем работу переопределенного ДЗ для трудоголика (+2 балла)
hard_trainee.do_homework()

# 5. Выводим список тех, кто проходит курс
passing_students = cohort.get_passing_students()

print(f"=== УСПЕВАЕМОСТЬ ГРУППЫ '{cohort.title}' ===")
for student in cohort.trainees:
    print(f"{student.name} {student.surname} | Баллы:{student.score} | Проходит: {student.is_passing()}")
    
print("\nУспешно зачислены на следующий модуль:")
for student in passing_students:
    print(f"- {student.name} {student.surname}")
    
    