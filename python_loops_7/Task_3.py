# Конфигурационный словарь, полученный от сервиса инициализации
db_config = {
"connection": {
"host": "production-db.internal",
"port": 5432,
"user": "postgres",
"ssl_setting":{
    "ssl_mode":""
}
}
}
# Ваш код здесь
connection = db_config["connection"]

db_host = connection["host"]

db_port = connection["port"]

db_ssl_settings = connection.get("ssl_setting",{})
db_ssl_mode = db_ssl_settings.get("ssl_mode","verify-full")

connection["user"]="admin"

connection["max_connections"] = "100"

for key, value in connection.items():
    print(f"{key}: {value}")
