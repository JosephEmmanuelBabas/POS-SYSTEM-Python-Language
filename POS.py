import os


def getint (prompt = 'Enter here: '):
    while True:
        userinput = input(prompt)
        if userinput.isdigit():
            return int(userinput)
        else:
            print('INVALID INPUT')

def outofstock(quantity,num1,num2):
    if quantity[num1][num2] <= 0:
         n: str = 'out of stock'
         return n
    else:
         m: str = 'have stock'
         return m

def cancelling(number):
    for i in range(0,5):
        print(i)



category: list[str] = ["BREAD", "PASTRIES", "CAKES", "COOKIES", "SAVORY TREATS"]
product1: list[str]  = [["Sourdough Loaf", "Baguette", "Multigrain Bread", "Focaccia", "Dinner Rolls (6 pcs)"],
                      ["Croissant", "Cinnamon Roll", "Danish", "Muffin", "Palmier"],
                      ["Chocolate Cake", "Carrot Cake", "Cheesecake", "Red Velvet Cake", "Mango Cake"],
                      ["Chocolate Chip Cookie", "Oatmeal Raisin Cookie", "Double Chocolate Cookie", "Peanut Butter Cookie", "White Chocolate Cookie"],
                      ["Ham and Cheese Croissant", "Spinach Sandwich", "Chicken Empanada", "Sausage Roll", "Beef Empanada"]]
productprice1: list[int] =  [[120, 90, 150, 130, 150],
                                [80, 85, 90, 95, 100],
                                [150, 140, 170, 160, 150],
                                [50, 45, 55, 50, 60],
                                [160, 150, 130, 140, 150]]
productquantity: list[int] = [[10, 10, 10, 10, 10],[10, 10, 10, 10, 10],[10, 10, 10, 10, 10],[10, 10, 10, 10, 10],[10, 10, 10, 10, 10]]
totalamt: float = 0
categ: int = 0
prod: int = 0
quantity: int = 0
re_order: int = 1
cash: float = 0
checkout: int = 0 

print('WELCOME TO MY STORE STORE!')

num = getint()
print(num)


Cart: list[str] = []
while True:
    
    
    os.system('cls')    # clearing screen function                        
    print('')
    print('')
    print('=======================')
    print('HERE IS MY MENU OPTION')
    print('=======================')
    print('1. ALL MENU')
    print('2. INVENTORY')
    print('3. PLACE ORDER')
    print('4. CART')
    print('5. CHECK OUT ORDER')
    print('X. (EXIT)')
    print('=======================')
    print('=======================')
    print('')


    option: int = input('Choose a number of your choice: ').lower()
    while option == '1':
# MENU SHOWING SYSTEM        
        if option == '1':
            for i in range(0,5):
                print('=====================================')
                print(f'{category[i].ljust(30)} PRICES')
                print('=====================================') 
                for p in range(0,5):
                    print(f'{product1[i][p].ljust(30)}Php.: {float(productprice1[i][p])}')
            print('=====================================')
            user_input = input("press Enter to go back to menu): ")
            break    

# INVETORY SHOWING SYSTEM
    while option == '2':
            print('===================================================================================')
            print('================================= INVENTORY =======================================')
            print('STOCK VAL ========== CATEGORY ============= PRODUCT ======================== QTY')
            
            for i in range(0,5):
                for p in range(0,5):
                    updater_stock = outofstock(productquantity,i,p)
                    print(f'{updater_stock.ljust(21)} {category[i].ljust(20)} {product1[i][p].ljust(30)} Stocks:{productquantity[i][p]}')
            print('===================================================================================')
            print('===================================================================================')
            user_input = input("press Enter to go back to menu): ")
            break
# PLACE ORDERING SYSTEM
    while option == '3':
        if re_order == 1: 
            print('Would you like to Order? ')
            order: int = getint('Press [1] Yes | [2] No: ')
            if order == 1:
                for i in range(0,5):
                    print(f'{i + 1}. {category[i]}')
            
            elif order == 2:
                break
            else:
                print('invalid input')# valid input checker
                continue
            while re_order == 1:    
                if re_order == 1:
                    while categ == 0 or categ == 1 or categ == 2 or categ == 3 or categ == 4 or categ == 5: 
                        print('') 
                        categ: int = getint('Please Choose a number 1-5 category you want to order: ')   
                        if categ == 1 or categ == 2 or categ == 3 or categ == 4 or categ == 5:
                            for i in range(0,5):
                                print(f'{i + 1}. {product1[categ - 1 ][i].ljust(25)} | Php. {productprice1[categ - 1][i]: <10} | Stock {productquantity[categ - 1][i]}')

                            if productquantity[categ - 1][0] == 0 and productquantity [categ - 1][1] == 0 and productquantity[categ - 1][2] == 0 and productquantity[categ - 1][3] == 0 and productquantity[categ - 1][4] == 0:
                                print('All product in this category is out of stock please choose other category')# IT SHOWS IF THE CATEGORY IS OUT OF STOCK
                                categ = 0
                                continue
                            break
                            
                        else:
                            print('Please enter only 1-5')
                            categ = 0
                            continue
                    while prod == 0 or prod == 1 or prod == 2 or prod == 3 or prod == 4 or prod == 5: 
                        print('') 
                        prod: int = getint('Please Choose a number 1-5 Product you want to order:')
                        if prod == 1 or prod == 2 or prod == 3 or prod == 4 or prod == 5:
                            if productquantity[categ - 1][prod - 1] != 0:# Indexing the product
                                print('')
                                print('==================== Your Current Order ====================')
                                print(f'{product1[categ - 1][prod - 1].ljust(25)}| Php. {productprice1[categ - 1][prod - 1]}  | Stock {productquantity[categ - 1][prod - 1]}')
                                print('===========================================================')
                                break
                            elif productquantity[categ - 1][prod - 1] == 0:# It shows if the product is out of stock
                                for i in range(0,5):
                                    print(f'{i + 1}. {product1[categ - 1 ][i].ljust(25)} | Php. {productprice1[categ - 1][i]: <10} | Stock {productquantity[categ - 1][i]}')
                                print(f'{product1[categ - 1][prod - 1]} is Out of stock please other product')
                                continue
                        else:
                            print('Please enter only 1-5')# valid input checker
                            prod = 0
                            continue
                    while quantity <= 0 or quantity > productquantity[categ - 1][prod - 1]:
                        quantity: int = getint('Enter Quantity: ')
                        if quantity > productquantity[categ - 1][prod - 1]:
                            print(f'you cannot buy more than {productquantity[categ - 1][prod - 1]}')
                        
                    productquantity[categ - 1][prod - 1] = productquantity[categ - 1][prod - 1]  - (int(quantity))
                    qty: str = (str(quantity))
                    Cart.append({
                        'Product': product1[categ - 1][prod - 1],
                        'Price': productprice1[categ - 1][prod - 1],
                        'Quantity': qty})
                    total: float = productprice1[categ - 1][prod - 1] * float(quantity)
                    print(total)
                    totalamt += total
                    quantity = 0
                    while True:
                        re_order = getint('[Order again? press 1 if Yes 2 if No]: ')
                        if re_order == 1 or re_order == 2:
                            break
                        else:
                            print('Please enter 1 or 2...')# valid input checker
                            continue
                elif re_order == 2:
                    break
                else:
                    print('Invalid input.')# valid input checker
                    continue
        elif re_order == 2:
            re_order = 1
            break
        else:
            print('Invalid input')# valid input checker
            continue    
            
# VIEWING SYSTEM CART            
    while option == '4':
        print('===========================================================')
        print('=================== CART CURRENT ORDER ====================')
        print('PRODUCT                   PRICES               QTY.    ')
        print('===========================================================')
        if totalamt <= 0:
            print('You dont have any order yet...')
            
        for index, item in enumerate(Cart, start=1):
            print(f'||{index}. {item["Product"].ljust(20)} | Php. {item["Price"]:<10} |qty: {item["Quantity"]}||')
        print(f'TOTAL AMOUNT: {totalamt}')
        print('===========================================================')
        print('===========================================================')
        print('') # cancel oder option here
        user_input = input("press Enter to go back to menu): ")
        break
#CHECK OUT WIH PAYMENT SYSTEM
    while option == '5':
            if checkout == 0:
                checkout: int = getint('DO YOU WANT TO CHECK OUT?: Press [1 - Yes ][2 - No]: ')
            elif checkout == 1 and totalamt <= 0:
                print('You dont have any order yet...')
                checkout = 0
                user_input = input("press Enter to go back to menu): ")
                break
            elif checkout == 2:
                break
            else:
                print('Invalid Input')
                continue
            
            if checkout == 1 and totalamt > 0:
                print('===========================================================')
                print('=================== CHECK OUT THE ORDERS ==================')
                print('PRODUCT                   PRICES               QTY.    ')
                print('===========================================================')
                for index, item in enumerate(Cart, start=1):
                    print(f'||{index}. {item["Product"].ljust(20)} | Php. {item["Price"]:<10} |qty: {item["Quantity"]}||')
                print(f'TOTAL AMOUNT: {totalamt}')
                print('===========================================================')
                print('===========================================================')
                print('')
                while cash < totalamt:
                    cash: float = getint('Please Input your Cash here: ')
                    if cash >= totalamt:
                        change: float = float(cash) - totalamt

                        print('')     
                        print('================================')
                        print('=========== RECIEPT ============')
                        print('')
                        for index, item in enumerate(Cart, start=1):
                            print(f'{index}. {item["Product"]} | Php. {item["Price"]} | qty: {item["Quantity"]}')
                        print('') 
                        print(f'TOTAL AMOUNT: {totalamt}')
                        print(f'CASH: {cash}')
                        print(f'CHANGE: {change}')
                        print('')
                        print('================================')
                        print('================================')
                        
                        totalamt = 0
                        Cart.clear()
                        while True:
                            checkout: int = getint('PLEASE PRESS 1 to go back in menu option... ')
                            if checkout == 1:
                                checkout = 1
                                break
                            else:
                                continue
                    else:
                        print(f'Insufficient Cash please provide this amount: {totalamt}')
                        continue
            elif checkout == 2:
                checkout = 0
                break

    if option == 'x':
        break
    else:
        continue
