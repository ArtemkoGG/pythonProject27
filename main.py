# Зберігає інформацію про баланс кошельків
wallet = {"USD": 1000, "EUR": 900, "UAH": 25000}

# Зберігає курси конвертації до UAH
exchange_rates_uah = {"USD": 41.3, "EUR": 43.9, "UAH": 1.0}

# Лог для відстеження операцій
transactions = []


def add_currency(currency, amount):
    """Додає валюту в кошелек або оновлює її баланс."""
    if currency in wallet:
        wallet[currency] += amount
    else:
        wallet[currency] = amount

def convert_currency(from_currency, to_currency, amount):
    """Конвертує суму з однієї валюти в іншу за заданими курсами."""
    coefficient_currency = exchange_rates_uah[from_currency] / exchange_rates_uah[to_currency]
    converted_amount = round(amount * coefficient_currency, 2)
    print(coefficient_currency)
    wallet[from_currency] -= amount
    wallet[to_currency] += converted_amount


def display_wallet():
    """Виводить баланс всіх кошельків."""
    for key, value in wallet.items():
        print(f"{key}: {value}")


def display_transactions(last=True, count=3):
    """Виводить історію транзакцій."""


def reset_wallet():
    """ Скидає всі баланси кошельків."""
    for currency in wallet.keys():
        wallet[currency] = 0


# ============================================


def main_process():
    """
    Імплементація функціоналу спілкування з користувачем
    """
    print("\nChoose an option:")
    print("1. Add currency")
    print("2. Convert currency")
    print("3. Display wallet")
    print("4. Display transactions")
    print("5. Reset wallet")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_currency(currency = input("Вкажіть валюту").upper(), amount = input("Вкажіть суму"))
    elif choice == "2":
        convert_currency()

    elif choice == "3":
        display_wallet()

    elif choice == "4":
        ...

    elif choice == "5":
        reset_wallet()

    elif choice == "0":
        exit()

    else:
        ...
main_process()