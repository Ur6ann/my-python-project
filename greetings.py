from datetime import datetime

# Отримання поточного часу
current_time = datetime.now().strftime("%H:%M:%S")

# Читання імен з файлу
with open("data/names.txt", "r") as file:
    names = file.read().splitlines()

# Персоналізоване привітання для кожного імені
for name in names:
    print(f"Привіт, {name}!")
print(f"Поточний час: {current_time}")

