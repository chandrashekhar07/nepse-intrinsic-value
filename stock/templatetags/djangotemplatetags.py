from django import template
import math
FdInterestRate = 10.05 # avg
savingInterestRate = 5.86  # BOK

register = template.Library()


@register.filter(name="calcvalue")
def calcvalue(value, arg):
    dps = 0
    book_value = 0
    if value.category == "Microfinance":
        if value.eps <= 20:
            dps = value.eps
        else:
            dps = (value.eps+20)/2
                
    else:
        dps = 0.8*value.eps 
    
    book_value = value.book_value * (1+FdInterestRate/100) +(value.eps-dps)

    intrensic_value = round(dps/FdInterestRate*100 + book_value, 3) + value.roe/savingInterestRate

    return arg.replace(str(arg), str(round(intrensic_value,2)))


@register.filter(name="interest")
def interest(value, arg):

    dps = 0
    if value.category == "Microfinance":
        if value.eps <= 20:
            dps = value.eps
        else:
            dps = (value.eps+20)/2
    else:
        dps = 0.8*value.eps

    interest = round((dps/value.price)*100, 3)

    return arg.replace(str(arg), str(interest))


@register.filter(name="difference")
def difference(value, arg):
    difference = round(float(value.price)-float(calcvalue(value, arg)), 2)
    return arg.replace(str(arg), str(difference))


@register.filter(name="graham")
def graham(value, arg):
    dps = 0
    if value.category == "Microfinance":
        if value.eps <= 20:
            dps = value.eps
        else:
            dps = (value.eps+20)/2
    else:
        dps = 0.8*value.eps

    book_value = value.book_value * (1+FdInterestRate/100) + (value.eps-dps)

    graham = round(
        float(math.sqrt(100/savingInterestRate*dps*1.5*book_value)), 2)

    return arg.replace(str(arg), str(graham))
