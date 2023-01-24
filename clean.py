import string

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


def balance_teams_function(PLAYERS):
    num_players_team = len(PLAYERS) / len(TEAMS)
    num_players_team = int(num_players_team)
    size = num_players_team
    tracker = 0
    team_players = {}
    for team in TEAMS:
        team_players[team] = PLAYERS[tracker:num_players_team]
        tracker += size
        num_players_team += size
    return team_players

def decide_function():
    choice = input("Enter an option between A or B:").upper().strip()
    return choice

def display_teams():
    identification = list(string.ascii_uppercase)
    team_and_identication = {}
    for i, team in enumerate(TEAMS):
        print(f"{identification[i]}) {team}") 

        team_and_identication[identification[i]] = team 

    choice = input(f"Enter an option between {identification[0]} to {identification[len(team_and_identication) - 1]}, \n").upper().strip()
    selected_team = None
    while choice not in team_and_identication:
        choice = input(f"Enter an option between {identification[0]} to {identification[len(team_and_identication) - 1]}, \n").upper().strip()
        
    if choice:
        selected_team = team_and_identication[choice]
    else:
        print('Wrong selection, please between A, B, or C:')
    
    return selected_team

def split_guardian(list_of_guardian):
    save_guardians = ''
    for guardian in list_of_guardian:
        save_guardians = save_guardians + guardian + ', '

    return save_guardians

def continue_function():
    choice = input("Please type CONTINUE to continue... or random key to quit: ").upper().strip()
    return choice


def start_game():
    print("BASKETBALL TEAM STATS TOOL \n") 
    print("---- MENU---- \n")
    print("Here are your choices:")
    print("\t A) Display Team Stats")
    print("\t B) Quit")
    
    decision = decide_function()
    while decision not in ['A', 'B']:
        print('again')
        print("Please choose between A or B:")
        decision = decide_function()

    if decision == "A":
        team_selected = display_teams()
        print(team_selected)
        while team_selected == None:
            team_selected = display_teams()

        clean_players = clean_data_players(PLAYERS)
        balance_team = balance_teams_function(clean_players)
        team_stat_to_display = balance_team[team_selected]
        print(f'Team {team_selected} stat')
        print('--------------------------')

        select_team_len = len(team_stat_to_display)
        num_of_experience = 0
        num_of_inexperience = 0
        sum_height = 0
        save_players_name = "\t"
        guardians = '\t'
        

        for player in team_stat_to_display:
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

        to_continue = continue_function()

        while to_continue == 'CONTINUE':
            print('Display new game stat')     
            start_game() 

        print("Thank you, have a nice day.")

        quit()

    elif decision.upper().strip() == 'B':
        print("You decided to quit, have a nice day")
        quit()

if __name__ == '__main__':
    start_game()

