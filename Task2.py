
import re

from typing import Callable



def generator_numbers(text: str) -> float:
    pattern = r"\s\d+\.\d+\s"
    for match in re.finditer(pattern, text):
        yield float(match.group())



def sum_profit(text: str) -> (Callable [[str],float]):
    salary = 0.0
    for number in generator_numbers(text):
        salary += number
    return salary

#text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
#total_income = sum_profit(text)
#print(f"Загальний дохід: {total_income}")

from_user = input("Введіть речення:")
text = from_user.strip()
total_income = sum_profit(text)
print(f"Загальний дохід: {total_income}")
