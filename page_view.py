import tkinter as tk
from tkinter import ttk
import backend

class Page(ttk.Frame):
    def __init__(self, master, *kw):
        super().__init__(master, *kw)

# new client page derives from page class (seen through parameter)
class NewClient(Page):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        self.create_frame_content().pack(fill=tk.BOTH, expand=True)

    def create_frame_content(self):
        # this frame goes into NewClient page frame
        self.frame_content = ttk.Frame(self)

        # talk about differing ttk and tk causing issues and rectifying it

        lbl_firstname = ttk.Label(self, text="First Name")
       # lbl_firstname.grid(row=0, column=0)

        lbl_lastname = ttk.Label(self, text="Last Name")
       # lbl_lastname.grid(row=0, column=2)

        lbl_dob = ttk.Label(self, text="Date of Birth")
      #  lbl_dob.grid(row=1, column=0)

        lbl_phone = ttk.Label(self, text="Phone Number")
      #  lbl_phone.grid(row=1, column=2)

        firstname_text = tk.StringVar()
        ent_firstname = ttk.Entry(self, textvariable=firstname_text)
      #  ent_firstname.grid(row=0, column=1)

        lastname_text = tk.StringVar()
        ent_lastname = ttk.Entry(self, textvariable=lastname_text)
      #  ent_lastname.grid(row=0, column=3)

        dob_text = tk.StringVar()
        ent_dob = ttk.Entry(self, textvariable=dob_text)
      #  ent_dob.grid(row=1, column=1)

        phone_text = tk.StringVar()
        ent_phone = ttk.Entry(self, textvariable=phone_text)
      #  ent_phone.grid(row=1, column=3)

        scrollbar = ttk.Scrollbar(self)
      #  scrollbar.grid(row=2, column=2, rowspan=6)

        listbox = tk.Listbox(self, height=6, width=35)
      # listbox.grid(row=2, column=0, rowspan=6, columnspan=2)

        listbox.bind('<<ListboxSelect>>')

        listbox.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=listbox.yview)

        view_button = ttk.Button(self, text="View all", width=12)
      #  view_button.grid(row=2, column=3)

        search_button = ttk.Button(self, text="Search entry", width=12)
      #  search_button.grid(row=3, column=3)

        add_button = ttk.Button(self, text="Add entry", width=12)
      #  add_button.grid(row=4, column=3)

        update_button = ttk.Button(self, text="Update selected", width=12)
      #  update_button.grid(row=5, column=3)

        delete_button = ttk.Button(self, text="Delete selected", width=12)
      #  delete_button.grid(row=6, column=3)

        quit_button = ttk.Button(self, text="Quit", width=12, command=self.destroy)
      #  quit_button.grid(row=7, column=3)

        return self.frame_content




class ManageClients(Page):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        self.create_frame_content().pack()

    def create_frame_content(self):
        # this frame goes into NewClient page frame
        self.frame_content = ttk.Frame(self)

        lbl_firstname = ttk.Label(self, text="First Name")
        lbl_firstname.pack()

        firstname_text = tk.StringVar()
        ent_firstname = ttk.Entry(self, textvariable=firstname_text)
        ent_firstname.pack()

        lbl_lastname = ttk.Label(self, text="Last Name")
        lbl_lastname.pack()

        lastname_text = tk.StringVar()
        ent_lastname = ttk.Entry(self, textvariable=lastname_text)
        ent_lastname.pack()

        lbl_dob = ttk.Label(self, text="Date of Birth")
        lbl_dob.pack()

        dob_text = tk.StringVar()
        ent_dob = ttk.Entry(self, textvariable=dob_text)
        ent_dob.pack()

        lbl_phone = ttk.Label(self, text="Phone Number")
        lbl_phone.pack()

        phone_text = tk.StringVar()
        ent_phone = ttk.Entry(self, textvariable=phone_text)
        ent_phone.pack()

        # scrollbar = ttk.Scrollbar(self)
        # scrollbar.pack()

        # listbox = tk.Listbox(self, height=6, width=35)
        # listbox.pack()

        # listbox.bind('<<ListboxSelect>>')

        # listbox.configure(yscrollcommand=scrollbar.set)
        # scrollbar.configure(command=listbox.yview)

        # view_button = ttk.Button(self, text="View all", width=12)
        # view_button.pack()

        # search_button = ttk.Button(self, text="Search entry", width=12)
        #  search_button.grid(row=3, column=3)

        add_button = ttk.Button(self, text="Add entry", width=12)
        add_button.grid(row=4, column=3)

        update_button = ttk.Button(self, text="Update selected", width=12)
        #  update_button.grid(row=5, column=3)

        delete_button = ttk.Button(self, text="Delete selected", width=12)
        #  delete_button.grid(row=6, column=3)

        quit_button = ttk.Button(self, text="Quit", width=12, command=self.destroy)

    #  quit_button.grid(row=7, column=3)

        return self.frame_content