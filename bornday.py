import datetime
RightBirthDay=datetime.date(1799,6,6)
print(RightBirthDay, "  ", type(RightBirthDay))

year=int(input("год рождения Пушкина  "))

if RightBirthDay.year==year:

    date_str = input("День рождения Пушкина  (dd/mm/yyyy)\n")
    AskDate = datetime.datetime.strptime(date_str, '%d/%m/%Y').date()
    if AskDate == RightBirthDay:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год рождения')
