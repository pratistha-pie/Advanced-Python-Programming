# Cricket Team Management System
class Player:
    def __init__(self, name, jersey_number, runs):
        self.name = name
        self.jersey_number = jersey_number
        self.runs = runs

    def category(self):
        if self.runs >= 1000:
            return "Excellent"
        elif self.runs >= 500:
            return "Good"
        else:
            return "Average"

    def display(self):
        print("Player Name:", self.name)
        print("Jersey Number:", self.jersey_number)
        print("Runs:", self.runs)
        print("Category:", self.category())
        print("------------------------")

class Team:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_all(self):
        print("\n--- All Player Details ---")
        for player in self.players:
            player.display()

team = Team()

n = int(input("Enter number of players: "))

for i in range(n):
    print("\nEnter Player", i + 1, "Details")

    name = input("Enter Player Name: ")
    jersey = int(input("Enter Jersey Number: "))
    runs = int(input("Enter Runs: "))

    player = Player(name, jersey, runs)
    team.add_player(player)

team.display_all()