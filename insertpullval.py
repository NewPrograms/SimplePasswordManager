
import psycopg2
from psycopg2 import extensions
from user import User
from encrypt import Encryption
from decrypt import Decrypt
import time
class InsertPull:
     def __init__(self):
         self.encrypt = Encryption()

     def input_password(self, acc_u_name, acc_p_word):
         self.site_name = input("\nAdd a sitename: ")
         self.password = input("Add a password: ")
         self.conn = psycopg2.connect(dbname=f'{acc_u_name}_passwords', user=f'{acc_u_name}', 
                                       password = f"{acc_p_word}", host='127.0.0.1')
         self.cur = self.conn.cursor()
         self.cur.execute(f"INSERT INTO passwords(site_name, passwords) VALUES (%s, %s)", (f"{self.site_name}", f"{self.encrypt.encrypt(self.password)}"))
         self.conn.commit()
         self.cur.close()
         self.conn.close()
         time.sleep(2)
         print("\nThe password has been entered!")
         
     def pull_password(self, acc_u_name, acc_p_word, ans):
        try:
            self.conn = psycopg2.connect(dbname=f'{acc_u_name}_passwords', user=f"{acc_u_name}", password = f'{acc_p_word}', 
                                        host='127.0.0.1')
            self.cur = self.conn.cursor()
            self.cur.execute("SELECT * FROM passwords WHERE site_name = %s", (ans, ))
            self.row = self.cur.fetchone()
            self.conn.commit()
            self.cur.close()
            self.conn.close()
            self.decrypt = Decrypt(self.row[2])
            print("\nPassword: ", self.decrypt.decrypt())

        except TypeError:
            print("You have typed the wrong site name! It doesn't exist!")

     def show_pass(self, acc_u_name, acc_p_word):
        self.conn = psycopg2.connect(dbname=f'{acc_u_name}_passwords', user=f'{acc_u_name}', 
                                     password=f'{acc_p_word}', host='127.0.0.1' )
        self.cur = self.conn.cursor()
        self.cur.execute(f"SELECT site_name FROM passwords;")
        self.vals = self.cur.fetchall()
        self.cur.close()
        self.conn.close()

        for site_name in self.vals:
           print("SiteName: %s \n" % (site_name))