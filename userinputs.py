games = ["Fallout 4", "Fallout 76", "Call of Duty", "Warzone", "Black Ops",
         "OverWatch", "For Honor", "Star Wars: The Fallen Order"]

for game in games:
    print ("%s" % games)

add = input("Type in a game: ")
if add not in games: games.append(add)
else: print("Game already in the list! ")
print(games)