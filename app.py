import psycopg2
"""
self - instance
"""
class DbConnect:
    def __init__(self):   #constructor
        self.con = psycopg2.connect(database='postgres',
                            user='postgres',
                            password='toor',
                            host='localhost')
        print(self.con)
        self.get_date()

    def get_date(s):
        query = "select * from mock_data"
        cursor = s.con.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
        print(data)
        s.con.commit()

    def __del__(self):
        print("Conpleted")
        self.con.close()

psql = DbConnect()
psql.get_date()
del psql