from user import User as u
from insertpullval import InsertPull
import time
from create import Delete
class PasswordManager:
    # This is the main program
    def __init__(self):
       # User Accounts 
        self.acc_u_name = input("Username: ")
        self.acc_p_word = input("Password: ")
        self.user = u(self.acc_u_name, self.acc_p_word)
        self.active = True
        self.insert_pull = InsertPull()
        
    def __run__(self):
        while self.active == True:
            self.user.auth()
            if self.user.active == False:
                self.active = False
            else:
                self.list_choices()
        
    def list_choices(self):
        time.sleep(2)
        print("\n\nEntering User...\n\n")
        time.sleep(3)
        print("Here are the list of choices:\n"
                + "1. Find password.\n "
                + "2. Add a new password.\n"
                + "3. Delete password.\n "
                + "4 End program.")
        time.sleep(5)
        self.choices()

    def choices(self):
        self.ans = input("Choose: ")
        if self.ans == "1":
            self.find_pass()

        elif self.ans == "2":
            self.add_password()

        elif self.ans == "3":
            self.delete_pass()

        elif self.ans == "4":
            self.active = False

        else:
            print("Invalid command! Try again")
            self.list_choices()

    def add_password(self):
        """ This is a function meant to add a new password."""

        ans = input("Are you sure you want to add a password(Y/N)?")
   
        if ans.lower() == 'y':
            time.sleep(2)
            self.insert_pull.input_password(self.acc_u_name, self.acc_p_word)
            
        else:
            self.list_choices()

    def find_pass(self):
        """ This is a function meant to find the password """

        self.insert_pull.show_pass(self.acc_u_name, self.acc_p_word)
        ans = input("Enter the site_name: ")

        print("\nFetching Password....\n")
        
        time.sleep(2)

        self.insert_pull.pull_password(self.acc_u_name, self.acc_p_word, ans)

        time.sleep(2)
        print("\nReturning to menu")
        time.sleep(5)

        self.list_choices()

    def delete_pass(self):
        """ This is a function meant to delete the passwords """

        print("Here are the list of site that you can delete! ")
        self.insert_pull.show_pass(self.acc_u_name, self.acc_p_word)
        self.to_del = input("Which password do you want to delete? ")
        self.will_del = Delete(self.acc_u_name, self.acc_p_word, self.to_del)
        self.will_del.delete_table()

        if self.will_del.deleted == True:
            self.list_choices()
         
        else: 
            self.active = False
        
if __name__ == '__main__':
    pm = PasswordManager()
    pm.__run__()

