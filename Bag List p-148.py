# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 16:22:12 2022

@author: Ankan Datta
"""

from tkinter import * 
import random

root = Tk()

root.title("Bag List")
root.geometry("500x450")

root.configure(bg="gold")

bag_list = Label(root)
item = Label(root)

def bag():
    array = ["Bottle", "Tiffin", "ID_Card", "Passports", "Chocolates", "Ticket", "Handkerchief"]
    print(array)
    bag_list["text"] = "LIST OF ITEMS : " + str(array)
    
    item_list = random.sample(range(0,3),1)
    item["text"] = "PUT ITEM NO. " + str(item_list) + " IN BAG"
    
btn1 = Button(root, text="Which Item To Put In Bag", command=bag)    
btn1.place(relx=0.5, rely=0.3, anchor=CENTER)

bag_list.place(relx=0.5, rely=0.1, anchor=CENTER)
item.place(relx=0.5, rely=0.5, anchor=CENTER)
 
root.mainloop()