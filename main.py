import text_tranfromer
import matplotlib.pyplot as plt
const_ani = {2:"compro data chicken.csv",1:"compro data beef.csv",3:"compro data duck.csv"}
price = {"Cattle":350*94,"Chicken":3*31,"Duck":2.7*73}
weight_ani = [350,3,2.7]
def menu():
    print("1.Category\n2.Provinces\n3.Total\n4.Exit")
    choice  = input("Choices: ")
    if int(choice,10) == 1:
        print("1.Cattle\n2.Chicken\n3.Duck")
        choice2 = input("Choices: ")
    elif int(choice,10) == 2:
        choice2 = 0
    else:
        choice2 = -1
    return [choice,choice2]

#section 1
def make_graph_by_animal(name,b):
    title = ["Cattle","Chicken","Duck"]
    ex,_ = text_tranfromer.max_mem(name)
    x = []
    y = []
    for i in ex:
        x.append(i[0])
        y.append(i[1])
    fig,ax =plt.subplots()
    plt.xlabel("District")
    plt.ylabel("Quantity")
    ax.set_title(title[int(b,10)-1]+" Quantity")
    ax.yaxis.grid(True)
    ax.bar(x,y)
    print(y)
    plt.show()
def price_graph(name,b):
    title = ["Cattle","Chicken","Duck"]
    ex,_ = text_tranfromer.max_mem(name)
    x = []
    y = []
    for i in ex:
        x.append(i[0])
        y.append(i[1]*price[title[int(b,10)-1]])
    fig,ax =plt.subplots()
    print(y)
    ax.set_title(title[int(b,10)-1]+" Price")
    plt.xlabel("District")
    plt.ylabel("Price")
    ax.yaxis.grid(True)
    ax.bar(x,y)
    plt.show()
def pie_price_graph():
    title = ["Cattle","Chicken","Duck"]
    value = []
    tot_val = 0
    cattle_ex,tot = text_tranfromer.max_mem(const_ani[1])
    tot_cattle = tot*price["Cattle"]
    value.append(tot_cattle)
    tot_val += tot_cattle
    chick_ex,tot = text_tranfromer.max_mem(const_ani[2])
    tot_chick = tot*price["Chicken"]
    value.append(tot_chick)
    tot_val += tot_chick
    duck_ex,tot = text_tranfromer.max_mem(const_ani[3])
    tot_duck = tot*price["Duck"]
    value.append(tot_duck)
    tot_val += tot_duck
    percent = [(i/tot_val)*100 for i in value]
    fig,ax =plt.subplots()
    ax.set_title("Total sales of animal by price")
    ax.pie(percent,labels=title, autopct='%1.1f%%')
    ax.axis('equal')
    plt.show()
#section 2
def make_graph_by_provice(dis_name):
    title = ["Cattle","Chicken","Duck"]
    Quantity = []
    #district choices
    for i in dis_name:
        print(i)
    choice = int(input("Choices: "),10) - 1
    real_dis = dis_name[choice]
    cattle_ex = text_tranfromer.find_district(const_ani[1],real_dis)
    Quantity.append((cattle_ex*weight_ani[0])/1000)
    chick_ex = text_tranfromer.find_district(const_ani[2],real_dis)
    Quantity.append((chick_ex*weight_ani[1])/1000)
    duck_ex = text_tranfromer.find_district(const_ani[3],real_dis)
    Quantity.append((duck_ex*weight_ani[2])/1000)
    fig,ax =plt.subplots()
    plt.xlabel("Animal")
    plt.ylabel("Tot. Weight (Tons.)")
    ax.set_title("Animal in district: "+real_dis)
    ax.yaxis.grid(True)
    ax.bar(title,Quantity)
    plt.show()
if __name__ == "__main__":
    ex = open(const_ani[1],"r+").readlines()
    ex = [i.replace("\n","") for i in ex]
    ex = [i.split(",") for i in ex]
    ex =  ex[1:len(ex)-1]
    idx = [ex[i][0] for i in range(len(ex))] #get district name
    a,b=menu()
    while a  in ['1','2','3','4']:
        if a == "1":
            print("Graph choice\n1.Quantity\n2.Price\n3.Total")
            c = input("Choices: ")
            if c == "1":
                make_graph_by_animal(const_ani[int(b,10)],b)
            elif c == "2":
                price_graph(const_ani[int(b,10)],b)
        elif a == "2":
            make_graph_by_provice(idx)
        elif a == "3":
            pie_price_graph()
        elif a == "4":
            break
        a,b = menu()
    print("Thanks you for using")