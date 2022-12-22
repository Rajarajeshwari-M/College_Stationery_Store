from sys import argv

def main():
    # Sample code to read inputs from the file
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    lines = lines[:-1]
    '''if product == 'TSHIRT':
        OP = 1000
    if product == 'JACKET':
        OP = 2000
    if product == 'CAP':
        OP = 500
    if product == 'NOTEBOOK':
        OP = 200
    if product == 'PENS':
        OP = 300
    if product == 'MARKERS':
        OP = 500'''
    word_list = []
    Original_P_T = 0
    Original_P_J = 0
    Original_P_C = 0
    Original_P_N = 0
    Original_P_P = 0
    Original_P_M = 0
   
    dis_applied_T = 0 
    dis_applied_J = 0 
    dis_applied_C = 0 
    dis_applied_N = 0 
    dis_applied_P = 0
    dis_applied_M = 0
    total = 0
    total_dis = 0
    total_dis_T = 0
    total_dis_J = 0
    total_dis_C = 0
    total_dis_N = 0
    total_dis_P = 0
    total_dis_M = 0
    total_after_dis = 0
    grand_total = 0
    New_P_T = 0
    New_P_J = 0
    New_P_C = 0
    New_P_N = 0
    New_P_P = 0
    New_P_M = 0
    New_Total = 0
    
    for line in lines:
        # Add your code here to process input commands.
        #word_list = [word for word in line.split()]
        word_list = line.split()
        #print(word_list)
        l1 = ['TSHIRT', 'JACKET', 'CAP']
        l2 = ['NOTEBOOK','PENS','MARKERS']
        #print(len(l1))
        tot = 0
        #wor_len = len(word_list[1])
        #if wor_len == 0:
        #    pass
        total1 = 0
        total2 = 0
        if word_list[1] in l1:
            if int(word_list[2]) > 2:
                print("ERROR_QUANTITY_EXCEEDED")
                tot = tot+0
            else:
                print("ITEM_ADDED")
                if word_list[1] == 'TSHIRT':
                    Original_P_T = 1000
                    tot = Original_P_T * int(word_list[2])
                if word_list[1] == 'JACKET':
                    Original_P_J = 2000
                    tot = Original_P_J * int(word_list[2])
                if word_list[1] == 'CAP':
                    Original_P_C = 500
                    tot = Original_P_C * int(word_list[2])
            total1 = total + tot
        if word_list[1] in l2:
            if int(word_list[2]) > 3:
                print("ERROR_QUANTITY_EXCEEDED")
            else:
                print("ITEM_ADDED")
                if word_list[1] == 'NOTEBOOK':
                    Original_P_N = 200
                    tot = Original_P_N * int(word_list[2])
                if word_list[1] == 'PENS':
                    Original_P_P = 300
                    tot = Original_P_P * int(word_list[2])
                if word_list[1] == 'MARKERS':
                    Original_P_M = 500
                    tot = Original_P_M * int(word_list[2])
            total2 = total + tot
        total = total1 + total2
        #print("total = ",total)
        
    
    if(total > 1000):
        for line in lines:
            word_list = line.split()
            if word_list[1] == 'TSHIRT':
                dis_Price_T = 0.1 * Original_P_T
                dis_applied_T = int(word_list[2]) * dis_Price_T
                #total_dis = total_dis + dis_applied_T 
                New_P_T = int(word_list[2])*Original_P_T - dis_applied_T
            if word_list[1] == 'JACKET':
                dis_Price_J = 0.05 * Original_P_J
                dis_applied_J = int(word_list[2]) * dis_Price_J
                #total_dis = total_dis + dis_applied_J
                New_P_J = int(word_list[2])*Original_P_J - dis_applied_J
            if word_list[1] == 'CAP':
                dis_Price_C = 0.2 * Original_P_C
                dis_applied_C = int(word_list[2]) * dis_Price_C
                #total_dis = total_dis + dis_applied_C
                New_P_C = int(word_list[2])*Original_P_C - dis_applied_C
            if word_list[1] == 'NOTEBOOK':
                dis_Price_N = 0.2 * Original_P_N
                dis_applied_N = int(word_list[2]) * dis_Price_N
                #total_dis = total_dis + dis_applied_N
                New_P_N = int(word_list[2])*Original_P_N - dis_applied_N
            if word_list[1] == 'PENS':
                dis_Price_P = 0.1 * Original_P_P
                dis_applied = int(word_list[2]) * dis_Price_P
                #total_dis = total_dis + dis_applied_P
                New_P_P = int(word_list[2])*Original_P_P - dis_applied_P
            if word_list[1] == 'MARKERS':
                dis_Price_M = 0.05 * Original_P_M
                dis_applied_M = int(word_list[2]) * dis_Price_M
                #total_dis = total_dis + dis_applied_M
                New_P_M = int(word_list[2])*Original_P_M - dis_applied_M
        New_Total = New_P_T + New_P_J + New_P_C + New_P_N + New_P_P + New_P_M
        total_dis = dis_applied_T + dis_applied_J + dis_applied_C + dis_applied_N + dis_applied_P + dis_applied_M
        
   
    
    
              
    if(total > 3000):
        dis_P = 0.05 * total
        total_dis = total_dis + dis_P
            
    total_after_dis = New_Total - total_dis
        
    sales_tax = 0.1 * total_after_dis
        
    grand_total = total_after_dis + sales_tax
        
    
        #output = "TOTAL_DISCOUNT %d \n TOTAL_AMOUNT_TO_PAY %d", #process the input command and get the output
        # Once it is processed print the output using the command System.out.println()
    print("TOTAL_DISCOUNT ",total_dis)
    print("TOTAL_AMOUNT_TO_PAY ",grand_total)
    
    f.close()
    
if __name__ == "__main__":
    main()