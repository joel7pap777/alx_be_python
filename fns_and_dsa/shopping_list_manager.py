def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
 shopping_list = []
 while True:
     display_menu()
     choice=  int(input('enter your choice:'))
     if choice == 1:
       user_input = input('nter the item to add:')
       if user_input.isdigit():
         user_input= int(user_input)
       shopping_list.append(user_input)
       print(f"you have added {user_input} to shopping list")
       
     elif choice == 2:
       user_input = input('what item do you want to remove:')
       shopping_list.remove(user_input)
       print(f"you have removed {user_input} from shopping list")
       
     elif choice == 3:
      print(shopping_list)
     
     elif choice == 4:
       print('Good bye!')
       break
   
     else:
      print('Invalid choice. Please try again.')
     
main() 
    
    
             
    
