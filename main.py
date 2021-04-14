import matplotlib.pyplot as plt
data_beef = "compro data beef.txt"
data_duck = "compro data duck.txt"
data_chicken = "compro data chicken.txt"
price = [350*94,3*31,2.7*73]
weight_ani = [350,3,2.7]
def menu():
    print("\nPlease select 1-4 (Press 4 to exit)")
    print("1.Graph by Category\n2.Graph by Provinces\n3.Pie chart by Total\n4.Exit")
    choice  = input("Choices: ")
    if int(choice,10) == 1:
        print("\nChoose animal type")
        print("1.Cattle\n2.Chicken\n3.Duck")
        choice2 = input("Choices: ")
    elif int(choice,10) == 2:
        choice2 = 0
    else:
        choice2 = -1
    return [choice,choice2]

def max_mem(name):
    a = open(name,"r+").read().splitlines()
    a = [i.split(",") for i in a]
    #change from string to int
    for i in range(1,len(a)):
        a[i][1] = int(a[i][1],10)
    return a[1:4],a[len(a)-1][1]
def find_district(name,dis):
    a = open(name,"r+").read().splitlines()
    a = [i.split(",") for i in a]
    for i in a:
        if i[0] == dis:
            print(i)
            return int(i[1],10)
#section 1
def print_table(name,b):
    title = ["Cattle","Chicken","Duck"]
    elem,_ = max_mem(name)
    print("\tTable for the highest 3 district("+title[b]+")")
    print("-"*60)
    print(" District\t Quantity\t Price per unit\t Total Price\t")
    print("-"*60)
    for row in elem:
        print(f" {row[0]}\t {row[1]}\t\t {price[b]:.2f}\t\t {row[1]*price[b]:.2f}")
    print("-"*60)
def make_graph_by_animal(name,b):
    title = ["Cattle","Chicken","Duck"]
    ex,_ = max_mem(name)
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
    ex,_ = max_mem(name)
    x = []
    y = []
    for i in ex:
        x.append(i[0])
        y.append(i[1]*price[int(b,10)-1])
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
    cattle_ex,tot = max_mem(data_beef)
    tot_cattle = tot*price[0]
    value.append(tot_cattle)
    tot_val += tot_cattle
    chick_ex,tot = max_mem(data_chicken)
    tot_chick = tot*price[1]
    value.append(tot_chick)
    tot_val += tot_chick
    duck_ex,tot = max_mem(data_duck)
    tot_duck = tot*price[2]
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
    print("\nplease choose district from 1 to "+str(len(dis_name)))
    #district choices
    for i in range(len(dis_name)):
        print(str(i+1)+"."+dis_name[i])
    choice = int(input("Choices: "),10) - 1
    real_dis = dis_name[choice]
    cattle_ex = find_district(data_beef,real_dis)
    Quantity.append((cattle_ex*weight_ani[0])/1000)
    chick_ex = find_district(data_chicken,real_dis)
    Quantity.append((chick_ex*weight_ani[1])/1000)
    duck_ex = find_district(data_duck,real_dis)
    Quantity.append((duck_ex*weight_ani[2])/1000)
    fig,ax =plt.subplots()
    plt.xlabel("Animal")
    plt.ylabel("Tot. Weight (Tons.)")
    ax.set_title("Animal in district: "+real_dis)
    ax.yaxis.grid(True)
    ax.bar(title,Quantity)
    plt.show()
if __name__ == "__main__":
    print("-"*50)
    print("Welcome to our program!")
    ex = open(data_beef,"r+").readlines()
    ex = [i.replace("\n","") for i in ex]
    ex = [i.split(",") for i in ex]
    ex =  ex[1:len(ex)-1]
    idx = [ex[i][0] for i in range(len(ex))] #get district name
    a,b=menu()
    while a  in ['1','2','3','4']:
        if a == "1":
            print("\nChoose graph type\n1.By Quantity\n2.By Price\n3.Total")
            c = input("Choices: ")
            if c == "1":
                if b == "1":
                    make_graph_by_animal(data_beef,b)
                elif b == "2":
                    make_graph_by_animal(data_chicken,b)
                elif b == "3":
                    make_graph_by_animal(data_duck,b)                
            elif c == "2":
                if b == "1":
                    price_graph(data_beef,b)
                elif b == "2":
                    price_graph(data_chicken,b)
                elif b == "3":
                    price_graph(data_duck,b)
            elif c == "3":
                if b == "1":
                    print_table(data_beef,int(b,10)-1)
                elif b == "2":
                    print_table(data_chicken,int(b,10)-1)
                elif b == "3":
                    print_table(data_duck,int(b,10)-1)
        elif a == "2":
            make_graph_by_provice(idx)
        elif a == "3":
            pie_price_graph()
        elif a == "4":
            break
        a,b = menu()
    print("Thanks you for using")