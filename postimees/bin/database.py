import psycopg2
import sys, csv
 

file = "../results/headings.csv"

class database:
	
	def __init__(self, cf):
		line = 'jehuu'
		self.conn_string = "host='"+ cf.host+ "' dbname='"+cf.dbname+"' user='"+cf.user+"' password='"+cf.password+"'"

		print (self.conn_string)
 
	def connect (self):
		self.conn = psycopg2.connect(self.conn_string)
		# conn.cursor will return a cursor object, you can use this cursor to perform queries
		self.cursor = self.conn.cursor()
		
	def insertHeading(self, heading, rank, dt, tm):
			self.cursor.execute("INSERT INTO headings (heading, rank, date, time) VALUES (%s, %s, %s, %s)",(heading, rank, dt, tm))
			self.conn.commit()
	
	def close(self):
		self.conn.close()
	
if __name__ == "__main__":
	main()