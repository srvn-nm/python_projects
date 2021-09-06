from texttable import Texttable
l = [['firstName' , 'lastName' , 'age'] , ['Sarvin' , 'Nami' , 19]]
table = Texttable()
table.add_rows(l)
print(table.draw())