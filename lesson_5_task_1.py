#Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартал (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю
# прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

company_list = set()
company_attr = namedtuple('Company', ['name', 'quarters', 'revenue'])
number = int(input("Введите число предприятий: "))
total_revenue = 0
for i in range(1, number+1):
    revenue = 0
    quarters = []
    name = input(f'Название {i}-го предприятия: ')
    for j in range(4):
        quarters.append(float(input(f'Прибыль за {j+1}-й квартал = ')))
        revenue += quarters[j]
    company_info = company_attr(name=name, quarters=tuple(quarters), revenue=revenue)
    company_list.add(company_info)
    total_revenue += revenue
average_revenue = total_revenue / number
print(f'Средняя прибыль предприятия за год: {average_revenue}')
print(f'Предприятия с прибылью выше среднего:')
for company_attr in company_list:
    if company_attr.revenue > average_revenue:
        print(f'Компания {company_attr.name} заработала {company_attr.revenue}')
print(f'Предприятия с прибылью ниже среднего:')
for company_attr in company_list:
    if company_attr.revenue < average_revenue:
        print(f'Компания {company_attr.name} заработала {company_attr.revenue}')
