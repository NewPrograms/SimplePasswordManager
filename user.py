import psycopg2
from create import Create
class User():
    # This is the user class
    def __init__(self, acc_u_name, acc_p_word):
        self.acc_u_name = acc_u_name
        self.acc_p_word = acc_p_word
        self.active = True
        self.create = Create(self.acc_u_name, self.acc_p_word)

    def auth(self):
        """ This used in order to autheticate the user while also registering it if not registered yet"""
        try:
            if ';' in self.acc_u_name:
                print("\n\nNo semicolons allowed!")
                self.active = False
            else:
                self.conn = psycopg2.connect(dbname=f"{self.acc_u_name}_passwords", user=f"{self.acc_u_name}", password=f"{self.acc_p_word}", host="127.0.0.1")
                self.cur = self.conn.cursor()
                self.cur.execute(f"SELECT * FROM passwords;")
                self.cur.fetchone()
                self.cur.close()
                self.conn.close()

        except:
            self.create.create_user()
            self.create.create_db()
            self.create.create_table() 
            print("We've already registered you")

            














             