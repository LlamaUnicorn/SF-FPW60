# Запишите вместо вопросительных знаков выражение, которое вернет True,
# когда каждое из чисел А и В нечетное.


def are_both_odd(a, b):
    return a % 2 != 0 and b % 2 != 0


are_both_odd(3, 5)
