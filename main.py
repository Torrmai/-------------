# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
const_ani = {2:"compro data chicken.xlsx",1:"compro data beef.xlsx",3:"compro data duck.xlsx"}
def menu():
    print("1.Category\n2.Provinces\n3.Exit")
    choice  = input("Choices: ")
    if int(choice,10) == 1:
        print("1.Cattle\n2.Chicken\n3.Duck")
        choice2 = input("Choices: ")
    elif int(choice,10) == 2:
        choice2 = 0
    else:
        choice2 = -1
    return [choice,choice2]
def make_graph_by_animal(name,b):
    title = ["Cattle","Chicken","Duck"]
    ex = pd.read_excel(name)
    ex =ex.sort_values(by='NO.',ascending=False)
    ex = ex[1:4]
    x = []
    for i in ex['District']:
        x.append(i)
    y = []
    for i in ex['NO.']:
        y.append(i)
    fig,ax =plt.subplots()
    ax.set_title(title[int(b,10)-1])
    ax.bar(x,y)
    plt.show()
def price_graph(name,b):
    title = ["Cattle","Chicken","Duck"]
    price = {"Chicken":3*31,"Duck":2.7*73}
    ex = pd.read_excel(name)
    ex =ex.sort_values(by='NO.',ascending=False)
    ex = ex[1:4]
    x = []
    for i in ex['District']:
        x.append(i)
    y = []
    for i in ex['NO.']:
        y.append(i*price[title[int(b,10)-1]])
    fig,ax =plt.subplots()
    ax.set_title(title[int(b,10)-1])
    ax.bar(x,y)
    plt.show()    
if __name__ == "__main__":
    a,b=menu()
    while a != "3":
        if a == "1":
            print("Graph choice\n1.Quantity\n2.Price\n3.Total")
            c = input("Choices: ")
            if c == "1":
                make_graph_by_animal(const_ani[int(b,10)],b)
            elif c == "2":
                price_graph(const_ani[int(b,10)],b)
        a,b = menu()