def get_move(step_number):
    body_parts = ["left hand", "right hand", "left foot", "right foot"]
    move_types = ["crimp", "sidepull", "pinch", "sloper", "pocket", "jug", "gaston"]

    print(f"\nMove {step_number}:")
    print("Select a body part or type 'done' to finish:")
    for i, part in enumerate(body_parts, 1):
        print(f"{i}. {part}")

    body_choice = input("Enter the number for the body part: ").strip()

    if body_choice.lower() == "done":
        return None  # Exit input loop

    body_part = body_parts[int(body_choice) - 1]

    # If the body part is a hand, ask for the move type
    move_type = None
    if body_part in ["left hand", "right hand"]:
        print("\nSelect a move type:")
        for i, move in enumerate(move_types, 1):
            print(f"{i}. {move}")

        move_choice = int(input("Enter the number for the move type: ")) - 1
        move_type = move_types[move_choice]

    return {
        "step": step_number,
        "body_part": body_part,
        "move_type": move_type  # Will be None for foot moves
    }

def main():
    moves = []
    print("Climbing Move Logger - Type 'done' at any time to finish.\n")

    step_number = 1  # Keeps track of move order

    while True:
        move = get_move(step_number)
        if move is None:  # User typed 'done'
            break
        
        moves.append(move)

        if move["move_type"]:
            print(f"Registered Move {move['step']}: {move['body_part']} -> {move['move_type']}\n")
        else:
            print(f"Registered Move {move['step']}: {move['body_part']}\n")

        step_number += 1  # Increment step number only when a move is added

    # Display the moves in order
    print("\nFinal Move Sequence:")
    for move in moves:
        move_description = f"{move['step']}. {move['body_part']}"
        if move["move_type"]:
            move_description += f" -> {move['move_type']}"
        print(move_description)

if __name__ == "__main__":
    main()
