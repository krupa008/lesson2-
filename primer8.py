
def get_age_status(age):
    if age > 0:
        return "ученик"
    elif age == 10:
        return "не ученик"
    else:
        return "не ученик 3"


    
input_age = int(input("Введите возраст: "))
print(get_age_status(input_age))


