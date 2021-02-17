#Krista Miller
#2/17/2020
# This game is called Mille Bornes, which is French for "a thousand
# milestones".  The premise of the game is that 2 players are in a
# road race.  Each race- or hand- is 1000 miles long.  There
# are hazard, remedy, safety, and distance cards.  Each hazard
# is corrected by a corresponding remedy, and can be prevented
# from happening in the first place by a corresponding safety.
# The target distance is reached by playing distance cards.

# Card List:
# distance: 25 mile(10), 50 mile(10), 75 mile(10), 100 mile(12), 200 mile(4)
# hazards: accidents (3), out of gas (3), flat tire(3)
# remedies: repairs(6), gasoline(6), spare tire(6)
# safeties: driving ace(1), fuel tank(1), puncture proof(1),right of way(1)

import copy
import random

# 1: Building the deck of cards:
class Distance:
    def __init__(self, distance):
        self.distance = distance
        
    def __str__(self):
        return f"Distance Card - {self.distance}"

# building distance cards:
Mile25 = Distance(25)
Mile50 = Distance(50)
Mile75 = Distance(75)
Mile100 = Distance(100)
Mile200 = Distance(200)

class Hazards:
    def __init__(self, hazard, remedy):
        self.hazard = hazard
        self.remedy = remedy

    def __str__(self):
        return f'Hazard Card - {self.hazard}'

# building hazard cards:
Accident = Hazards('accident', 'repair')
Out_of_Gas = Hazards('out of gas', 'gasoline')
Flat_Tire = Hazards('flat tire', 'spare tire')

# print(Flat_Tire.remedy)

class Remedies:
    def __init__(self, hazard, remedy):
        self.hazard = hazard
        self.remedy = remedy

    def __str__(self):
        return f'Remedy Card - {self.remedy}'

# building remedy cards:
Repair = Remedies('accident', 'repair')
Gasoline = Remedies('out of gas', 'gasoline')
Spare_Tire = Remedies('flat tire', 'spare tire')

#TODO ignore for now because it is hard
class Safeties:
    def __init__(self, safety, hazardimmunity):
        self.safety = safety
        self.hazardimmunity = hazardimmunity

    def immunity(self):
        return '{} card is immune from {} card'.format(self.safety, self.hazardimmunity)

# building safety cards
Driving_Ace = Safeties('driving ace', Accident.hazard)
Fuel_Tank = Safeties('fuel tank', Out_of_Gas.hazard)
Puncture_Proof = Safeties('puncture proof', Flat_Tire.hazard)

# testing cards:
# print(Puncture_Proof.immunity())
# print(Out_of_Gas.__dict__)

def get_default_deck():
    default_deck = []

    # Distance cards
    distance_25 = Distance(25)
    for i in range(10):
        default_deck.append(copy.copy(distance_25)) # Example of a shallow copy

    for i in range(10):
        default_deck.append(Distance(50))

    for i in range(10):
        default_deck.append(Distance(75))

    for i in range(12):
        default_deck.append(Distance(100))

    for i in range(4):
        default_deck.append(Distance(200))

    # Hazard cards
    for i in range(3):
        default_deck.append(Hazards('accident', 'repair'))

    for i in range(3):
        default_deck.append(Hazards('flat tire', 'spare tire'))

    for i in range(3):
        default_deck.append(Hazards('out of gas', 'gasoline'))

    # Remedy cards
    for i in range(6):
        default_deck.append(Remedies('accident', 'repair'))

    for i in range(6):
        default_deck.append(Remedies('flat tire', 'spare tire'))

    for i in range(6):
        default_deck.append(Remedies('out of gas', 'gasoline'))

    return default_deck

TARGET_DISTANCE = 1000

def main():
    #0. build large deck
    deck = get_default_deck()
    random.shuffle(deck)
    
    # 1. build decks
    deck1 = []
    deck2 = []

    for i in range(5):
        deck1.append(deck.pop())
        deck2.append(deck.pop())

    # 2. declare our distances and declare blocks(hazards)
    distances = [0, 0]
    blocks = [None, None]

    # 3. while loop until one person gets > 1000 miles
    def player_play_routine(player):
        other_player = 0 if player == 1 else 0

        # Prompt player to play
        print("\n----------------------------------")
        print(f"PLAYER {player} TURN: PLAY A CARD BY SELECTING NUMBER")
        print("DISTANCE TOTALS:", distances)
        print("----------------------------------")
        target_deck = deck1 if player == 1 else deck2

        # While no card is played or they didn't select pass, keep asking to play a card
        target_idx = -1
        player_passed = False
        while target_idx == -1:
            # Print list of cards
            # card is an alias for each card in deck
            # target_deck is also an alias for the current deck of interest
            for index, card in enumerate(target_deck):
                print(f"{index}. {str(card)}")
            print(f"{index+1}. PASS")

            # Need to check that value is int
            print("Which card do you want to play?")
            card_idx = int(input())

            # target card is an alias
            if card_idx == index+1:
                player_passed = True
                break
            target_card = target_deck[card_idx]
            if isinstance(target_card, Distance) and blocks[player] is None:
                # if a distance card is played, then add to total distance
                #isinstance function checks if the object is an instance of the
                #specified class or not
                distances[player] += target_card.distance
                target_idx = card_idx
            elif isinstance(target_card, Hazards):
                # mark the other player as blocked
                if blocks[other_player] is None:
                    blocks[other_player] = target_card
                    target_idx = card_idx
            elif isinstance(target_card, Remedies):
                # verify that you are blocked and that this would fix your block
                if blocks[player] is not None and blocks[player].remedy == target_card.remedy:
                    blocks[player] = None
                    target_idx = card_idx

        # Remove that card from the deck
        if not player_passed:
            del target_deck[card_idx]

        # Draw a card
        target_deck.append(deck.pop())

    player_turn = 0
    while distances[0] < TARGET_DISTANCE and distances[1] < TARGET_DISTANCE:

        player_play_routine(player_turn)
        player_turn = 0 if player_turn == 1 else 1

    if distances[0] >= TARGET_DISTANCE:
        print("PLAYER 0 WINNER!!")
    else:
        print("PLAYER 1 YOU ARE THE BEST!!")

main()
