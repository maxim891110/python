time = int(input("Введите время в секундах "))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = (time % 3600) % 60
print(f"Время в формате чч:мм:сс   {hours:>02} : {minutes:>02} : {seconds:>02}")

