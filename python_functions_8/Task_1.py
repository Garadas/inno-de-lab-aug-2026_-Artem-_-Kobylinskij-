MAX_RENTAL_BATCH_LIMIT = 150.0
PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8
DEFAULT_RETURN_INDEX_BASE = 10.0

def calculate_rental_batch(
    quantity: int,
    rental_rate: float,
    discount:float = 0.0
    ) -> tuple[float, bool]:
    """
    Считает сумму партии аренды и проверка лимита.
    Args:
        quantity (int): The number of items to rent.
        rental_rate (float): The rate per item.
        discount (float, optional): The discount to apply. Defaults to 0.0.

    Returns:
        float: The calculated rental batch.
    """
    final_sum = quantity * rental_rate * (1 - discount)
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT
    return final_sum, is_limit_exceeded 

parties = [
    ("Academy Dinosaur", 30, 2.99, 0.0),
    ("Affair Prejudice", 40, 4.99, 0.10),
    ("Agent Truman", 10, 1.99, 0.0),
    ("African Egg", 50, 3.50, 0.20), 
    ]

print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===")
for i, party in enumerate(parties, start=1):
    name, quantity, rental_rate, discount = party
    final_sum, is_limit_exceeded = calculate_rental_batch(quantity, rental_rate, discount)
    limit_status = "Превышен лимит" if is_limit_exceeded else "Лимит не превышен"
    print(f"Партия {i} ({name}): cумма {final_sum:.2f}$. Превышение лимита: {is_limit_exceeded}")