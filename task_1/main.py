

def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                parts = line.split(",")
                salary = int(parts[1].strip())
                total += salary
                count += 1

        average = total / count
        return total, average

    except FileNotFoundError:
        print("Немає файла - немає зарплати:)")
        return 0, 0
    
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати---> {total}, Середня заробітна плата---> {average}")