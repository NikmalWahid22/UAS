class View : 
    @staticmethod
    def display_menu(): 
        print("\n=== Inventory Management System ===")
        print("1. Add Item")
        print("2. View Item")
        print("3. Exit ")
    
    @staticmethod
    def get_input(prompt, is_float=False): 
        while True: 
            try: 
                user_input = input(prompt)
                if is_float: 
                    return float (user_input)
                else : 
                    return user_input
            except ValueError: 
                print("Invalid Input. Please Try Again. ")
    @staticmethod
    def display_items(items): 
        if items : 
            print("\n === Current Inventory ===")
            print(" Name      |  Quantity |  Price | ")
            print("-------------------------------------")
            for item in items: 
                print(f"{item['name']:<10} | {item['quantity']:<9} | {item['price']:<5}")
        else: 
            print("\n Inventory Is Empty")

        
         

                