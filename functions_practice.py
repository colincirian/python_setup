def hello():
    print("Hello user") 
hello()


def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]
print(pack("arg1", "arg2", "arg3"))


def eat_lunch(lunch_items):
    if len(lunch_items) == 0:
        print("My lunchbox is empty!")
    else: 
        print(f"First I eat {lunch_items[0]}")
        for item in lunch_items[1:]:
            print(f"Next I eat {item}")

lunch_items_list = ["granola", "banana", "sandwich", "kiwi", "oatmeal"]
eat_lunch(lunch_items_list)

          