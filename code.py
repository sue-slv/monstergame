from random import randint

score = {}
player = {'name': 'name', 'attack': 'random', 'health': 100, 'heal': 'random'}
monster = {'attack': 'random', 'health': 100}

print('>>>>>>>>>>>>>>>> STARTING THE GAME <<<<<<<<<<<<<<<<')

remain_health_m = 0
remain_health_p = 0

def action_player(remain_health_m, remain_health_p, monster, player, score):
    player['name'] = str(input('What is your name?: ').upper())
    print('Ok! The game is starting... Are you ready, ' + player['name'] + '?')

    while monster['health'] > 0 and player['health'] > 0:
        print('===================== ACTION ======================')
        print('What do you want to do?')
        action = input('[1] Attack; [2] Heal; [3] Winners; [4] Exit: ')
        print('---------------------------------------------------')

        if action == '1' or action == '2':
            if action == '1':
                damage_m = randint(1, 25)
                remain_health_m = monster['health'] - damage_m
                monster['health'] = remain_health_m

                damage_p = randint(1, 25)
                remain_health_p = player['health'] - damage_p
                player['health'] = remain_health_p

                if damage_m > damage_p:
                    print('You was stronger than the Monster this time!')
                elif damage_p > damage_m:
                    print('Oh, oh! The monster was stronger than you this time!')
                else:
                    print('Oddly, you both lost the same amount of health in this round')

                print('The monster lost [' + str(damage_m) + '] points with your attack')
                print('It attacked back and you lost [' + str(damage_p) + '] points')

            else:
                healing_p = randint(1, 15)
                remain_health_p = player['health'] + healing_p
                player['health'] = remain_health_p
                print('You healed yourself and recovered ' + str(healing_p) + ' points!')

            print('Current score: ' + player['name'] + ' [' + str(player['health']) + '] x [' + str(monster['health']) + '] MONSTER')

        elif action == '3':
            print('WINNERS')
            if len(score) == 0:
                print('So far there is no winner')

            else:
                for key, value in score.items():
                    print(str(key) + ' won ' + str(value) + ' game(s)')

        elif action == '4':
            print('===================================================')
            print('Schade Marmelade! Good Bye!')
            print('GAME END')
            print('===================================================')
            quit()

        else:
           print('Invalid input. Type 1, 2, 3 or 4')

    if monster['health'] > player['health'] or monster['health'] < player['health']:
        if monster['health'] > player['health']:
            print('===================================================')
            print('GAME OVER')
            print('Sorry for you! The Monster won!')
            print('===================================================')

        else:
            print('===================================================')
            print('END OF THE GAME')
            print('Good Job! You won!')
            print('===================================================')

            if player['name'] not in score.keys():
                score[player['name']] = 1

            else:
                score[player['name']] = score[player['name']] + 1


        print('>>>>>>>>>>>>>>> RESTARTING THE GAME <<<<<<<<<<<<<<<')
        monster['health'] = 100
        player['health'] = 100
        action_player(remain_health_m, remain_health_p, monster, player, score)

action_player(remain_health_m, remain_health_p, monster, player, score)
