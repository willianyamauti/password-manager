from tkinter import *
# from mvc_controller import Controller

FONT = ("Arial", 12, 'normal')
JUSTIFY = 'left'


class View:
    def __init__(self, controller):
        self.controller = controller
        self.view_logo = Logo()
        self.panel = PswGenPanel(controller)


class Logo:
    def __init__(self):
        self.logo_canvas = Canvas(width=200, height=200, highlightthickness=0)
        self.logo_img = PhotoImage(file="logo.png")
        self.logo_canvas.create_image(100, 100, image=self.logo_img)
        self.logo_canvas.grid(column=1, row=0)


class PswGenPanel:
    def __init__(self, controller):
        # website
        self.website_label = Label(text='Website:', font=FONT)
        self.website_label.grid(column=0, row=1)
        self.website_entry = Entry(width=49, font=FONT, highlightthickness=0, justify=JUSTIFY)
        self.website_entry.focus()
        self.website_entry.grid(column=1, row=1, columnspan=2)

        # username
        self.username_label = Label(text='Email/Username:', font=FONT)
        self.username_label.grid(column=0, row=2)
        self.username_entry = Entry(width=49, font=FONT, highlightthickness=0, justify=JUSTIFY)
        self.username_entry.insert(0, controller.model.username_temp)
        self.username_entry.grid(column=1, row=2, columnspan=2)

        # password
        self.password_label = Label(text='Password:', font=FONT)
        self.password_label.grid(column=0, row=3)
        self.psswrd = StringVar()
        self.password_entry = Entry(width=30, font=FONT, highlightthickness=0, justify=JUSTIFY)
        self.psswrd.get()
        self.password_entry.grid(column=1, row=3, sticky='W')

        # generate password button
        self.password_button = Button(text='Generate Password', width=14)
        # self.password_button.place(height=24, width=120, x=500, y=246)
        self.password_button.grid(column=2, row=3, sticky='E')
        self.password_button.bind("<Button>", controller.view_generate_password)

        # hide password checkbox
        self.check_state = IntVar(value=0)
        self.hide_password_checkbox = Checkbutton(text='Hide', variable=self.check_state, onvalue=1, offvalue=0)
        self.check_state.get()
        self.hide_password_checkbox.place(height=15, width=45, x=450, y=302, bordermode='outside')
        # self.hide_password_checkbox.grid(column=2, row=3,)
        self.hide_password_checkbox.bind("<Button>", controller.view_hide_password)

        # add button
        self.add_button = Button(text='Add', width=4, font=FONT, highlightthickness=0)
        self.add_button.grid(column=1, row=4, columnspan=5, sticky='N')
        self.add_button.bind("<Button>", controller.model_add_to_data)
