def birthday_ranges(birthdays, ranges):
    list_of_number_of_birthdays = []
    for start, end in ranges:
        number = 0
        for current_birthday in birthdays:
            if current_birthday in range(start, end):
                number += 1
        list_of_number_of_birthdays.append(number)

    return list_of_number_of_birthdays
