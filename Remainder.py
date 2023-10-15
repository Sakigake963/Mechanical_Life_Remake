import SQLiteDB

try:
    SQLiteDB.init_db()
except:
    pass

SQLiteDB.getFirstDate()
SQLiteDB.insertData()
SQLiteDB.showAll()