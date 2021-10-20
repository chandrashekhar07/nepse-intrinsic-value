from django import template
import math
FdInterestRate = 10.10   #NICA -  3 months
savingInterestRate = 5.27  #BOK

register = template.Library()

@register.filter(name="calcvalue")
def calcvalue(value, arg):

    dps=value.profit/value.shares_outstanding
    intrensic_value = round(dps/FdInterestRate*100 + value.book_value-dps,3)    

    return arg.replace(str(arg),str(intrensic_value))



@register.filter(name="interest")
def interest(value, arg):

    dps=value.profit/value.shares_outstanding
    interest = round((dps/value.price)*100,3)

    return arg.replace(str(arg),str(interest))

@register.filter(name="difference")
def difference(value,arg):
    difference = round(float(value.price)-float(calcvalue(value, arg)),2)
    return arg.replace(str(arg),str(difference))

@register.filter(name="graham")
def graham(value,arg):

    dps=value.profit/value.shares_outstanding
    graham = round(float(math.sqrt(100/savingInterestRate*dps*1.5*value.book_value)),2)

    return arg.replace(str(arg),str(graham))