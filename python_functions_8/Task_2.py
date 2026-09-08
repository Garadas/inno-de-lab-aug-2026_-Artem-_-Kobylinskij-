import time
from functools import wraps
from typing import Callable, Any

MAX_RENTAL_BATCH_LIMIT = 150.0
PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8
DEFAULT_RETURN_INDEX_BASE = 10.0

# Набор 1 (Стандартный)
tests = [
    [
        {"category": "Action", "total_sales": 4311.85},
        {"category": "Animation", "total_sales": 4656.30},
        {"category": "Children", "total_sales": 3655.55}
    ],
# Набор 2 (С одинаковой выручкой)
    [
        {"category": "Classics", "total_sales": 1200.10},
        {"category": "Comedy", "total_sales": 4000.00},
        {"category": "Documentary", "total_sales": 4000.00}
    ],
# Набор 3 (Единичный элемент)
    [
        {"category": "Drama", "total_sales": 500.00}
    ],
]

def performance_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Декоратор для логирования времени выполнения функции.
    Args:
        func: Функция, которую нужно обернуть.

    Returns:
        Callable[..., Any]: Обернутая функция с логированием времени выполнения.
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = round(end_time - start_time, TIME_DECIMALS)
        print(f"{PERFORMANCE_LOG_PREFIX} Функция '{func.__name__}' выполнена за {elapsed_time:.{TIME_DECIMALS}f} сек.")
        return result
    return wrapper

@performance_logger
def get_sorted_report(genre_data: list[dict[str,str| float]]) -> list[dict[str, float]]:
    """
    Возвращает отсортированный список категорий по выручке.
    Args:
        genre_data: Список словарей с информацией о категориях и их выручке.

    Returns:
        list[dict[str, str | float]]: Отсортированный список категорий.
    """
    return sorted(genre_data, key=lambda item: item["total_sales"], reverse=True)

print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")
for i, data in enumerate(tests, start=1):
        print(f"--- ТЕСТ {i} ---")
        report = get_sorted_report(data)
        print("Топ категорий по выручке:")
        for rank, entry in enumerate(report, start=1):
            print(f"{rank}. {entry['category']}: {entry['total_sales']}")