def get_move():
    body part = ['left hand', 'right hand', 'left leg', 'right leg']

    print('\nSelect a body part:')
    for i, part in enumerate(body_parts, 1):
        print(f'{i}. {part}')

    body_choice = int(input('Enter the number for the body part: ')) - 1
    body_part = body_parts[body_choice]

    print('\nSelect a move type:')
    for i, move in enumerate(move_types, 1):
        print(f'{i}. {move}')

    move_choice =  int(input('Enter the number for the move type: ')) - 1
    move_type = move_types[move_choice]

    return {'body_part': body_part, 'move_type': move_type}

def main():
    moves = []
    print('Climbing Move Logger - Type "Done" at any time to finish.\n')

    while True:
        move = get move()
        moves.append(move)
        print(f'Registered move: {move["body_part"]} -> {move["move_type"]}\n')

        cont = input('Add another move? (y/n): ').strip().lower()
        if cont != 'y':
            break

    print('\nFinal move sequence:')
    for i, move in enumerate(move, 1):
        print(f'{i}. {move["body_part"]} -> {move["move_type"]}')

if __name__ == '__main__':
    main()
