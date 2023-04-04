from datetime import datetime

name = input(" enter the Your  name : ")

lists='''
USBCABLES : Rs 199 per 1
HEADPHONES : Rs 699 per1
CHARGER    : Rs 1999 per1
PORTCABLE : Rs 599 per1
BATTERIES  : Rs 299 per 1
ANALOUGEEQIUPMENT :8999 per 1
DIGITALMONITERS :  6999 per 1
REFRIGERATORS : 12999 per 1
TELEVISIONS : 9999 per 1
IRONBOX : 8999 per 1
DIGITALWATCHES : 5999 per 1
WIRELESSHEADPHONES  : 999 per 1
DIGITALLOCKS : 8899 per 1


'''

price = 0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]



#rates
items={'USBCABLES': 199,'HEADPHONES':699,'CHARGER': 1999,
       'PORTCABLE': 599,'BATTERIES':299,'ANALOUGEEQIUPMENT' :8999,
       'DIGITAL MONITERS' :  6999,'REFRIGERATORS' : 12999,'TELEVISIONS' : 9999,
       'IRONBOX' : 8999,'DIGITALWATCHES' : 5999,'WIRELESSHEADPHONES'  : 999,'DIGITALLOCKS' : 8899}






option = int(input("enter for list of items press 1  :-- "))

if option==1:
    print(lists)



for i in range(len(items)):
    inp1=int(input("for purchasing press 1 or pess 2  to for exit :--"))
    if inp1==2:
        break
    if inp1==1:
        item = input("Enter the item :")
        num_of_items=int(input("enter the number of items : "))
        if item in items.keys():
            price=num_of_items*(items[item])
            pricelist.append((item,num_of_items,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(num_of_items)
            plist.append(price)
            gst=(totalprice*5)/100
            finalprice=gst+totalprice
        else:
            print("the item is not avaliable")
    else:
        print("you've entered wrong number ")
    inp = input("do you  need the bill yes or no : ")
    if inp=='yes':
        pass
        if finalprice!=0:
            print(25*"=","RK ENTERPRICES",25*"=")
            print(28*" ","KARIMNAGAR")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ","num_of_items",5*" "," price")

            for i in range(len(pricelist)):
                print(i,ilist[i],qlist[i],plist[i])
            print(75*"-")
            print(50*" ",'totalprice:', 'Rs', totalprice)
            print('GST:', 50*" ",'Rs', gst)
            print(75*"-")
            print(50*" ",'totalamount:', 'Rs', finalprice)
            print(75*"-")

            print(50*" ",'THANK YOU FOR VISITING')

            print(75*"-")


