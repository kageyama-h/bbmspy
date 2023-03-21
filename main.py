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

        for f in (bookings, clients):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(clients)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class bookings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        self.firstname_text = tk.StringVar
        self.lastname_text = tk.StringVar
        self.dob_text = tk.StringVar
        self.phone_text = tk.StringVar

        self.top_frame = tk.Frame()
        self.top_frame.pack(fill = tk.BOTH, side = tk.TOP)

        btn_clients = ttk.Button(self.top_frame, text="Clients", command=lambda: controller.show_frame(clients))
        btn_clients.pack(side = tk.LEFT)


        btn_bookings = ttk.Button(self.top_frame, text="Bookings", command=lambda: controller.show_frame(bookings))
        btn_bookings.pack()



class clients(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.top = ttk.LabelFrame(self, text = "Clients")

        self.top.pack(fill = tk.BOTH, padx = 20, pady = 20)
        self.middle = ttk.LabelFrame(self, text = "Bookings")
        self.middle.pack(fill = tk.BOTH, padx = 20, pady = 20)
        self.bottom = ttk.LabelFrame(self)
        self.bottom.pack(fill = tk.BOTH, padx = 20, pady = 20)

        self.trv_clients = ttk.Treeview(self.top, columns = (1, 2, 3, 4, 5), show = "headings")
        self.trv_clients.pack(fill = tk.BOTH, expand = tk.TRUE)

        self.trv_clients.heading(1, text = "ID")
        self.trv_clients.heading(2, text = "First Name")
        self.trv_clients.heading(3, text = "Last Name")
        self.trv_clients.heading(4, text = "Date of Birth")
        self.trv_clients.heading(5, text = "Phone Number")


        self.trv_bookings = ttk.Treeview(self.middle, columns=(1,2,3,4,5,6), show="headings", height="5")
        self.trv_bookings.pack(expand = tk.TRUE, fill = tk.BOTH, side = tk.BOTTOM)

        self.trv_bookings.heading(1, text="Booking ID")
        self.trv_bookings.heading(2, text="Service")
        self.trv_bookings.heading(3, text="Booking Date")
        self.trv_bookings.heading(4, text="Client ID")
        self.trv_bookings.heading(5, text="Last Name")
        self.trv_bookings.heading(6, text="Date of Birth")


        self.selected = []
        self.firstname_text = tk.StringVar()
        self.lastname_text = tk.StringVar()
        self.dob_text = tk.StringVar()
        self.phone_text = tk.StringVar()


        self.trv_clients.bind('<<TreeviewSelect>>', self.get_selection_client)
        self.trv_clients.bind('<Double-Button>', self.manage_client_window)

        self.trv_bookings.bind('<<TreeviewSelect>>', self.get_selection_booking)
        self.trv_bookings.bind('<Double-Button>', self.manage_booking_window)


        btn_add_client = ttk.Button(self.bottom, text="Add Client",
                                       command=self.add_client_window)
        btn_add_client.pack(side = tk.LEFT)

        btn_add_booking = ttk.Button(self.bottom, text="Add a booking", command=self.add_booking_window)
        btn_add_booking.pack()

        self.populate_clients()
        self.populate_bookings()

    def manage_booking_window(self, event):
        pop_manage_booking_window = tk.Toplevel(self)

        lbl_service = ttk.Label(pop_manage_booking_window, text = "Service")
        lbl_service.pack()

        # fill service info!?!?!?!?!?


    def add_booking_window(self):
        self.pop_add_booking_window = tk.Toplevel(self)

        lbl_firstname = ttk.Label(self.pop_add_booking_window, text="First Name")
        self.ent_firstname = tk.Entry(self.pop_add_booking_window, textvariable=self.firstname_text)
        lbl_lastname = ttk.Label(self.pop_add_booking_window, text="Last Name")
        self.ent_lastname = tk.Entry(self.pop_add_booking_window, textvariable=self.lastname_text)
        lbl_dob = ttk.Label(self.pop_add_booking_window, text="Date of Birth")
        self.ent_dob = tk.Entry(self.pop_add_booking_window, textvariable=self.dob_text)
        lbl_phone = ttk.Label(self.pop_add_booking_window, text="Phone Number")
        self.ent_phone = tk.Entry(self.pop_add_booking_window, textvariable=self.phone_text)

        lbl_firstname.pack()
        self.ent_firstname.pack()

        lbl_lastname.pack()
        self.ent_lastname.pack()

        lbl_dob.pack()
        self.ent_dob.pack()

        lbl_phone.pack()
        self.ent_phone.pack()

        self.cbut_editing_value = tk.IntVar(value=0)
        self.cbut_editing = tk.Checkbutton(self.pop_add_booking_window,
                                           text = "Enable Editing",
                                           variable = self.cbut_editing_value,
                                           onvalue = 1,
                                           offvalue = 0,
                                           command = self.cbut_editing_callback)
        self.cbut_editing.pack()

        self.btn_update = ttk.Button(self.pop_add_booking_window,
                                     text="Update selected",
                                     width=12,
                                     command=self.update_client_callback)
        self.btn_update.pack()

        self.btn_add_booking = ttk.Button(self.pop_add_booking_window,
                                          text="Add a booking",
                                          width=12,
                                          command=self.add_booking_callback)
        self.btn_add_booking.pack()

        self.drop_service_value = tk.StringVar(self)
        self.drop_service = tk.OptionMenu(self.pop_add_booking_window,
                                          self.drop_service_value,
                                          *self.get_value())
        self.drop_service.pack()

        self.date = Calendar(self.pop_add_booking_window, selectmode='day')
        self.date.pack()

        self.get_value()

        self.fill_pop()


    def populate_clients(self):
        for item in self.trv_clients.get_children():
            self.trv_clients.delete(item)
        for i in db.get_clients():
            self.trv_clients.insert('', 'end', values = i)

    def populate_bookings(self):
        for item in self.trv_bookings.get_children():
            self.trv_bookings.delete(item)
        for i in self.package_bookings():
            self.trv_bookings.insert('', 'end', values = i)

    def package_bookings(self):
        raw_data = db.get_bookings()
        id = [i[0] for i in raw_data]
        service = [i[1] for i in raw_data]
        booking_date = [i[2] for i in raw_data]
        client = [i[3] for i in raw_data]
        service_out = list()
        lastname_out = list()
        dob_out = list()
        for i in range(0, len(service)):
            x = db.get_service_name(service[i])
            service_out.append(x)
        for i in range(0, len(client)):
            x = db.get_client_lastname(client[i])
            lastname_out.append(x)
            z = db.get_client_dob(client[i])
            dob_out.append(z)

        print(service_out)
        print(lastname_out)
        print(dob_out)
        print(booking_date)

        def convert(list):
            return tuple(list)

        client_id = (convert(client))

        out = (list(zip(id, service_out, booking_date, client_id, lastname_out, dob_out)))

        return out




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
        self.key_list = list(dic.keys())
        self.value_list = list(dic.values())

        position = self.value_list.index(picked)
        return(self.key_list[position])

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

    def get_selection_client(self, event):
        # row id of treeview
        selected_item = self.trv_clients.focus()
        data = self.trv_clients.item(selected_item)
        # converts to the data at row id
        self.selected = data.get("values")
        print(self.selected)

    def get_selection_booking(self, event):
        # row id of treeview
        selected_item = self.trv_bookings.focus()
        data = self.trv_bookings.item(selected_item)
        # converts to the data at row id
        self.selected = data.get("values")
        print(self.selected)

    def manage_client_window(self, event):
        self.pop_manage_client_window = tk.Toplevel(self)

        lbl_firstname = ttk.Label(self.pop_manage_client_window, text="First Name")
        self.ent_firstname = tk.Entry(self.pop_manage_client_window, textvariable=self.firstname_text)
        lbl_lastname = ttk.Label(self.pop_manage_client_window, text="Last Name")
        self.ent_lastname = tk.Entry(self.pop_manage_client_window, textvariable=self.lastname_text)
        lbl_dob = ttk.Label(self.pop_manage_client_window, text="Date of Birth")
        self.ent_dob = tk.Entry(self.pop_manage_client_window, textvariable=self.dob_text)
        lbl_phone = ttk.Label(self.pop_manage_client_window, text="Phone Number")
        self.ent_phone = tk.Entry(self.pop_manage_client_window, textvariable=self.phone_text)

        lbl_firstname.pack()
        self.ent_firstname.pack()

        lbl_lastname.pack()
        self.ent_lastname.pack()

        lbl_dob.pack()
        self.ent_dob.pack()

        lbl_phone.pack()
        self.ent_phone.pack()

        self.cbut_editing_value = tk.IntVar(value=0)
        self.cbut_editing = tk.Checkbutton(self.pop_manage_client_window,
                                           text="Enable Editing",
                                           variable=self.cbut_editing_value,
                                           onvalue=1,
                                           offvalue=0,
                                           command=self.cbut_editing_callback)
        self.cbut_editing.pack()

        self.btn_update = ttk.Button(self.pop_manage_client_window,
                                     text="Update selected",
                                     width=12,
                                     command=self.update_client_callback)
        self.btn_update.pack()

        self.fill_pop()

    def add_client_window(self):
        self.pop_add_client_window = tk.Toplevel(self)

        lbl_firstname = ttk.Label(self.pop_add_client_window, text="First Name")
        self.ent_firstname = tk.Entry(self.pop_add_client_window, textvariable=self.firstname_text)
        lbl_lastname = ttk.Label(self.pop_add_client_window, text="Last Name")
        self.ent_lastname = tk.Entry(self.pop_add_client_window, textvariable=self.lastname_text)
        lbl_phone = ttk.Label(self.pop_add_client_window, text="Phone Number")
        self.ent_phone = tk.Entry(self.pop_add_client_window, textvariable=self.phone_text)

        lbl_firstname.pack()
        self.ent_firstname.pack()

        lbl_lastname.pack()
        self.ent_lastname.pack()



        lbl_phone.pack()
        self.ent_phone.pack()

        lbl_dob = ttk.Label(self.pop_add_client_window, text="Client Date of Birth")
        lbl_dob.pack()

        self.date = Calendar(self.pop_add_client_window, selectmode='day')
        self.date.pack()

        self.btn_add_client = ttk.Button(self.pop_add_client_window,
                                          text="Add",
                                          width=12,
                                          command=self.add_client_callback)
        self.btn_add_client.pack()

    def date_pick_callback(self):
        self.picked_date = self.date.get_date()
        return self.picked_date

    def add_client_callback(self):
        db.insert_client(self.firstname_text.get(),
                         self.lastname_text.get(),
                         self.date_pick_callback(),
                         self.phone_text.get())
        self.populate_clients()

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

    def insert_trv(self, data):
        for item in self.trv.get_children():
            self.trv.delete(item)
        for row in data:
            self.trv.insert('', 'end', values = data)

    def search_clients(self, event):
        typed = self.ent_search.get()
        if typed == '':
            data = db.get_clients()
        else:
            data = []
            for row in db.get_clients():
                if typed in row:
                    data.append(row)
        self.insert_trv(data)




    # def update_client(self):
    #     print(self.selected)
    #     db.update_client(self.selected[0],
    #                      self.firstname_text.get(),
    #                      self.lastname_text.get(),
    #                      self.dob_text.get(),
    #                      self.phone_text.get())
    #     self.view_callback()



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


    def get_client_lastname(self, id):
        self.conn = sqlite3.connect("clients.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT lastName from client WHERE id=?",(id,))
        lastname = self.cur.fetchall()
        self.conn.commit()
        return lastname

    def get_client_dob(self, id):
        self.conn = sqlite3.connect("clients.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT dob from client WHERE id=?", (id,))
        dob = self.cur.fetchall()
        self.conn.commit()
        return dob

    def get_services(self):
        self.conn = sqlite3.connect("clients.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT id, service from service")
        services = self.cur.fetchall()
        self.conn.commit()
        return services

    def get_service_name(self, id):
        self.conn = sqlite3.connect("clients.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT service from service WHERE id=?",(id))
        services_name = self.cur.fetchall()
        self.conn.commit()
        return services_name


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
app.geometry("1200x800")
app.wm_title("Beautiful Beauty Salon Management System")
app.mainloop()
