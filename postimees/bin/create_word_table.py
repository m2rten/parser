import psycopg2
import sys, csv
 

file = "../results/headings.csv"

def main():
	#Define our connection string
	conn_string = "host='localhost' dbname='postimees' user='postgres' password='2104802s'"
 
	# print the connection string we will use to connect
	print ("Connecting to database\n	->%s" % (conn_string))
 
	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)
	conn2 = psycopg2.connect(conn_string)
 
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()
	cursor2 = conn2.cursor()
	print ("Connected!\n")
	
	cursor.execute("SELECT * FROM distinctheadings;")
	for row in cursor:
		sentence = row[1].split(" ")
		for word in sentence:
			try:
				cursor2.execute("INSERT INTO words values(%s, %s)", (row[0], word))
				conn2.commit()
			except psycopg2.DataError:
				print (row[1].encode("utf-8"))
			except psycopg2.InternalError:
				print ("internal error")
				
	cursor.close()
	conn.close()

 
if __name__ == "__main__":
	main()