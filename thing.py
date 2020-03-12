import mysql.connector, csv


class Player:
    def __init__(self, raw_data):
        self.attributes = {'First Name': raw_data[0], 'Last Name': raw_data[1], 'Team Name': raw_data[60],
                           'Team Nickname': raw_data[61], 'Aggression': raw_data[9],
                           'Bravery': raw_data[10], 'Determination': 0, 'Teamplayer': 0,
                           'Leadership': 0, 'Temperament': 0, 'Professionalism': 0,
                           'Mental Toughness': raw_data[16], 'Goalie Stamina': raw_data[17], 'Acceleration': raw_data[18],
                           'Agility': raw_data[19], 'Balance': raw_data[20], 'Speed': raw_data[21], 'Stamina': raw_data[22],
                           'Strength': raw_data[23], 'Fighting': raw_data[24], 'Screening': raw_data[25],
                           'Getting Open': raw_data[26], 'Passing': raw_data[27], 'Puck Handling': raw_data[28],
                           'Shooting Accuracy': raw_data[29], 'Shooting Range': raw_data[30],
                           'Offensive Read': raw_data[31], 'Checking': raw_data[32], 'Faceoffs': raw_data[33],
                           'Hitting': raw_data[34], 'Positioning': raw_data[35], 'Shot Blocking': raw_data[36],
                           'Stickchecking': raw_data[37], 'Defensive Read': raw_data[38], 'G Positioning': raw_data[39],
                           'G Passing': raw_data[40], 'G Pokecheck': raw_data[41], 'Blocker': raw_data[42],
                           'Glove': raw_data[43], 'Rebound': raw_data[44], 'Recovery': raw_data[45],
                           'G Puckhandling': raw_data[46], 'Low Shots': raw_data[47], 'G Skating': raw_data[48],
                           'Reflexes': raw_data[49]}
        self.attributes['TPE'] = self.calculate_tpe()

    def calculate_tpe(self):
        tpe_total = 0
        for value in self.attributes.values():
            if isinstance(value, int) == True:
                current_level = 0
                while value > 17:
                    value -= 1
                    current_level += 1
                tpe_total += (current_level * 40)
                current_level = 0
                while value > 15:
                    value -= 1
                    current_level += 1
                tpe_total += (current_level * 25)
                current_level = 0
                while value > 13:
                    value -= 1
                    current_level += 1
                tpe_total += (current_level * 15)
                current_level = 0
                while value > 11:
                    value -= 1
                    current_level += 1
                tpe_total += (current_level * 8)
                current_level = 0
                while value > 9:
                    value -= 1
                    current_level += 1
                tpe_total += (current_level * 5)
                current_level = 0
                while value > 7:
                    value -= 1
                    current_level += 1
                tpe_total += (current_level * 2)
                current_level = 0
                while value > 5:
                    value -= 1
                    current_level += 1
                tpe_total += (current_level * 1)
                current_level = 0
        return tpe_total


def main():
    mydb = mysql.connector.connect(
        host="192.168.10.53",
        user="user",
        passwd="password",
        database="fhm6"
    )


    mycursor = mydb.cursor()

    mycursor.execute("SELECT fhm6.player_master.`First Name`, fhm6.player_master.`Last Name`, fhm6.player_ratings.*, fhm6.team_data.Name, fhm6.team_data.Nickname, fhm6.league_data.Name AS Expr1 \
                      FROM fhm6.player_ratings \
                      INNER JOIN fhm6.player_master \
                        ON fhm6.player_ratings.PlayerId = fhm6.player_master.PlayerId \
                          INNER JOIN fhm6.team_data \
                            ON fhm6.player_master.TeamId = fhm6.team_data.TeamId \
                              INNER JOIN fhm6.league_data \
                                ON fhm6.team_data.LeagueId = fhm6.league_data.LeagueId \
                                  ORDER BY fhm6.league_data.Name")

    myresult = mycursor.fetchall()

    player_list = list()
    count = 0
    for x in myresult:
        player = Player(x)
        player_list.append(player.attributes)
        count += 1
    csv_file = 'fhm6_all_players.csv'
    csv_columns = player_list[0].keys()
    with open(csv_file, 'w+', encoding='utf-8-sig', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in player_list:
            writer.writerow(data)
    print(count)

main()