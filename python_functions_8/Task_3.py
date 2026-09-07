from typing import Any

MAX_RENTAL_BATCH_LIMIT = 150.0
PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8
DEFAULT_RETURN_INDEX_BASE = 10.0


def calculate_overdue_fine(
    movie_title: Any,
    days_overdue: Any,
    fine_rate: Any,
) -> tuple[float, float] | None:


    try:
        numeric_days = float(days_overdue)
        total_fine = numeric_days * fine_rate
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days
 
        print(
            f"Фильм: '{movie_title}' | "
            f"Итоговый штраф: {total_fine}$ | "
            f"Индекс: {return_index}"
        )
        return total_fine, return_index
 
    except TypeError as e:
        print(f"[ОШИБКА ТИПА] Некорректный тип данных для '{movie_title}': {e}")
    except ValueError as e:
        print(f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для '{movie_title}': {e}")
    except ZeroDivisionError as e:
        print(f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для '{movie_title}': {e}")
    finally:
        print("--- Проверка транзакции возврата завершена ---")
 

print("=== ПРОВЕРКА ВОЗВРАТОВ ===")
 
calculate_overdue_fine("Matrix", 5, 1.5)
calculate_overdue_fine("Inception", "пять", 2.0)
calculate_overdue_fine("Avatar", 0, 2.5)
calculate_overdue_fine("Interstellar", [3, ], 3.0)