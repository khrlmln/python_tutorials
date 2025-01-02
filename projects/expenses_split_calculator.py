def calculate_split(total_amount: float, number_of_people: int, currency: str) -> None:
    if number_of_people < 1:
        raise ValueError("Number of people must be greater than one.")

    share_per_person: float = total_amount / number_of_people

    print(f"Total expenses: {currency}{total_amount:,.2f}")
    print(f"Number of people: {number_of_people}")
    print(f"Amount each person should pay: {currency}{share_per_person:,.2f}")


def main() -> None:
    try:
        total_amount: float = float(input("Enter total bill amount: "))
        number_of_people: int = int(input("Enter total number of people: "))
        currency: str = input("Enter currency symbol (default ₹): ") or "₹"

        if total_amount < 0 or number_of_people < 0:
            raise ValueError("Monthly income and tax rate must be non-negative.")

        calculate_split(total_amount, number_of_people, currency)

    except ValueError as err:
        print(f"Error: {err}. Please enter valid values.")


if __name__ == "__main__":
    main()
