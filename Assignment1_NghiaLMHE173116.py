import pandas as pd
import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-G8TILI6O;'
                      'Database=Chicago_DB;'
                      'Trusted_Connection=yes;')

# Problem 1: Find the total number of crimes recorded in the CRIME table.

cursor = conn.cursor()

cursor.execute('''
                select count(ID) from Crimes_2001_to_Present
                ''')
result = cursor.fetchone()[0]                
print("Total number of crimes recorded:", result)

conn.commit() 
print()

# Problem 2: List community areas with per capita income less than 11000.

df = pd.read_sql_query('''
                SELECT [Community Area Number], [COMMUNITY AREA NAME], [PER CAPITA INCOME ] 
                FROM Census_Data
                WHERE [PER CAPITA INCOME ] < 11000
                ''', conn)

print(df)
print(type(df))
print()

# Problem 3: List all case numbers for crimes involving minors?

df1 = pd.read_sql_query('''
                SELECT DISTINCT [Case Number] FROM Crimes_2001_to_Present 
                WHERE [Description] LIKE '%MINOR%'
                ''', conn)

print(df1)
print(type(df1))
print()

# Problem 4: List all kidnapping crimes involving a child?(children are not considered minors for the purposes of crime analysis)

df2 = pd.read_sql_query('''
                SELECT DISTINCT [Case Number], [Date], [Primary Type], [Description] 
                FROM Crimes_2001_to_Present
                WHERE [Primary Type] LIKE 'KIDNAPPING'
                ''', conn)

print(df2)
print(type(df2))
print()

# Problem 5: What kind of crimes were recorded at schools?

df3 = pd.read_sql_query('''
                SELECT DISTINCT [Primary Type], [Location Description] FROM Crimes_2001_to_Present
                WHERE [Location Description] LIKE '%SCHOOL%'
                ''', conn)

print(df3)
print(type(df3))
print()

# Problem 6: List the average safety score for all types of schools.

df4 = pd.read_sql_query('''
                SELECT [Elementary, Middle, or High School], AVG([Safety Score]) [Average_Safety Score] 
                FROM Chicago_Public_Schools
                GROUP BY [Elementary, Middle, or High School]
                ''', conn)

print(df4)
print(type(df4))
print()

# Problem 7: List 5 community areas with highest % of households below poverty line.

df5 = pd.read_sql_query('''
                SELECT TOP 5 [COMMUNITY AREA NAME], [PERCENT HOUSEHOLDS BELOW POVERTY]
                FROM Census_Data 
                ORDER BY [PERCENT HOUSEHOLDS BELOW POVERTY]
                ''', conn)

print(df5)
print(type(df5))
print()

# Problem 8: Which community area(number) is most crime prone?

df6 = pd.read_sql_query('''
                SELECT TOP 1 [Community Area] ,COUNT([Community Area]) [frequency]
                FROM Crimes_2001_to_Present
                GROUP BY [Community Area]
                ORDER BY COUNT([Community Area]) DESC
                ''', conn)

print(df6)
print(type(df6))
print()

# Problem 9: Use a sub-query to find the name of the community area with highest hardship index.

df7 = pd.read_sql_query('''
                SELECT [COMMUNITY AREA NAME] FROM  Census_Data 
                WHERE [HARDSHIP INDEX] = (
                    SELECT MAX([HARDSHIP INDEX]) FROM Census_Data
                    )
                ''', conn)

print(df7)
print(type(df7))
print()

# Problem 10: Use a sub-query to determine the Community Area Name with most number of crimes?

df8 = pd.read_sql_query('''
                SELECT TOP 1 [COMMUNITY AREA NAME] FROM Census_Data
                WHERE [Community Area Number] = (
                    SELECT TOP 1 [Community Area] FROM Crimes_2001_to_Present 
                    GROUP BY [Community Area]
                    ORDER BY COUNT([Community Area]) DESC
                    )
                ''', conn)

print(df8)
print(type(df8))
print()
