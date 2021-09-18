import string
from tkinter import *
from tkinter import messagebox
from mvc_model import Model
from mvc_views import View
from random import randint, choice, shuffle
import string


class Controller:
    def __init__(self):
        self.root = Tk()
        self.model = Model()
        self.view = View(self)
        self.root.title("Password Manager")
        self.root.config(padx=50, pady=50)
        self.root.mainloop()

    # ####--------------- Model related methods ---------------#####

    # format the Models atributes and append on database.txt
    def model_add_to_data(self, event):
        self.view_gather_user_inputs()
        if not self.model_check_input_size():
            error_msg = self.model_size_of_input_error_message_box()
        else:
            do_add = self.model_confirmation_message_box()
            if do_add:
                self.model.update_database()
                self.view_reset_fields()

    def model_check_input_size(self):
        if len(self.model.website_temp) == 0 or len(self.model.username_temp) == 0 or len(self.model.password_temp) == 0:
            return False
        else:
            return True

    def model_get_last_used_credentials(self):
        self.model.last_info = self.model.get_last_used_info()

    def model_reset_database(self):
        self.model.reset_database()

    def model_confirmation_message_box(self):
        msg = f"These are the details entered: \nEmail: {self.model.username_temp}" \
              f"\nPassword: {self.model.password_temp} \nDo you wish to save?"

        return messagebox.askokcancel(title=self.model.website_temp, message=msg)


    def model_size_of_input_error_message_box(self):
        msg = f"Error: Failed to save login credentials.\n\n" \
              f"There might be fields unfilled, check your input before continuing."

        return messagebox.showinfo(title='System Fail', message=msg)

    # ####--------------- View related methods ---------------#####

    # get user inputs from View and update the Model atributes
    def view_gather_user_inputs(self):
        self.model.website_temp = self.view.panel.website_entry.get()
        self.model.username_temp = self.view.panel.username_entry.get()
        self.model.password_temp = self.view.panel.password_entry.get()

    def view_reset_fields(self):
        self.view.panel.website_entry.delete(0, END)
        self.view.panel.username_entry.config(text = self.model.username_temp)
        self.view.panel.password_entry.delete(0, END)

    def view_generate_password(self, event):
        self.view.panel.password_entry.delete(0, END)
        # generates random passwords with length between 12 to 18 characters long
        random_symbols = [choice(string.punctuation) for _ in range(randint(2, 4))]
        random_letters = [choice(string.ascii_letters) for _ in range(randint(8, 10))]
        random_numbers = [choice(string.digits) for _ in range(randint(2, 4))]

        password_list = random_symbols + random_letters + random_numbers
        shuffle(password_list)
        password = "".join(password_list)
        self.view.panel.password_entry.insert(0, password)

    def view_hide_password(self, event):
        if self.view.panel.check_state.get() == 0:
            password = self.view.panel.psswrd
            self.view.panel.password_entry.config(show="*")
        else:
            self.view.panel.password_entry.config(show="")

    # fill the info with your last used username and password
    # def view_fill_with_last_used_credentials(self):
    # username already implemente above, uncomment only for future implementations
    # self.view.username_entry.insert(0, self.model.username_temp)
    # self.view.panel.password_entry.insert(0, self.model.password_temp)
