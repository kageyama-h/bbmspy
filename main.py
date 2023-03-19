import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import sqlite3


# inherits tkinter
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for f in (view_bookings, new_client, NewBooking):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(view_bookings)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class view_bookings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        self.top_frame = tk.Frame()
        self.top_frame.pack(fill = tk.BOTH, side = tk.TOP)

        btn_new_client = ttk.Button(self.top_frame, text="New Client", command=lambda: controller.show_frame(new_client))
        btn_new_client.pack(side = tk.LEFT)

        btn_page2 = ttk.Button(self.top_frame, text="New Booking", command=lambda: controller.show_frame(NewBooking))
        btn_page2.pack(side = tk.RIGHT)

        btn_page2 = ttk.Button(self.top_frame, text="View Bookings", command=lambda: controller.show_frame(view_bookings))
        btn_page2.pack()


        self.rclick = tk.Menu(self, tearoff=0)
        self.rclick.add_command(label = 'New Client', command=lambda: controller.show_frame(new_client))

        self.bind("<Button-2>", self.rclick_callback)

        self.treeview = ttk.Treeview(self, columns=(1,2,3,4,5), show="headings", height="5")
        self.treeview.pack(expand = tk.TRUE, fill = tk.BOTH, side = tk.BOTTOM)

        self.treeview.heading(1, text="Service")
        self.treeview.heading(2, text="Booking Date")
        self.treeview.heading(3, text="First Name")
        self.treeview.heading(4, text="Last Name")
        self.treeview.heading(5, text="Date of Birth")

        self.populate_treeview()

    def populate_treeview(self):
        for row in db.get_bookings():
            self.treeview.insert('', tk.END, values=row)
            print(row)

    def package_data(self):
        



    def update(self, data):
        self.listbox.delete(0, tk.END)
        for row in data:
            self.listbox.insert(tk.END, row)

    def load_bookings(self):
        self.listbox.delete(0, tk.END)
        for row in db.get_bookings():
            self.listbox.insert(tk.END, row)

    def search(self, event):
        typed = self.ent_search.get()
        if typed == '':
            data = db.get_bookings()
        else:
            data = []
            for row in db.get_bookings():
                if typed in row:
                    data.append(row)
        self.update(data)

    def rclick_callback(self, event):
        self.rclick.tk_popup(event.x_root, event.y_root, 0)



class new_client(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)

        self.firstname_text = tk.StringVar()
        self.lastname_text = tk.StringVar()
        self.dob_text = tk.StringVar()
        self.phone_text = tk.StringVar()

        lbl_firstname = ttk.Label(self, text="First Name")
        lbl_lastname = ttk.Label(self, text="Last Name")
        lbl_dob = ttk.Label(self, text="Date of Birth")
        lbl_phone = ttk.Label(self, text="Phone Number")

        lbl_firstname.grid(row = 0, column = 0, sticky = tk.W, pady = 2)
        lbl_lastname.grid(row = 2,  column = 0, sticky = tk.W, pady = 2)
        lbl_dob.grid(row = 4, column = 0, sticky = tk.W, pady = 2)
        lbl_phone.grid(row = 6, column = 0, sticky = tk.W, pady = 2)

        self.ent_firstname = ttk.Entry(self, textvariable=self.firstname_text)
        self.ent_lastname = ttk.Entry(self, textvariable=self.lastname_text)
        self.ent_dob = ttk.Entry(self, textvariable=self.dob_text)
        self.ent_phone = ttk.Entry(self, textvariable=self.phone_text)

        self.ent_firstname.grid(row = 1, column = 0, sticky = tk.W, pady = 2)
        self.ent_lastname.grid(row = 3, column = 0, sticky = tk.W, pady = 2)
        self.ent_dob.grid(row = 5, column = 0, sticky = tk.W, pady = 2)
        self.ent_phone.grid(row = 7, column = 0, sticky = tk.W, pady = 2)

        btn_view = ttk.Button(self, text="View all", width=12, command=self.view_callback)
        btn_search = ttk.Button(self, text="Search entry", width=12)
        btn_add = ttk.Button(self, text="Add entry", width=12, command=self.add_callback)
        btn_update = ttk.Button(self, text="Update selected", width=12, command=self.update_client)
        btn_delete = ttk.Button(self, text="Delete selected", width=12, command=self.delete_callback)


        btn_view.grid(row = 0, column = 2, sticky = tk.E, pady = 0)
        btn_search.grid(row = 1, column = 2, sticky = tk.E, pady = 0)
        btn_add.grid(row = 2, column = 2, sticky = tk.E, pady = 0)
        btn_update.grid(row = 3, column = 2, sticky = tk.E, pady = 0)
        btn_delete.grid(row = 4, column = 2, sticky = tk.E, pady = 0)


        self.listbox = tk.Listbox(self, height=6, width=35)
        self.listbox.bind('<<ListboxSelect>>', self.cur_select)
        self.listbox.grid(row = 10, column = 1, sticky = tk.E, pady = 2)

        btn_newclient = ttk.Button(self, text="New Client", command=lambda: controller.show_frame(NewClient))
        btn_newclient.grid(row = 11, column = 1, sticky = tk.E, pady = 2)

        btn_page2 = ttk.Button(self, text="New Booking", command=lambda: controller.show_frame(NewBooking))
        btn_page2.grid(row = 12, column = 1, sticky = tk.E, pady = 2)

        btn_page2 = ttk.Button(self, text="Visit Home", command=lambda: controller.show_frame(Start))
        btn_page2.grid(row = 13, column = 1, sticky = tk.E, pady = 2)

    def cur_select(self, event):
        self.selected = self.listbox.get(int(self.listbox.curselection()[0]))

        self.ent_firstname.delete(0, tk.END)
        self.ent_firstname.insert(tk.END, self.selected[1])
        self.ent_lastname.delete(0, tk.END)
        self.ent_lastname.insert(tk.END, self.selected[2])
        self.ent_dob.delete(0, tk.END)
        self.ent_dob.insert(tk.END, self.selected[3])
        self.ent_phone.delete(0, tk.END)
        self.ent_phone.insert(tk.END, self.selected[4])


    def add_callback(self):
        db.insert_client(self.firstname_text.get(),
                         self.lastname_text.get(),
                         self.dob_text.get(),
                         self.phone_text.get())
        self.listbox.delete(0, tk.END)
        self.listbox.insert(tk.END, (self.firstname_text.get(),
                                     self.lastname_text.get(),
                                     self.dob_text.get(),
                                     self.phone_text.get()))

    def view_callback(self):
        self.listbox.delete(0, tk.END)
        for row in db.get_clients():
            self.listbox.insert(tk.END, row)

    def delete_callback(self):
        db.delete_client(self.selected[0])
        self.view_callback()

    def update_client(self):
        print(self.selected)
        db.update_client(self.selected[0],
                         self.firstname_text.get(),
                         self.lastname_text.get(),
                         self.dob_text.get(),
                         self.phone_text.get())
        self.view_callback()

class NewBooking(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.firstname_text = tk.StringVar()
        self.lastname_text = tk.StringVar()
        self.dob_text = tk.StringVar()
        self.phone_text = tk.StringVar()

        self.ent_search = tk.Entry(self, font=("Helvetica", 20))
        self.ent_search.pack(pady=20)
        self.ent_search.bind("<KeyRelease>", self.search)

        self.listbox = tk.Listbox(self, width=50)
        self.listbox.pack(pady=40)
        self.listbox.bind('<<ListboxSelect>>', self.cur_select)
        self.listbox.bind('<Double-Button>', self.pop_window)
        new_client.view_callback(self)

    def pop_window(self, event):
        data = self.listbox.get(self.listbox.curselection()[0])
        self.pop = tk.Toplevel(self)

        lbl_firstname = ttk.Label(self.pop, text="First Name")
        self.ent_firstname = tk.Entry(self.pop, textvariable=self.firstname_text)
        lbl_lastname = ttk.Label(self.pop, text="Last Name")
        self.ent_lastname = tk.Entry(self.pop, textvariable=self.lastname_text)
        lbl_dob = ttk.Label(self.pop, text="Date of Birth")
        self.ent_dob = tk.Entry(self.pop, textvariable=self.dob_text)
        lbl_phone = ttk.Label(self.pop, text="Phone Number")
        self.ent_phone = tk.Entry(self.pop, textvariable=self.phone_text)

        lbl_firstname.pack()
        self.ent_firstname.pack()

        lbl_lastname.pack()
        self.ent_lastname.pack()

        lbl_dob.pack()
        self.ent_dob.pack()

        lbl_phone.pack()
        self.ent_phone.pack()

        self.cbut_editing_value = tk.IntVar(value=0)
        self.cbut_editing = tk.Checkbutton(self.pop,
                                           text = "Enable Editing",
                                           variable = self.cbut_editing_value,
                                           onvalue = 1,
                                           offvalue = 0,
                                           command = self.cbut_editing_callback)
        self.cbut_editing.pack()

        self.btn_update = ttk.Button(self.pop,
                                     text="Update selected",
                                     width=12,
                                     command=self.update_client_callback)
        self.btn_update.pack()

        self.btn_add_booking = ttk.Button(self.pop,
                                          text="Add a booking",
                                          width=12,
                                          command=self.add_booking_callback)
        self.btn_add_booking.pack()

        self.drop_service_value = tk.StringVar(self)
        self.drop_service = tk.OptionMenu(self.pop,
                                          self.drop_service_value,
                                          *self.get_value())
        self.drop_service.pack()

        self.date = Calendar(self.pop, selectmode='day')
        self.date.pack()

        self.get_value()

        self.fill_pop()


    def date_pick_callback(self):
        self.picked_date = self.date.get_date()
        return self.picked_date

    def add_booking_callback(self):
        client_id = self.selected[0]
        db.insert_booking(self.get_key(self.drop_service_value.get()),
                          self.date_pick_callback(),
                          client_id)

        print(self.get_key(self.drop_service_value.get()), self.date_pick_callback(), client_id)


    def get_key(self, picked):
        dic = self.dictionary_convert()
        key_list = list(dic.keys())
        value_list = list(dic.values())

        position = value_list.index(picked)
        return(key_list[position])

    def get_value(self):
        i = self.dictionary_convert()
        x = i.values()
        return x


    def dictionary_convert(self):
        services = db.get_services()
        out = dict((x, y) for x, y in services)
        return out


    def update_client_callback(self):
        print(self.selected)
        db.update_client(self.selected[0],
                         self.firstname_text.get(),
                         self.lastname_text.get(),
                         self.dob_text.get(),
                         self.phone_text.get())
        self.fill_pop()


    def cbut_editing_callback(self):
        if self.cbut_editing_value.get() == 0:
            self.ent_firstname.config(state='disabled')
            self.ent_lastname.config(state='disabled')
            self.ent_dob.config(state='disabled')
            self.ent_phone.config(state='disabled')
        if self.cbut_editing_value.get() == 1:
            self.ent_firstname.config(state='normal')
            self.ent_lastname.config(state='normal')
            self.ent_dob.config(state='normal')
            self.ent_phone.config(state='normal')



    def fill_pop(self):
        self.ent_firstname.delete(0, tk.END)
        self.ent_firstname.insert(tk.END, self.selected[1])
        self.ent_lastname.delete(0, tk.END)
        self.ent_lastname.insert(tk.END, self.selected[2])
        self.ent_dob.delete(0, tk.END)
        self.ent_dob.insert(tk.END, self.selected[3])
        self.ent_phone.delete(0, tk.END)
        self.ent_phone.insert(tk.END, self.selected[4])
        # runs so start disabled - tried putting this with definition of checkbox, but if it was disabled here then the data would never be able to get in.
        self.cbut_editing_callback()



    def cur_select(self, event):
        self.selected = self.listbox.get(int(self.listbox.curselection()[0]))
        print(self.selected)
        print(type(self))


    def search(self, event):
        typed = self.ent_search.get()
        if typed == '':
            data = db.get_clients()
        else:
            data = []
            for row in db.get_clients():
                if typed in row:
                    data.append(row)
        self.update(data)


    def update(self, data):
        self.listbox.delete(0, tk.END)
        for row in data:
            self.listbox.insert(tk.END, row)





class Db():
    def __init__(self):
        self.conn = sqlite3.connect("clients.db")
        self.cur = self.conn.cursor()

    def insert_client(self, firstname_text, lastname_text, dob_text, phone_text):
        print(firstname_text, lastname_text, dob_text, phone_text)
        self.conn = sqlite3.connect("clients.db")
        self.cur = self.conn.cursor()
        self.cur.execute("INSERT INTO client VALUES (NULL,?,?,?,?)",(firstname_text,lastname_text,dob_text,phone_text))
        self.conn.commit()

    def insert_booking(self, service, date, client_id):
        self.conn = sqlite3.connect("clients.db")
        self.cur = self.conn.cursor()
        self.cur.execute("INSERT INTO booking VALUES (NULL,?,?,?)",(service,str(date),int(client_id)))
        self.conn.commit()

    def get_clients(self):
        self.conn = sqlite3.connect("clients.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM client")
        rows = self.cur.fetchall()
        self.conn.commit()
        return rows

    def get_services(self):
        self.conn = sqlite3.connect("clients.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT id, service from service")
        services = self.cur.fetchall()
        self.conn.commit()
        return services

    def get_bookings(self):
        self.conn = sqlite3.connect("clients.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * from booking")
        rows = self.cur.fetchall()
        self.conn.commit()
        return rows

    def delete_client(self, id):
        self.conn = sqlite3.connect("clients.db")
        self.cur = self.conn.cursor()
        self.cur.execute("DELETE FROM client WHERE id=?", (id,))
        self.conn.commit()

    def update_client(self, id, firstname_text, lastname_text, dob_text, phone_text):
        self.conn = sqlite3.connect("clients.db")
        self.cur = self.conn.cursor()
        self.cur.execute("UPDATE client SET firstName=?, lastName=?, dob=?, phone=? WHERE id=?",
                    (firstname_text, lastname_text, dob_text, phone_text, id))
        self.conn.commit()
        self.conn.close()

    def __del__(self):
        self.conn.close()


db = Db()
app = App()
app.geometry("900x800")
app.wm_title("Beautiful Beauty Salon Management System")
app.mainloop()
