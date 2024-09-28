def calculate_split(total_amount: float, number_of_people: int, currency: str):
    if number_of_people < 1:
        raise ValueError('Number of people must be greater than one')

    share_per_person = total_amount / number_of_people
    print(f'Total expense: {currency}{total_amount}')
    print(f'Number of people: {number_of_people:}')
    count = 0

    while number_of_people > 0:
        count += 1
        person_count = f'Person{count}'
        percent_per_person = int(input(f"What percentage should {person_count} take: "))
        percent_conversion = percent_per_person / 100
        print(f"{person_count} should take {percent_conversion}% of {currency}{total_amount:,.2f}")
        calculation = percent_conversion * total_amount
        print(f"{person_count} share: {currency}{calculation:,.2f}")
        number_of_people -= 1


def main() -> None:
    while True:
        try:
            total_amount = float(input("Enter the total amount of the expense: "))
            number_of_people = int(input("Number of persons: "))
            calculate_split(total_amount, number_of_people, currency='$')
            break
        except ValueError as e:
            print(f'Error: {e}')


if __name__ == '__main__':
    main()


