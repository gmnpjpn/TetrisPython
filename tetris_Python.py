from enum import Enum
import keyboard

class Movement(Enum):
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    ROTATE = 4

# My tetris game will have a 10x10 screen so it will be represented by list called "screen".
# The cells will be represented as arrays inside "screen".
# (The number of arrays will the number of rows, 10 in this case)
def tetris():
    screen = [["⬛", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
              ["⬛", "⬛", "⬛", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
              ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
              ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
              ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
              ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
              ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
              ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
              ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
              ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"]]

    print_screen(screen)
    
    rotation = 0
    
    while(True):
        event = keyboard.read_event()
        
        if event.name == "esc":
            break
        elif event.event_type == keyboard.KEY_DOWN:
            if event.name == "flecha abajo":
                (screen, rotation) = move_piece(screen, Movement.DOWN, rotation)
            elif event.name == "flecha derecha":
                (screen, rotation) = move_piece(screen, Movement.RIGHT, rotation)
            elif event.name == "flecha izquierda":
                (screen, rotation) = move_piece(screen, Movement.LEFT, rotation)
            elif event.name == "space":
                (screen, rotation) = move_piece(screen, Movement.ROTATE, rotation)

def move_piece(screen: list, movement: Movement, rotation: int) -> (list, int):
    
    # Creates a blank screen
    new_screen = [["⬜"] * 10 for _ in range(10)]
    
    rotation_item = 0
    # The possible changes in position for the piece
    rotations = [[(1, 1), (0, 0), (-2, 0), (-1, -1)],
                 [(0, 1), (-1, 0), (0, -1), (1, -2)],
                 [(0, 2), (1, 1), (-1, 1), (-2, 0)],
                 [(0, 1), (1, 0), (2, -1), (1, -2)]]
    
    new_rotation = rotation
    
    # It changes the index of the rotation (0 = 0 degrees // 3 = 270 degrees)
    if movement is Movement.ROTATE:
        new_rotation = 0 if rotation == 3 else rotation + 1
    
    for row_index, row in enumerate(screen):
        for column_index, item in enumerate(row):

            if item == "⬛":
                new_row_index = 0
                new_column_index = 0

                match movement:
                    case Movement.DOWN:
                        new_row_index = row_index + 1
                        new_column_index = column_index

                    case Movement.RIGHT:
                        new_row_index = row_index
                        new_column_index = column_index + 1

                    case Movement.LEFT:
                        new_row_index = row_index
                        new_column_index = column_index - 1
                        
                    case Movement.ROTATE:
                        new_row_index = row_index + rotations[new_rotation][rotation_item][0]
                        new_column_index = column_index + rotations[new_rotation][rotation_item][1]
                        rotation_item += 1

                if new_row_index > 9 or new_column_index > 9 or new_column_index < 0:
                    print("\nYou can't do that movement")
                    return (screen, rotation)
                else:
                    new_screen[new_row_index][new_column_index] = "⬛"
                
    print_screen(new_screen)
    return (new_screen, new_rotation)

def print_screen(screen: list):
    print("\nTetris Screen:\n")
    
    for row in screen:
        print("".join(map(str, row)))


# I call the function tetris
tetris()