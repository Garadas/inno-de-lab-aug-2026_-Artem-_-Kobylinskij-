# Список ролей, переданный в запросе на авторизацию (содержитповторы)
requested_roles = ["guest", "developer", "guest", "admin", "developer", "guest"]
# Набор обязательных ролей для выполнения административных функций
required_admin_roles = {"admin", "security_officer", "audit_manager"}
# Ваш код здесь

unique_roles = set(requested_roles)                       # дедупликация
common_admin = unique_roles & required_admin_roles        # пересечение множеств
missing_admin = required_admin_roles - unique_roles       # недостающие роли
has_security_officer = "security_officer" in unique_roles # проверка через O(1)

# Вывод результатов
print(f"Уникальные запрошенные роли: {unique_roles}")
print(f"Общие административные роли: {common_admin}")
print(f"Недостающие административные роли: {missing_admin}")
print(f"Наличие роли security_officer в запросе: {has_security_officer}")
