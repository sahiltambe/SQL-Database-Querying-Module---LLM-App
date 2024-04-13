import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('Iron Man','AI','A',99)''')
cursor.execute('''Insert Into STUDENT values('Ant-man','Quantum','B',85)''')
cursor.execute('''Insert Into STUDENT values('Hulk','Gamma','C',90)''')
cursor.execute('''Insert Into STUDENT values('Spider-Man','Web','D',75)''')
cursor.execute('''Insert Into STUDENT values('Thor','Hammer','A',100)''')
cursor.execute('''Insert Into STUDENT values('Clint Barton','Arrow','A',60)''')
cursor.execute('''Insert Into STUDENT values('Black Panther','Vakanda','B',90)''')
cursor.execute('''Insert Into STUDENT values('Doctor Strange','Magic','C',80)''')
cursor.execute('''Insert Into STUDENT values('Loki','Villain','D',35)''')
cursor.execute('''Insert Into STUDENT values('Vision','Stone','A',86)''')


## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()