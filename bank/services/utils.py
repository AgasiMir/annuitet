def annuitet(money: int, percent: int, year: int) -> int:
    return round(money * (1 + percent / 100) ** year)


def proper_annuitet(amount: int) -> str:
    return f"{amount:_}".replace('_', ' ')
