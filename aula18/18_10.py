import sqlite3 as sql
import sys

def main(argv):
    db = sql.connect(argv[1])
    result = db.execute("SELECT firstname FROM contacts")
    n = 0
    for row in result:
        print(row[0])
        n = n + 1
    
    print("%d contactos" %n)
    db.close()
main(sys.argv)