from random import randint

winners = {}
player = {'name': 'name', 'health': 100}
monster = {'name': 'Learning-to-Code', 'health': 100}

print('  ')
print('>' * 28 + ' STARTING THE GAME ' + '<' * 28)
print('Welcome to the Learning-to-Code Monster Game')
print('... based on real life events of a Redi School student and migrant in Germany')
print('  ')
print('Instructions')
print('1. Your goal is to beat the monster that keeps you from learning to code')
print('2. Everytime you attack the monster, the monster counterattacks you')
print('3. The attacks -and its strength- are a bit "random", as some life events')
print('4. You can try to heal to recover some points')
print('5. The best players are registered in the winners table')
print('The game is starting...')
print('  ')


remain_health_m = 0
remain_health_p = 0

def game(remain_health_m, remain_health_p, monster, player, winners):
    player['name'] = str(input('What is your name?: ').upper())
    print('Are you ready, ' + player['name'] + '?')

    while monster['health'] > 0 and player['health'] > 0:

        print('='*31 + ' ACTION ' + '='*32)
        print('What do you want to do?')
        action = input('[1] Attack; [2] Heal; [3] Winners; [4] Exit game: ')
        print('-'*71)

        if action == '1' or action == '2':

            if action == '1':
                # player attacks monster, randomly from 6 options, and damages the monster
                attack_p = randint(1, 6)
                if attack_p == 1:
                    damage_m = randint(1, 5)
                    print('You did your homework from last Redis class')

                elif attack_p == 2:
                    damage_m = randint(5, 10)
                    print('You asked/looked for support to understand something')

                elif attack_p == 3:
                    damage_m = randint(10, 15)
                    print('You attended a Redis class!')

                elif attack_p == 4:
                    damage_m = randint(15, 20)
                    print('You found new sources to learn besides the Redi classes')

                elif attack_p == 5:
                    damage_m = randint(20, 25)
                    print('You debugged something in your code! Uhuuu!')

                else:
                    damage_m = randint(25, 30)
                    print('You coded! As simple as that!')

                remain_health_m = monster['health'] - damage_m
                monster['health'] = remain_health_m

                print(':) The monster lost [' + str(damage_m) + '] points')
                print('   ')

                # the monster attacks back, randomly from 7 options, and damages the player
                attack_m = randint(1, 6)
                if attack_m == 1:
                    damage_p = randint(1, 5)
                    print('Your head is full and you keep confusing the coding syntax')

                elif attack_m == 2:
                    damage_p = randint(5, 10)
                    print('Self-doubt kicked in, and you wonder if you will ever learn how to code')

                elif attack_m == 3:
                    damage_p = randint(10, 15)
                    print('Concerned about your future and your learning success, you procrastinate')

                elif attack_m == 4:
                    damage_p = randint(15, 20)
                    print('Grrrrr! The code is not working! Waruuuuuuuuuuuuum!?')

                elif attack_m == 5:
                    damage_p = randint(20, 25)
                    print('You need to take several tiring-small-underpaid jobs to cover your expenses')
                    print('No coding for a while')

                else:
                    damage_p = randint(25, 30)
                    print('You need to deal with Deutsche Bürokratie or you will lose your permit!')
                    print('No coding for a while')

                remain_health_p = player['health'] - damage_p
                player['health'] = remain_health_p

                print(':( You lost [' + str(damage_p) + '] points')

            else:
                # player tries to heal, from 4 random options
                healing = randint(1, 4)

                if healing == 1:
                    healing_p = 10
                    print('You had a therapy session or talked to a good friend!')
                    print('No self-doubt or procrastination for a while!')

                elif healing == 2:
                    healing_p = 15
                    print('You took a break and did something you enjoy! :)')

                elif healing == 3:
                    healing_p = 20
                    print('After networking with Redi School Community, you are feeling motivated!')

                else:
                    healing_p = 0
                    print('You know that life is not that easy! No healing for you in this round')

                remain_health_p = player['health'] + healing_p
                player['health'] = remain_health_p
                print('You recovered ' + str(healing_p) + ' points!')

            print('  ')
            print('Current score: ' + player['name'] + ' [' + str(player['health']) + '] x [' + str(
            monster['health']) + '] MONSTER')

        elif action == '3':
            # option to see the winners chart
            print('WINNERS')

            # checking if the winners dictionary is empty
            if len(winners) == 0:
                print('So far there is no winner')

            # if it is not empty, iterating to print the winners keys and values
            else:
                for key, value in winners.items():
                    print(str(key) + ' won ' + str(value) + ' game(s)')

        elif action == '4':
            # option to exit the game
            print('='*71)
            print('Schade Marmelade! But do not forget:')
            print('You can play again the Learning-to-Code Monster Game in the future')
            print('GOOD BYE!')
            print('='*71)
            quit()

        else:
            # in case of an invalid input by the user
           print('Invalid input. Type 1, 2, 3 or 4')

    # there is a winner
    if monster['health'] <= 0 or player['health'] <= 0:
        print('-' * 71)

        # monster wins
        if monster['health'] > player['health']:
            print('OH NO! The Monster won! :(')
            print('But you can always try again!')

        # player wins
        else:
            print('UHUUUUUUUUU! You won!')
            print('Learning to code IS possible!')

            # adding new players names (keys) in the winners dictionary
            if player['name'] not in winners.keys():
                winners[player['name']] = 1

            # updating when the players wins (values) in the winners dictionary
            else:
                winners[player['name']] = winners[player['name']] + 1

        print('=' * 71)
        print('  ')
        print('>'*25 + ' RESTARTING THE GAME ' + '<'*25)
        monster['health'] = 100
        player['health'] = 100
        game(remain_health_m, remain_health_p, monster, player, winners)

game(remain_health_m, remain_health_p, monster, player, winners)

