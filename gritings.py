from datetime import datetime

# Запит імені користувача
name = input("Введіть ваше ім'я: ")

# Отримання поточного часу
current_time = datetime.now().strftime("%H:%M:%S")

# Персоналізоване привітання
print(f"Привіт, {name}!")
print(f"Поточний час: {current_time}")
