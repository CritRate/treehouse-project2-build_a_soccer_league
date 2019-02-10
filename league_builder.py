import csv


def welcome(player, team):
    # transform name to all lowercase with whitespace as underscore ending with .txt
    fname = '_'.join(player['Name'].lower().split(' ')) + '.txt'

    fhandle = open(fname, 'w')

    fhandle.write('Dear {}'.format(player['Guardian Name(s)']) + '\n')
    fhandle.write('Player name: {}'.format(player['Name']) + '\n')
    fhandle.write('Team name: {}'.format(team.upper()) + '\n')
    fhandle.write('Date and Time of first practice 27.5.2025 10:00' + '\n')
    fhandle.close()


def write_teams(teams):
    fhandle = open('teams.txt', 'w')

    for team in teams:
        fhandle.write('{}'.format(team['team_name']) + '\n')
        fhandle.write('-------' + '\n')
        for player in team['team']:
            fhandle.write('{}, {}, {}'.format(
                player['Name'], player['Soccer Experience'], player['Guardian Name(s)']) + '\n')
            # welcome txt file for extra credit
            welcome(player, team['team_name'])
        fhandle.write('-------' + '\n\n')

    fhandle.close()


if __name__ == "__main__":

    # create teams as dictionary
    sharks = {'team': list(), 'team_name': 'sharks'}
    raptors = {'team': list(), 'team_name': 'raptors'}
    dragons = {'team': list(), 'team_name': 'dragons'}
    player_exp = list()
    player_nonexp = list()

    with open('soccer_players.csv', newline='') as players:
        csvPlayers = csv.DictReader(players)
        # sort players by experience
        for player in csvPlayers:
            if player['Soccer Experience'] == 'YES':
                player_exp.append(player)
            else:
                player_nonexp.append(player)

    # evenly divide players
    for _ in range(0, 3):
        sharks['team'].append(player_exp.pop())
        raptors['team'].append(player_exp.pop())
        dragons['team'].append(player_exp.pop())
        sharks['team'].append(player_nonexp.pop())
        raptors['team'].append(player_nonexp.pop())
        dragons['team'].append(player_nonexp.pop())

    # write txt file with teams
    write_teams((sharks, raptors, dragons))
