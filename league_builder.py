import csv

if __name__ == "__main__":
    sharks = list()
    raptors = list()
    dragons = list()
    player_exp = list()
    player_nonexp = list()

    with open('soccer_players.csv', newline='') as players:
        csvPlayers = csv.DictReader(players)
        for player in csvPlayers:
            if player['Soccer Experience'] == 'YES':
                player_exp.append(player)
            else:
                player_nonexp.append(player)
    
    