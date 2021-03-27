import random

MAX_STEP = 100
NUMBER_OF_LADDERS = 3
NUMBER_OF_SNAKES = 3

class Player: # help keep track of player state and positions.
    def __init__(self, CurrentPosition, CurrentState):
        self.CurrentPosition = CurrentPosition
        self.CurrentState = CurrentState

class Game: # help keep track of game settings (ladder and snake positions, and num. of rolls)
    def __init__(self, Ladders, Snakes):
        self.Ladders = Ladders
        self.Snakes = Snakes
        self.Rolls = 0

def initialize_game_obj(): # returns a game object with randomized ladders and snakes positions.
    def rand_choose(used_nums, large_first): # returns positions of either snake head/butt or top/bottom of ladder.
        larger_num = random.randrange(3, MAX_STEP)
        while larger_num in used_nums:
            larger_num = random.randrange(3,MAX_STEP)

        smaller_num = random.randrange(2, larger_num)
        while smaller_num in used_nums:
            smaller_num = random.randrange(2, larger_num)

        used_nums.append(smaller_num)
        used_nums.append(larger_num)

        if large_first == True: # because positions of snakes are in the format of [higher_val, lower_val]
            return (larger_num, smaller_num)
        return (smaller_num, larger_num)

    used_nums = [None] # keeps a record of all the positions that are occupied by ladder and snake heads/butts.
    Ladders = []
    Snakes = []
    for num in range(0,NUMBER_OF_LADDERS): # appends positions to list.
        Ladders.append(rand_choose(used_nums, False))
    for num in range(0, NUMBER_OF_SNAKES):
        Snakes.append(rand_choose(used_nums, True))

    return Game(Ladders, Snakes)

def initialize_player_obj(): # returns a player obj. with starting parameters
    return Player(0, "AtHome")

def make_changes_to_game(GameObject, PlayerObject): # roll a die and make changes to game progress base on die value.
    print("Pressed 1, rolling a die")
    die_val = random.randrange(1, 7)
    print(f"Dice value: {die_val}")

    if die_val == 6 and PlayerObject.CurrentState != "RoamFree": # once the first 6 is obtained, change state to RoamFree.
        PlayerObject.CurrentState = "RoamFree"

    msg = None # msg variable helps the main function to know if player encountered ladder/snake so the program can print corresponding statement.
    if PlayerObject.CurrentState == "RoamFree":
        new_pos = PlayerObject.CurrentPosition + die_val
        for tuples in GameObject.Ladders: # check if ladder bottom is reached, if it is, change new_pos to the top of ladder.
            if new_pos == tuples[0]:
                new_pos = tuples[1]
                msg = "laddered"
        for tuples in GameObject.Snakes: # check if snake head is reached, if it is, change new_pos to snake tail.
            if new_pos == tuples[0]:
                new_pos = tuples[1]
                msg = "snaked"
        if new_pos <= 100: # this helps make sure that new_pos will never exceed 100.
            PlayerObject.CurrentPosition = new_pos

    return msg

def game(): # main function
    def game_board_status(GameObject, PlayerObject): # prints game status before die is rolled.
        print(f"------------------------- Total Dice rolls before this: {GameObject.Rolls} --------------------------------------")
        print(f"Ladders: {GameObject.Ladders}")
        print(f"Snakes: {GameObject.Snakes}")
        print(f"CurrentPosition: {PlayerObject.CurrentPosition}")
        print(f"CurrentState: {PlayerObject.CurrentState}")
    def game_board_results(PlayerObject, msg = None): # prints result from rolling a die.
        def get_msg_str(msg):
            if msg == "snaked":
                return " (Since it is bit by a snake)"
            elif msg == "laddered":
                return " (Since it gets a ladder)"
            return ""
        print("")
        print("After the dice is rolled:")
        print(f"CurrentPosition: {PlayerObject.CurrentPosition}" + get_msg_str(msg))
        print(f"PlayerState: {PlayerObject.CurrentState}")
        if PlayerObj.CurrentPosition == 100:
            print("\nHurray you won!! Bye bye :)") 
        print("---------------------------------------------------------------")
    def game_board_user_choice(): # gets user choice.
        user_input = "0"
        while user_input not in "12" or len(user_input) != 1:
            user_input = input("Press 1 to roll a die and 2 to exit!!")
        return user_input

    GameObj = initialize_game_obj()
    PlayerObj = initialize_player_obj()

    while PlayerObj.CurrentPosition != 100:
        game_board_status(GameObj, PlayerObj)
        user_input = game_board_user_choice()
        if user_input == "2":
            print("\nGoodbye!")
            quit()
        GameObj.Rolls += 1
        msg = make_changes_to_game(GameObj, PlayerObj)
        game_board_results(PlayerObj, msg)

if __name__ == '__main__':
    game()