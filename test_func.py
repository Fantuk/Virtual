import pytest

from credit import credit_calc

@pytest.mark.parametrize("amount, bid, term, expected", [
    (10000, 10, 6, [
        {'date': 1, 'overpayment': 83.33, 'payment': 1666.67, 'fee': 1750.0, 'remainder': 8333.33},
        {'date': 2, 'overpayment': 69.44, 'payment': 1666.67, 'fee': 1736.11, 'remainder': 6666.66},
        {'date': 3, 'overpayment': 55.56, 'payment': 1666.67, 'fee': 1722.23, 'remainder': 4999.99},
        {'date': 4, 'overpayment': 41.67, 'payment': 1666.67, 'fee': 1708.34, 'remainder': 3333.32},
        {'date': 5, 'overpayment': 27.78, 'payment': 1666.67, 'fee': 1694.45, 'remainder': 1666.65},
        {'date': 6, 'overpayment': 13.89, 'payment': 1666.67, 'fee': 1680.56, 'remainder': 0}]),
    ])
def test_1(amount, bid, term, expected):
    assert credit_calc(amount, bid, term) == expected


@pytest.mark.parametrize("amount, bid, term, expected", [
    (-1, 11, 10, "Amount must be greater than zero"),
    ("a", 11, 10, "Amount must be a number"),
    ("", 11, 10, "Amount must be a number"),
    (False, 11, 10, "Amount must be a number")
])
def test_2(amount, bid, term, expected):
    assert credit_calc(amount, bid, term) == expected