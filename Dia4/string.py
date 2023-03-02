concatunate = ['Thirty', 'Days', 'Of', 'Python']
full_sentence = ' '.join(concatunate)
print(full_sentence)

string = ['Coding', 'For', 'All']
string_sentence = ' '.join(string)
print(string)

company = 'Coding For All'
print(company)
print(len(company))
print(company.upper)
print(company.lower)
print(company)

remove_coding = company[4:14]
print(remove_coding)

print(company.index('Coding'))
print(company.find('Coding'))
print(company.replace('Coding', 'Python'))
sentense = 'Python for Everyone'
print(company.replace('Everyone', 'All'))
print(company.split())
first_letter = company[5]
print(first_letter)
last_letter = company[-5]
print(last_letter)
tenth_index = company[10]
print(tenth_index)
print(company.index('C'))
print(company.index('F'))
last_1 = '1'
print(company.find(last_1, 13))
