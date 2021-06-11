import psycopg2
from psycopg2 import extensions
import time
class Create:
     
     def __init__(self, u_name, p_word):
        self.acc_u_name = u_name
        self.acc_p_word = p_word

     def create_user(self):
        conn = psycopg2.connect(dbname="", user="", password="", host="127.0.0.1")
        cur = conn.cursor()
        cur.execute(f"CREATE USER {self.acc_u_name} WITH PASSWORD '{self.acc_p_word}'")
        conn.commit()

        cur.close()
        conn.close()

     def create_db(self):

            auto_commit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
            self.conn = psycopg2.connect(dbname='', user=f'', 
                                        password=f'09092004ni', host='127.0.0.1' )
            self.conn.set_isolation_level(auto_commit)
            self.cur = self.conn.cursor()
            self.cur.execute(f'ALTER ROLE {self.acc_u_name} CREATEDB')
            self.cur.execute(f'CREATE DATABASE {self.acc_u_name}_passwords')
            self.cur.execute('ALTER DATABASE {}_passwords OWNER TO {}'.format(self.acc_u_name, self.acc_u_name))
            self.cur.close()
            self.conn.close()

     def create_table(self):
        self.conn = psycopg2.connect(dbname=f'{self.acc_u_name}_passwords', user=f'{self.acc_u_name}', 
                                     password=f'{self.acc_p_word}', host='127.0.0.1' )
        self.cur = self.conn.cursor()
        self.cur.execute(f'CREATE TABLE passwords(id bigserial PRIMARY KEY, site_name varchar(50) NOT NULL, passwords varchar(50) NOT NULL);')
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        print("Database Made!")

class Delete:
     def __init__(self, u_name, p_word, will_del):
        self.will_del = will_del
        self.acc_u_name = u_name
        self.acc_p_word = p_word
        self.deleted = True
     def delete_table(self):
        
            self.conn = psycopg2.connect(dbname=f'{self.acc_u_name}_passwords', user=f'{self.acc_u_name}', 
                                          password=f'{self.acc_p_word}', host='127.0.0.1' )
            self.cur = self.conn.cursor()
            self.cur.execute("SELECT site_name FROM passwords WHERE site_name = %s;" % (f"'{self.will_del}'"))
            self.values = self.cur.fetchone()
            self.cur.execute("DELETE FROM %s WHERE %s = '%s'" % ("passwords", "site_name", self.will_del))
            self.conn.commit()
            self.cur.close()
            self.conn.close()
              
            if self.values != None:
               time.sleep(3)
               print("\nDeleted succesfully")
               self.deleted = True
            
            else:
               time.sleep(3)
               print("\nWrong site_name!")
               self.deleted = False 
              
             