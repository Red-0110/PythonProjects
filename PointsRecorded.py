#Defining a dictionary to map strokes to their corresponding integers
stroke_map = {
    0: "Ace",
    1: "Double fault",
    2: "Forehand",
    3: "Backhand",
    4: "Dropshot",
    5: "Forehand Volley",
    6: "Backhand Volley",
    7: "Smash"
    }

#Create separate lists to store points for each player

player1_log = []
player2_log = []

#Create a list to store how points are scored
point_log = []
print('Tennis Point Tracker')
print('Enter the number corresponding to the stroke used to win the point:')
for key, value in stroke_map.items():
    print(f"{key}: {value}")

while True:
    try:
        #Ask user which player scored the point
        player = input("\nWho scored the point? (Enter '1' for Player 1, '2' for Player 2, or '-1' to finish): ").strip()

        if player == '-1': #Exit loop
            break
        elif player not in ['1', '2']:
            print('Invalid input. Please enter appropriate integer.')
            continue
        
        #Ask user for integer
        point = int(input("How was the point scored?"))

        if point in stroke_map:
            if player == '1':
                player1_log.append(point)
                print(f'Player 1 scored with: {stroke_map[point]}')
            elif player == '2':
                player2_log.append(point)
                print(f'Player 2 scored with: {stroke_map[point]}')
        else:
            print("Invalid input. Please enter a valid stroke number.")
    except ValueError:
        print("Invalid input.")

#Function to summarize points for a player

def summarize_points(log, player_name):
    print(f'\n{player_name} Summary:')
    if log:
        for stroke, count in {stroke: log.count(stroke) for stroke in set(log)}.items():
            print(f'{stroke_map[stroke]}: {count} points')
    else:
        print('No points recorded.')

#Summarize points for both players
summarize_points(player1_log, "Player 1")
summarize_points(player2_log, "Player 2")
