import csv, time

transactions = open('transactions.csv')
reader = csv.reader(transactions, delimiter=';')

transactionsConverted = open('transactionsConverted.csv', 'w')
writer = csv.writer(transactionsConverted)

# Write header row
writer.writerow(['Date','Payee','Category','Memo','Outflow','Inflow'])

reader.next()

for row in reader:
  # print row
  date = time.strftime('%d/%m/%Y', time.strptime(row[0], '%d-%m-%Y')) # DD/MM/YYYY
  payee = ''
  category = ''
  memo = row[2]

  # Check if the transaction is 'D' (outflow) or 'C' (inflow)
  if row[5] == 'D':
    outflow = row[6]
    inflow = '0'
  elif row[5] == 'C':
    outflow = '0'
    inflow = row[6]

  writer.writerow([date, payee, category, memo, outflow, inflow])

transactionsConverted.close()