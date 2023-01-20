from constants import TEAMS, PLAYERS

def clean_data_players(PLAYERS):
    new_players = []
    for user in PLAYERS:
        new_player = {}
        new_player["name"] = user["name"]
        if "and" in user["guardians"]:
            new_player["guardians"] = user["guardians"].split(" and ")
        else:
            new_player["guardians"] = [user["guardians"]]
        split_height = user["height"].split(" ")
        new_player["height"] = int(split_height[0])
        if user["experience"] == "YES":
            new_player["experience"] = True
        elif user["experience"] == "NO":
            new_player["experience"] = False
        new_players.append(new_player)
    return new_players


def balance_teams_function(players_clean_data):
    num_players_team = len(players_clean_data) / len(TEAMS)
    num_players_team = int(num_players_team)
    size = num_players_team
    tracker = 0
    team_players = {}
    for team in TEAMS:
        team_players[team] = players_clean_data[tracker:num_players_team]
        tracker += size
        num_players_team += size
    return team_players


def decide_function():
    choice = input("Enter an option between A or B ")

    if choice.upper().strip() not in ["A","B"]:
        print("Please choose between A or B")
        decide_function()
    return choice


def continue_function():
    choice = input("Please type CONTINUE to continue..")
    if choice.upper().strip() == "CONTINUE":
        start_game()
    else:
        print("Thank you, have a nice day.")
        quit()


def display_teams():
    print("A) Panthers")
    print("B) Bandits")
    print("C) Warriors")

    selected_team = None
    choice = input("Enter an option between A,B or C ")
    if choice.upper().strip() == "A":
        selected_team = "Panthers"
    elif choice.upper().strip() == "B":
        selected_team = "Bandits"
    elif choice.upper().strip() == "C":
        selected_team = "Warriors"
    else:
        print("Chose between A, B or C")
        display_teams()

    if selected_team is None:
        display_teams()
    return selected_team




def split_guardian(list_of_guardian):
    save_guardians = ''
    for guardian in list_of_guardian:
        save_guardians = save_guardians + guardian + ', '

    return save_guardians

def start_game():
    print("BASKETBALL TEAM STATS TOOL \n") 
    print("---- MENU---- \n")
    print("Here are your choices:")
    print("\t A) Display Team Stats")
    print("\t B) Quit")
    
    decision = decide_function()
    #if decision.upper().strip() == "B":
    #    print("Thank you, have a nice day.")
    #    quit()
    if decision.upper().strip() == "A":
        team_selected = display_teams()
        clean_players = clean_data_players(PLAYERS)
        balance_team = balance_teams_function(clean_players)
        team_stat_to_display = balance_team[team_selected] 
        
        print(f'Team {team_selected} stat')
        print('---------a-----------------')

        select_team_len = len(team_stat_to_display)
        num_of_experience = 0
        num_of_inexperience = 0
        sum_height = 0
        save_players_name = "\t"
        guardians = '\t'


        for player in team_stat_to_display:
            # print(player['guardians'])
            splitted_guardian = split_guardian(player['guardians'])
            guardians = guardians +  splitted_guardian
            save_players_name = save_players_name + player["name"] + ", "
            if player['experience'] == True:
                num_of_experience += 1
            else:
                num_of_inexperience += 1

            sum_height += player['height']

        average_height = sum_height / select_team_len

        print(f'Total players: {select_team_len}')
        print(f'Total experienced: {num_of_experience}')
        print(f'Total inexperienced: {num_of_inexperience}')
        print(f'Average height: {average_height}')

        print("Players on Team: ")
        
        print(save_players_name, end='\n')

        print("Guardians: ")

        print(guardians)

        continue_function()

    else:
        print("You decided to quit, have a nice day")
        quit()
 


if __name__ == '__main__':
    start_game()
