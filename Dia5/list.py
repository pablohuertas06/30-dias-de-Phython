emptyList = []
household_items = ['coffee', 'cereals', 'pots', 'air-conditions', 'chairs']
length = len(household_items)
print(length)
first_item = household_items[0]
second_item = household_items[1]
third_item = household_items[2]
print(first_item)
print(second_item)
print(third_item)
mixed_data_types = ['Pablo', 34, 4.5, False, {'Huertas': '10H'}]
print(mixed_data_types)
it_companies = ['facebook', 'google', 'microsoft', 'apple', 'INM', 'oracle', 'amazon']
print(it_companies)
print(len(it_companies))
first_it_companies = it_companies[0]
second_it_companies = it_companies[4]
third_it_companies = it_companies[-2]
print(first_it_companies)
print(second_it_companies)
print(third_it_companies)
it_companies[1] = 'melón'
print(it_companies)
it_companies.append('sandía')
print(it_companies)
it_companies.insert(3, 'pera')
print(it_companies)
mayúscula = it_companies[2].upper()
print(mayúscula)
joiningn = '#,'.join(it_companies)
print(joiningn)
does_it_exist = 'manzana' in it_companies
print(does_it_exist)
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)
first_three_items = it_companies[0:3]
print(first_three_items)
last_three_items = it_companies[5:]
print(last_three_items)
middle_item = it_companies[4:3]
print(middle_item)

