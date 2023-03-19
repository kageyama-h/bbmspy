import tkinter as tk
from tkinter import ttk
from page_view import NewClient, ManageClients

class SidebarView(ttk.Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        # key of dict: page name (new client, new booking ect)
        # value of dict: page object (ttk.Frame)
        self.pages = {}

        # arrangement
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.create_frame_treeview().grid(row=0, column=0, sticky="ens")
        self.create_frame_page().grid(row=0, column=1)

    def create_frame_page(self) -> ttk.Frame:
        self.frame_page = ttk.Frame(self)
        return self.frame_page


    def create_frame_treeview(self) -> ttk.Frame:
        # creates frame that holds sidebar treeview and instantiates sidebar treeview class
        self.frame_treeview = ttk.Frame(self)
        self.treeview_sidebar = SidebarTreeview(self.frame_treeview)
        self.treeview_sidebar.bind("<<TreeviewSelect>>", self.on_treeview_selection_changed)
        self.treeview_sidebar.pack(fill=tk.BOTH, expand=True)
        return self.frame_treeview


    def on_treeview_selection_changed(self, event):
        selected_item = self.treeview_sidebar.focus()
        # .get ran on dictionary to extract text
        selected_item_name = self.treeview_sidebar.item(selected_item).get("text")
        self.show_page(selected_item_name)

    def show_page(self, page_name: str):
        # pack forget all pages and pack given page
        for page_name in self.pages.keys():
            self.pages[page_name].pack_forget()

        self.pages[page_name].pack(fill=tk.BOTH, expand=True)

    def add_page(self, page_name:str, page):
        # instantiate a page frame and add it to the pages dictionary
        self.pages[page_name] = page(self.frame_page)
        self.treeview_sidebar.add_item(section_text=page_name)



class SidebarTreeview(ttk.Treeview):
    def __init__(self, master, **kw):
        # super() used because initialising superclass (treeview class)
        # master refers to root window of this window
        # **kw = optional keywords
        super().__init__(master, **kw)

        self.heading("#0", text="BBMS Sidebar")

    def add_item(self, section_text: str):
        # inserts a row into treeview sidebar
        self.insert(parent="",
                    index=tk.END,
                    tfext=section_text)



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x800")
    sidebar = SidebarView(root)
    sidebar.add_page(page_name="New Client", page=NewClient)
    sidebar.add_page(page_name="Manage Clients", page=ManageClients)
    sidebar.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
