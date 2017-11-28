
def checkio(game_result):
    rotated_field = zip(*game_result)
    for row in game_result: 
        if row[0] == row[1] == row[2] and row[0] != ".":
            return row[1]
    for row in rotated_field:
        if row[0] == row[1] == row[2] and row[0] != ".":
            return row[0]     
    if game_result[0][0] == game_result[1][1]==game_result[2][2] and game_result[0][0] != ".":
        return game_result[0][0]
    elif game_result[0][2] == game_result[1][1]==game_result[2][0] and game_result[0][2] != ".":
        return game_result[0][2]
    else:
        return "D"
            
            
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

