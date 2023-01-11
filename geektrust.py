from sys import argv

MAX_CLOTHING = 2
MAX_STATIONARY = 3

clothing = ['TSHIRT','JACKET','CAP']
clothing_rs = [1000,2000,500]
clothing_dis = [10,5,20]
stationary = ['NOTEBOOK','PENS','MARKERS']
stationary_rs = [200,300,500]
stationary_dis = [20,10,5]
mytable = [['Item','Quantity','Discount applied','Price after discount']]

def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    total_cost = 0
    for i in Lines:
        i = i.split(' ')
        if i[0] == 'ADD_ITEM':
            if i[1] in clothing:
                if int(i[2]) <= MAX_CLOTHING:
                    dis = clothing_dis[clothing.index(i[1])]
                    rs = clothing_rs[clothing.index(i[1])]
                    actual_price = int(i[2]) * rs
                    total_cost += actual_price
                    applied_dis = (actual_price * dis)//100
                    temp = actual_price-applied_dis
                    mytable.append([i[1],i[2],applied_dis,temp])
                    print('ITEM_ADDED')
                else:
                    print('ERROR_QUANTITY_EXCEEDED')
            else:
                if int(i[2]) <= MAX_STATIONARY:
                    dis = stationary_dis[stationary.index(i[1])]
                    rs = stationary_rs[stationary.index(i[1])]
                    actual_price = int(i[2]) * rs
                    total_cost += actual_price
                    applied_dis = (actual_price * dis)//100
                    temp = actual_price-applied_dis
                    mytable.append([i[1],i[2],applied_dis,temp])
                    print('ITEM_ADDED')
                else:
                    print('ERROR_QUANTITY_EXCEEDED')
        else:
            total_dis = 0
            total_price = 0
            
            for i in range(1,len(mytable)):
                total_dis += mytable[i][2]
                total_price += mytable[i][3]
            if total_price >= 3000:
                total_dis += (total_price * 5)//100
                total_price -= (total_price * 5)//100
            if total_cost >= 1000:
                total_price += (total_price * 10)//100
                print(f'TOTAL_DISCOUNT {total_dis:.2f}')
                print(f'TOTAL_AMOUNT_TO_PAY {total_price:.2f}')
            else:
                total_cost += (total_cost * 10)//100
                print(f'TOTAL_DISCOUNT 0.00')
                print(f'TOTAL_AMOUNT_TO_PAY {total_cost:.2f}')
        
if __name__ == "__main__":
    main()
