import csv 

companies = []
sales = []

with open('carSale.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        companies.append(row[0])
        sales.append([int(x.replace(",", ""))for x in row [1:]])

monthly_sum = [sum(x) for x in zip(*sales)]

yearly_sum = {}
for i in range(len(companies)):
    yearly_sum[companies[i]] = sum(sales[i])

print("Monthly Sales:", monthly_sum)
print("Yearly sales:", yearly_sum)
for company, sales in yearly_sum.items():
    print(company, sales)