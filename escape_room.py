
inventory = []
current_room = "living_room"

torch_has_battery = False
has_key = False
locker_opened = False
saw_riddle = False
candle_melted = False

def show_inventory():
    print("\n inventory: ", inventory)

def move(room):
    global current_room
    current_room = room


# rooms

def living_room():
    global torch_has_battery

    print("\n you are in the living room")
    print("Options: inspect/ go kitchen / go bedroom / go studyroom")

    #if they saw the riddle, give them a hint
    if saw_riddle and not candle_melted:
        print("Hint: u remember the riddle about burning... must check inventory")

    choice = input("> ").lower()

    if choice == "inspect":
        print("there is sofa and shelf what u want to inspect? sofa / shelf?:")
        sub=input("> ").lower()

        if sub=="sofa":
            print('u r infront of sofa want to lift pillow to check or check side table?:')
            s=input("> ").lower()

            if s=="pillow":
                if "torch" not in inventory:
                    print("u have found a torch (no battery)")
                    inventory.append("torch")
                else:
                    print("nothing new")

            elif s=="table":
                if "battery" not in inventory:
                    print("u found a battery")
                    inventory.append("battery")
                else:
                    print("nothign new")

        elif sub=="shelf":
            print('just books')

    elif choice.startswith("go"):
        dest=choice.split()[1]

        if dest in ["kitchen", "bedroom", "studyroom"]:
            move(dest)
        else:
            print("can't go there")

    elif choice == "use":
        use_items()
        
    elif choice=='use battery':
        if torch_has_battery:
            print("torch already working")
        elif 'torch' in inventory and 'battery' in inventory:
            print('u put battery in torch. torch works now')
            torch_has_battery = True
        else:
            print("u dont have both items")

    elif choice == 'inventory':
        show_inventory()

def bedroom():
    global has_key

    print("\n Bedroom is dark")

    if not torch_has_battery:
        print("Too dark! You stumble back to the living room.")
        move("living_room") # Send them back so they aren't stuck!
        return
    
    print("with torch u see a drawer")
    print("options: inspect/back")
    choice = input("> ").lower()

    if choice == "inspect":
        if not has_key:
            print("y found a small key")
            inventory.append("key")
            has_key=True
        else:
            print("nothing else")
    
    elif choice == "back":
        move("living_room")


def kitchen():
    print("\n kitchen")
    print("options: counter / fridge / back")
    ch=input("> ").lower()

    if ch=="counter":
        if "matchstick" not in inventory:
            print("u found matchstick")
            inventory.append("matchstick")
        else:
            print("nothing new")

    elif ch=="fridge":
        if "candle" not in inventory:
            print("u found wax bear candle")
            inventory.append("candle")

        else:
            print("nothing new")

    elif ch=="back":
        move("living_room")


def studyroom():
    global locker_opened, saw_riddle

    print("\n u r in study room now, there is a locker")
    print("option: open locker / back")
    ch = input("> ").lower()

    if ch=="open locker":
        if "key" in inventory:
            if not locker_opened:
                print("locker opened")
                print('clue: "To reach heaven, I must burn in hell"')
                locker_opened=True
                saw_riddle=True
        else:
                print("need a key")
            
    elif ch=="back":
            move("living_room")
        

# item use

def use_items():
    global candle_melted,saw_riddle

    print("use what?")
    item = input("> ").lower()

    if item == "matchstick":
        if "candle" in inventory:
            print("you burn the candle... wax melts")
            print("a key appears inside")
            inventory.append("final_key")
            candle_melted=True
        else:
            print("nothing to burn")


# game loop
def game():
    print("escape room game started")

    while True:
        if "final_key" in inventory:
            print("\n*** YOU FOUND THE HIDDEN KEY IN THE WAX! ***")
            print("You unlocked the front door and escaped! YOU WIN!")
            break

        if current_room == "living_room":
            living_room()

        elif current_room == "bedroom":
            bedroom()
        elif current_room == "kitchen":
            kitchen()
        elif current_room == "studyroom":
            studyroom()

        

game()