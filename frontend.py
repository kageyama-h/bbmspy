from tkinter import *
import backend


# talk about event parameter - problems making func run so used print statements for testing
def curSelect(event):
    global selected
    index = listbox.curselection()[0]
    selected = listbox.get(index)

    e1.delete(0, END)
    e1.insert(END, selected[1])
    e2.delete(0, END)
    e2.insert(END, selected[2])
    e3.delete(0, END)
    e3.insert(END, selected[3])
    e4.delete(0, END)
    e4.insert(END, selected[4])


def viewCallback():
    listbox.delete(0, END)
    for row in backend.viewClient():
        listbox.insert(END, row)


def searchCallback():
    listbox.delete(0, END)
    for row in backend.searchClient(firstNameText.get(), lastNameText.get(), dobText.get(), phoneText.get()):
        listbox.insert(END, row)


def addCallback():
    backend.insertClient(firstNameText.get(), lastNameText.get(), dobText.get(), phoneText.get())
    listbox.delete(0, END)
    listbox.insert(END, (firstNameText.get(), lastNameText.get(), dobText.get(), phoneText.get()))


def deleteCallback():
    backend.deleteClient(selected[0])
    viewCallback()


def updateCallback():
    # keep id of selected, capture text within boxes for others
    # if the text is unchanged, it will not be set to null but value will be kept
    backend.updateClient(selected[0], firstNameText.get(), lastNameText.get(), dobText.get(), phoneText.get())


window = Tk()
window.wm_title("Beautiful Beauty Salon Management System")
window.geometry("800x800")



l1 = Label(window, text="First Name")
l1.grid(row=0, column=0)

l2 = Label(window, text="Last Name")
l2.grid(row=0, column=2)

l3 = Label(window, text="Date of Birth")
l3.grid(row=1, column=0)

l4 = Label(window, text="Phone Number")
l4.grid(row=1, column=2)

firstNameText = StringVar()
e1 = Entry(window, textvariable=firstNameText)
e1.grid(row=0, column=1)

lastNameText = StringVar()
e2 = Entry(window, textvariable=lastNameText)
e2.grid(row=0, column=3)

dobText = StringVar()
e3 = Entry(window, textvariable=dobText)
e3.grid(row=1, column=1)

phoneText = StringVar()
e4 = Entry(window, textvariable=phoneText)
e4.grid(row=1, column=3)

listbox = Listbox(window, height=6, width=35)
listbox.grid(row=2, column=0, rowspan=6, columnspan=2)
listbox.bind('<<ListboxSelect>>', curSelect)


b1 = Button(window, text="View all", width=12, command=viewCallback)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=12, command=searchCallback)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=12, command=addCallback)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update selected", width=12, command=updateCallback)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete selected", width=12, command=deleteCallback)
b5.grid(row=6, column=3)
#
# b6 = Button(window, text="Close", width=12, command=window.destroy)
# b6.grid(row=7, column=3)Í

window.mainloop()
