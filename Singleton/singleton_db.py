import MySQLdb


class Singleton:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None
    def __call__(self, *args, **kwds):
        if self.instance == None:
            self.instance = self.klass(*args, **kwds)
        return self.instance


@Singleton
class Database:
    connection = None
    def get_connection(self):
        if self.connection is None:
            self.connection = MySQLdb.connect(host="localhost", user="root", passwd="razvan", db="mydatabase")
        return self.connection

db1 = Database().get_connection()
db2 = Database().get_connection()
 
print(db2)
print(db1)