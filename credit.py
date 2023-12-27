import pytest
from prettytable import PrettyTable

def validate(amount, bid, term):
    try:
        if type(amount) == bool:
            return "Amount must be a number"
        float(amount)
        if amount < 0:
            return "Amount must be greater than zero"
        
    except ValueError:
        return "Amount must be a number"
    except TypeError:
        return "Amount must be a number"

    try:
        if type(bid) == bool:
            return "Bid must be a number"
        float(bid)
        if bid < 0:
            return "Bid must be greater than zero"
    except ValueError:
        return "Bid must be a number"
    except TypeError:
        return "Bid must be a number"
    
    try:
        if type(term) == bool:
            return "Term must be a number"
        int(term)
        if term < 0:
            return "Term must be greater then zero"
    except ValueError:
        return "Term must be a number"
    except TypeError:
        return "Term must be a number"
    return True    


def credit_calc(amount, bid, term):
    
    validation = validate(amount, bid, term)

    if validation == True:

        month = 0
        result = []

        debt = amount / term
        for i in range (term):
            percent = amount * bid / 100 / 12
            sum_payment = percent + debt
            remainder = amount - debt

            percent=round(percent, 2)
            sum_payment = round(sum_payment, 2)
            debt = round(debt, 2)
            remainder = round(remainder, 2)
            amount = remainder

            if remainder < 0.05:
                remainder = 0

            month +=1

            result.append({
            "date": month,
            "overpayment": percent,
            "payment": debt,
            "fee": sum_payment,
            "remainder": remainder
        })
    else:
        return validation
    return result

def table(result):

    mytable = PrettyTable()
    mytable.field_names = ["Month", "Overpayment", "Payment", "Fee", "Remainder"]

    for item in result:
        mytable.add_row(item.values())
    return mytable