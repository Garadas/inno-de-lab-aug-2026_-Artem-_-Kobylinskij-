# Исходная необработанная строка из источника данных
raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "
# Ваш код здесь
cleaned_user_record = [s.strip() for s in raw_user_record.split(';')] #из строки в массив строк и убираем лишние пробелы
cleaned_user_record[0] =f"UID-{cleaned_user_record[0]}" #добавляем UID через f-строку
cleaned_user_record[1] = cleaned_user_record[1].replace('_',' ').title() #приводим фио к нужному формату
cleaned_user_record[2]= cleaned_user_record[2].upper() #в верхний регистр
cleaned_user_record[3]= cleaned_user_record[3].lower() #в нижний регистр
final_user_record=" | ".join(cleaned_user_record) #объединение строк в 1
print("Нормализированная запись: " + final_user_record)