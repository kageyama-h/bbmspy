import sqlite3

def connectClient():
	conn=sqlite3.connect("clients.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS client (id INTEGER PRIMARY KEY, firstName text, lastName text, dob integer, phone integer)")
	conn.commit()
	conn.close()

def insertClient(firstNameText,lastNameText,dobText,phoneText):
	print(firstNameText,lastNameText,dobText,phoneText)
	conn=sqlite3.connect("clients.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO client VALUES (NULL,?,?,?,?)",(firstNameText,lastNameText,dobText,phoneText))
	conn.commit()
	conn.close()

def viewClient():
	conn=sqlite3.connect("clients.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM client")
	rows=cur.fetchall()
	conn.close()
	return rows

def searchClient(firstName="",lastName="",dob="",phone=""): # pass empty string to avoid errors 
	# instead of just doing firstName,lastName because it expects 4 peramater
	# write up []
	conn=sqlite3.connect("clients.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM client WHERE firstName=? OR lastName=? OR dob=? OR phone=?", (firstName,lastName,dob,phone))
	rows=cur.fetchall()
	conn.close()
	return rows

def deleteClient(id):
	conn=sqlite3.connect("clients.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM client WHERE id=?", (id,))
	conn.commit()
	conn.close()

def updateClient(id,firstName,lastName,dob,phone):
	conn=sqlite3.connect("clients.db")
	cur=conn.cursor()
	cur.execute("UPDATE client SET firstName=?, lastName=?, dob=?, phone=? WHERE id=?",(firstName,lastName,dob,phone,id))
	conn.commit()
	conn.close()


connectClient()
