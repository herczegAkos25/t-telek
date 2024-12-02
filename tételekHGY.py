date_list = ['1983-06-15', '1991-12-07', '1987-03-24', '2001-08-19', '2015-04-03', '1980-11-21', '1999-02-28', '2008-09-12', '1995-01-05', '2020-07-09',
             '1986-10-30', '1993-05-14', '2011-06-26', '1989-12-18', '2005-03-11', '2018-09-01', '1997-07-20', '2012-11-03', '2023-01-22', '1990-04-09']

date_2000=0


for date in date_list:
    if date <= "2000-01-01":
        date_2000+=1
    if date[5:7] == '09':
        print(date)

last_date = date_list[0]
for date in date_list:
    if date > last_date:
        last_date = date

print("2000 előtti dátumok száma: ",date_2000)
print("Legutolsó év a dátumok között: ",last_date[:4])