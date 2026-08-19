# Проектирование базы данных: Система высшего образования

## Part 1: Выбор сценария

Для данной работы выбран сценарий: **Система высшего образования**.

Эта система будет управлять студентами, преподавателями, группами, расписанием, аудиториями и предметами.

## Part 2: Проектирование базы данных и документация

### Идентификация сущностей и атрибутов

1. **Студенты (Students)** — хранит информацию о студентах
2. **Преподаватели (Teachers)** — хранит информацию о преподавателях
3. **Группы (Groups)** — хранит информацию о группах
4. **Расписание (Schedule)** — для составления расписания
5. **Аудитории (Classrooms)** — хранит информацию об аудиториях
6. **Предметы (Subjects)** — хранит информацию о предметах

---

## Проектирование таблиц

### 1. Students

Хранит информацию о студентах.

| Атрибут | Тип | Ограничения |
|---|---|---|
| id | SERIAL | PK |
| First_name | VARCHAR(100) | NOT NULL |
| Last_name | VARCHAR(100) | NOT NULL |
| Middle_name | VARCHAR(100) | — |
| Birthdate | DATE | NOT NULL |
| Has_scholarship | BOOLEAN | — |
| id_group | INTEGER | FK, NOT NULL |

**Constraints:**

```sql
PK_Students: PRIMARY KEY (id)
FK_Students_Groups: FOREIGN KEY (id_group) REFERENCES Groups(id)
```

---

### 2. Teachers

Хранит информацию о преподавателях.

| Атрибут | Тип | Ограничения |
|---|---|---|
| id | SERIAL | PK |
| First_name | VARCHAR(100) | NOT NULL |
| Last_name | VARCHAR(100) | NOT NULL |
| Middle_name | VARCHAR(100) | — |
| Birthdate | DATE | NOT NULL |
| Education | VARCHAR(100) | — |
| Department | VARCHAR(150) | — |

**Constraints:**

```sql
PK_Teachers: PRIMARY KEY (id)
```

---

### 3. Groups

Хранит информацию о группах.

| Атрибут | Тип | Ограничения |
|---|---|---|
| id | SERIAL | PK |
| Name | VARCHAR(30) | — |

**Constraints:**

```sql
PK_Groups: PRIMARY KEY (id)
```

---

### 4. Schedule

Для составления расписания.

| Атрибут | Тип | Ограничения |
|---|---|---|
| id | SERIAL | PK |
| id_group | INTEGER | FK, NOT NULL |
| id_teacher | INTEGER | FK, NOT NULL |
| id_subject | INTEGER | FK, NOT NULL |
| id_classroom | INTEGER | FK, NOT NULL |
| Lesson_date | DATE | NOT NULL |
| Class_number | SMALLINT | NOT NULL |
| Lesson_type | ENUM | NOT NULL |

**Constraints:**

```sql
PK_Schedule: PRIMARY KEY (id)

FK_Schedule_Groups: FOREIGN KEY (id_group) REFERENCES Groups(id)
FK_Schedule_Teachers: FOREIGN KEY (id_teacher) REFERENCES Teachers(id)
FK_Schedule_Subjects: FOREIGN KEY (id_subject) REFERENCES Subjects(id)
FK_Schedule_Classrooms: FOREIGN KEY (id_classroom) REFERENCES Classrooms(id)

UK_id_group: UNIQUE (id_group, Lesson_date, Class_number)
UK_id_teacher: UNIQUE (id_teacher, Lesson_date, Class_number)
UK_id_classroom: UNIQUE (id_classroom, Lesson_date, Class_number)

CHK_Lesson_type: CHECK (Lesson_type IN ('lecture', 'seminar', 'lab', 'section'))
```

---

### 5. Classrooms

Хранит информацию об аудиториях.

| Атрибут | Тип | Ограничения |
|---|---|---|
| id | SERIAL | PK |
| Has_projector | BOOLEAN | — |
| Number | VARCHAR(10) | UNIQUE |
| Room_type | ENUM | NOT NULL |
| Capacity | INTEGER | — |

**Constraints:**

```sql
PK_Classrooms: PRIMARY KEY (id)
UK_Number: UNIQUE (Number)
CHK_Room_type: CHECK (Room_type IN ('lecture', 'seminar', 'lab', 'section'))
```

---

### 6. Subjects

Хранит информацию о предметах.

| Атрибут | Тип | Ограничения |
|---|---|---|
| id | SERIAL | PK |
| Name | VARCHAR(150) | NOT NULL |
| Number_of_hours | INTEGER | NOT NULL |

**Constraints:**

```sql
PK_Subjects: PRIMARY KEY (id)
```

---

## Взаимосвязи

### Groups и Students (Один-ко-Многим)

В одной группе может находиться несколько студентов, но каждый студент может быть только в 1 группе.

- `Students.id_group` является внешним ключом, ссылающимся на `Groups.id`.

### Groups и Schedule (Один-ко-Многим)

Одна группа может посещать несколько занятий, но каждое занятие проводится, в идеале, для 1 группы.

- `Schedule.id_group` является внешним ключом, ссылающимся на `Groups.id`.

### Teachers и Schedule (Один-ко-Многим)

Один преподаватель может вести несколько занятий в разное время, но каждое занятие проводится только 1 преподавателем.

- `Schedule.id_teacher` является внешним ключом, ссылающимся на `Teachers.id`.

### Classrooms и Schedule (Один-ко-Многим)

Одну аудиторию могут использовать для разных занятий, но одновременно несколько занятий проводить нельзя.

- `Schedule.id_classroom` является внешним ключом, ссылающимся на `Classrooms.id`.

### Subjects и Schedule (Один-ко-Многим)

Один предмет может проводиться несколько раз за день у разных групп, но каждая запись содержит только один предмет.

- `Schedule.id_subject` является внешним ключом, ссылающимся на `Subjects.id`.
