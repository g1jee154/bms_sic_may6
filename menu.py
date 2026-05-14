import node

class BST:
    def __init__(self):
        self.headc = None

def insert(bst):
    new_node = node.Node()
    new_node.data = int(input("Enter data of the new node"))
    

def delete():
    print("element deleteed: ")

def update():
    print("element updateed: ")

def display():
    print("element displayed: ")

def exit():
    print("element exited: ")



def get_menu(choice):
    menu = {
        1 : insert,
        2 : delete,
        3 : update,
        4 : display,  
        5 : exit
    }

    return menu[choice]


def run_menu():
    count = 0
    while True:
        print("1:insert  2:deletr  3:update. 4:display  5:exit")
        choice = int(input("your choice: "))
        get_menu(choice)()
        count += 1
        if choice == 5 or count == 10:
            break
    return 0

run_menu()