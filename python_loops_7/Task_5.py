# Поток данных телеметрии от серверов кластера
system_telemetry = [
("srv_01", 12.5, 64, "online"),
("srv_02", 85.0, 92, "online"),
("srv_03", 0.0, 0, "offline"),
("srv_04", 45.2, 78, "online"),
("srv_05", 95.1, 99, "online")
]
# Реализация конвейера агрегации метрик
# Ваш код здесь
active_names = []
cpu_loads = []
ram_usages = []

for node_name, cpu_load, ram_usage, status in system_telemetry:
    if status != "offline":          # фильтрация
        active_names.append(node_name)
        cpu_loads.append(cpu_load)
        ram_usages.append(ram_usage)

print(f"Активные узлы в сети: {active_names}")

#метрики
total_active = len(active_names)
avg_cpu = sum(cpu_loads) / total_active if total_active > 0 else 0.0
max_ram = max(ram_usages) if ram_usages else 0


result = {
    "active_nodes_count": total_active,
    "metrics": {
        "average_cpu": round(avg_cpu, 2),
        "max_ram": max_ram
    }
}

print(f"Итоговый отчет телеметрии: {result}")
