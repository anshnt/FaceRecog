import psycopg2

conn = psycopg2.connect(database="testdb", user="postgres", password="root", host="127.0.0.1", port="5432")

if conn:
    print("Opened database successfully")