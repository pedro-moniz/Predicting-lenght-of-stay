pip install psycopg2
import psycopg2
#establishing the connection
conn = psycopg2.connect(
   database="mimic", user='postgres', password='..Aberdeen22', host='localhost', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

sqldata = "select row_id, subject_id \
      from mimiciii.admissions"
#Executing an MYSQL function using the execute() method
cursor.execute(sqldata)

numRows = cursor.rowcount
print("number of rows fetched =", numRows)
# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

records = cursor.rowcount
print(records)

#Close cursor 
cursor.close()
#Closing the connection
conn.close()