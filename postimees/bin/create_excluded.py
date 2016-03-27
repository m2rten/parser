import psycopg2
import sys, csv
 

filename = "excluded.txt"

def main():
	#Define our connection string
	conn_string = "host='localhost' dbname='postimees' user='postgres' password='2104802s'"
 
	# print the connection string we will use to connect
	print ("Connecting to database\n	->%s" % (conn_string))
 
	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)
 
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()
	print ("Connected!\n")
	
	f = open(filename, encoding = "utf-8")
	for line in f.readlines():
		print (line.strip().encode("utf-8"))
		cursor.execute("INSERT INTO excluded values(%s, %s)", (2, line.strip()))
		conn.commit()
	cursor.close()
	conn.close()
	print ("inserted ?")

 
if __name__ == "__main__":
	main()