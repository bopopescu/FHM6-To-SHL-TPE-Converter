import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Windforce",
  database="fhm6"
)

print(mydb)

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

for x in myresult:
  print(x)