inventory=[]


def start():
    print("Welcome to this adventure")
    print("You are an engineer in a mine")
    print("Your move options are North, South, East or West, to pick up an item type grab, to use an item type use")
    print("Your job is to fix any machinery that is broken, Have fun!")
    print("You wake up in your room, the mine seems to be running on emergency power. Time to earn your pay")
    answer=input("Move South to head further into the mine")
    if answer == "south":
        equip_rack()
    else:
        print("Your only valid movement option is south, please try again")

def equip_rack():
    global inventory
    if "light" in inventory:
        print("You probably don't need anything else here")
        answer=input("You can move North back to the starting area or South to go further into the mine")
        if answer== "north":
            start_area()
        elif answer== "south":
            boss_mess_area()
        else:
            print("Not a valid input")
    else:
        print("Your equipment is stored here, if the power is out, you might want to grab your flashlight")
        answer=input("You can move North back to the starting area or South to go further into the mine")
        if answer== "north":
            start_area()
        elif answer== "south":
            boss_mess_area()
        elif answer == "grab":
            flashlight()
        else:
            print("Not a valid input")
            
def flashlight():
    print("You got your flashlight")
    inventory.append("light")
    equip_rack()

def start_area():
    print("You get a message from your boss")
    print("TRYING TO TAKE A NAP, GET BACK TO WORK!")
    answer=input("move south to get back to work")
    if answer== "south":
        equip_rack()
    else:
        print("Not a valid input")
            
def boss_mess_area():
    print("You get a message from your boss")
    print("THE MINE'S GENERATOR HAS BROKEN DOWN, DO YOUR JOB AND GO FIX IT!")
    answer=input("move south to enter the mine proper, move north to go back to your equipment rack")
    if answer== "north":
        equip_rack()
    elif answer=="south":
        mine_proper_1()
        
def mine_proper_1():
    if "light" in inventory:
        print("A door to the south leads to the mining tunnels, a door to the east lead to the drill tunnel")
        answer=input("move south to go to the tunnels, move east to go to the drill")
        if answer== "south":
            tun_n_ent()
        elif answer == "east":
            drill_ent()
        else:
            print("Not a valid input")
    else:
        print("Because the generator is down you can't see anything")
        answer=input("move north to go back to your room")
        if answer=="north":
            equip_rack()
        else:
            print("Not a valid input")
            
def tun_n_ent():
    print("These are the old mining tunnels, who knows what's still down here")
    answer=input("You can move south to go further into the tunnels or north through a door")
    if answer== "north":
        mine_proper_1()
    elif answer=="south":
        tunnel_intersect()
    else:
            print("Not a valid input")

def tunnel_intersect():
    print("The center of the mines, with tunnels going in every direction")
    answer=input("There is a tunnel going every direction, choose one")
    if answer=="north":
        tun_n_ent()
    elif answer=="south":
        tun_s_entrence()
    elif answer=="west":
        west_tun()
    
        

start()