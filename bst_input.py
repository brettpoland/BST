from bst import BSTNode
bst = BSTNode()

def base_set():
    
    n = input("Enter number set: ")
    base_set.base = n.split()
    return base_set.base    

def display():
    nums = base_set.base

    for num in nums:
        bst.insert(num)
    print("preorder:")
    print(bst.preorder([]))
    print("#")

    print("postorder:")
    print(bst.postorder([]))
    print("#")

    print("inorder:")
    print(bst.inorder([]))
    print("#")

def get_menu_choice():
    def print_menu():       
        print(30 * "-", "Options", 30 * "_")
        print("1. Enter value for entry")
        print("2. Enter value for deletion")
        print("3. Display orders")
        print("4. Re-enter base values for tree")
        print("5. Exit")
        print(80 * "-")

    loop = True
    int_choice = -1

    while loop:       
        print_menu()    
        choice = input("Enter your choice [1-5]: ")

        if choice == '1':
            add_int = input("Enter value to add:")
            bst.insert(add_int)
            int_choice = 1
            loop = True

        elif choice == '2':

            remove_int = input("Enter value to delete: ")
            bst.delete(remove_int)
            loop = True
        elif choice == '3':
            choice = ''
            display()
            int_choice = 3
            loop = True
        elif choice == '4':
            base_set()
            int_choice = 4
            loop = True
        elif choice == '5':
            int_choice = -1
            print("Exiting..")
            loop = False  
        else:
            input("Wrong menu selection. Enter any key to try again..")
    return [int_choice, choice]

base_set()
print(get_menu_choice())




