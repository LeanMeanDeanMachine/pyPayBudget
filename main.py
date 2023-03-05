# input
from re import X

import pit as pit

tax_rate = [.0, .90, .88, .78, .76, .67, .65, .63]

hours_day = input("How many hours are you working a day: ")
hours_day = int(hours_day)

days_week = input("How many days are you working a week: ")
days_week = int(days_week)

print(" ")
################################
tax_tuple = (.0, .90, .88, .78, .76, .67, .65)
income_max = (9699, 39474, 84200, 160725, 204100, 510300, 999999999)
tax_brackets = {
    0: (0, 9699),
    10: (9700, 39474),
    12: (39475, 84200),
    22: (84200, 160725),
    24: (160725, 204100),
    32: (204100, 510300),
    35: (510300, 999999999999)
}

################################

reg_hourly_wage = input("What is your hourly wage: $")
reg_hourly_wage = float(reg_hourly_wage)
ot_rate = reg_hourly_wage * 1.5
print(" ")
print(f"your Overtime wage is: {ot_rate} per hour")
print(" ")

# Time Variables and Values


hours_week = hours_day * days_week

if hours_week > 40:
    hours_ot = hours_week - 40
    hours_week = 40
else:
    hours_ot = 0

print(f"Hours per Day: {hours_day}     Days per Week: {days_week}")
print(
    f"Regular Hours per Week: {hours_week}     OT Hours per Week: {hours_ot}     Hours per Week: {hours_week + hours_ot}")
print(" ")

# Monetary Variables and Values

tax_rate = tax_rate[0]
reg_hourly_wage_gross = reg_hourly_wage * hours_week
ot_wage_gross = hours_ot * ot_rate
gross = reg_hourly_wage_gross + ot_wage_gross
net = gross * tax_rate
yearly_net = net * 52
yearly_gross = gross * 52

if gross * 52 < income_max[0]:
    tax_rate = tax_tuple[0]
elif gross * 52 <= income_max[1]:
    tax_rate = tax_tuple[1]
elif gross * 52 <= income_max[2]:
    tax_rate = tax_tuple[2]
elif gross * 52 <= income_max[3]:
    tax_rate = tax_tuple[3]
elif gross * 52 <= income_max[4]:
    tax_rate = tax_tuple[4]
elif gross * 52 <= income_max[5]:
    tax_rate = tax_tuple[5]
else:
    tax_rate = tax_tuple[6]

yearly_net = yearly_gross * tax_rate

hourly_wage_net = reg_hourly_wage_gross * tax_rate

# Output

print(f"Hourly Wage: ${reg_hourly_wage}/Hr     Overtime Rate: ${ot_rate}/Hr")
print(" ")

gross = reg_hourly_wage_gross + ot_wage_gross
net = gross * tax_rate

print(f"Weekly Net: {net:.2f}")
print(f'Weekly Gross: {gross:.2f}')
print(" ")

print(f"Monthly Net: {net * 4:.2f} ")
print(" ")

print(f"Yearly Net: {yearly_net:.2f}")
print(f"Yearly Gross: {yearly_gross:.2f}")

### Bills, Personal, Investing ###

Bills_Budget = net * .5
Personal_Budget = net * .20
Investing_Budget = net * .30

print(f"Bills Budget: {Bills_Budget:.2f}")
print(f"Personal Budget: {Personal_Budget:.2f}")
print(f"Investing Budget: {Investing_Budget:.2f}")
