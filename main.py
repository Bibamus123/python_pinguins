import random

print(f'Сюжет: Главный герой - обычный крестьянин у феодала.'
      f'\nВ один из дней он решается украсть карту тайника своего феодала.'
      f'\nУ Вовы это получаеться после чего он решаеться сбежать ночью.\n')

print(f'Пока главный герой шёл до тайника, он решил сорвать лопух, чтобы в '
      f'нем нести '
      'драгоценности.'
      '\nПри подходе на метку карты, главный герой увидел небольшой вход в '
      'подземелье.'
      '\nНа входе в подземелье он падает запнувшись, '
      'о ступеньку и праваливается в дыру, кишащую монстрами.'
      '\nИспытание начинается\n')

#Игрок выбирает имя для персонажа
player = input('Choose name for your character: ')

#Список классов
player_classes = ['warrior', 'doctor', 'shield bearer']

#Игрок выбирает класс
player_class = int(input('Choose class of your character ('
                        'warrior - 1 (+15 damage),'
                        'doctor - 2 (+15 HP after level)'
                        'shield bearer - 3 (-10 damage from enemy): )'))

#Базовое и максимальное кол-во здоровья игрока
player_HP = 100
player_max_HP = 100

#Базовое и максимальное кол-во маны игрока и перезарядка маны в ход
player_mana = 100
player_mana_reload = 35
player_max_mana = 100

#Характеристики противников
enemy1 = {'enemy_name': 'Base_enemy', 'enemy_HP': 100, 'enemy_mana': 50,
          'enemy_damage': 20, 'mana_per_attack': 15, 'enemy_mana_reload': 5}

enemy2 = {'enemy_name': 'Hard_enemy', 'enemy_HP': 150, 'enemy_mana': 100,
          'enemy_damage': 30, 'mana_per_attack': 30, 'enemy_mana_reload': 10}

enemy3 = {'enemy_name': 'Smart_monster', 'enemy_HP': 80, 'enemy_mana': 120,
          'enemy_damage': 15, 'mana_per_attack': 15, 'enemy_mana_reload': 10}

enemy4 = {'enemy_name': 'Ringleader', 'enemy_HP': 110, 'enemy_mana': 30,
          'enemy_damage': 35, 'mana_per_attack': 15, 'enemy_mana_reload': 10}


#Список противников
list_of_enemies = [enemy1, enemy2, enemy3, enemy4]

#Список оружия игрока и их характеристик
list_of_weapon = ['sword', 'pistol', 'magic_wand']
power_of_weapon = [35, 55, 75]
mana_of_weapon = [30, 45, 55]

#Кол-во уровней, выбираемое игроком и действительный уровень
number_of_levels = int(input('Choose the number of levels: '))
current_level = 1

#Список действий игрока
list_of_actions = ['attack', 'reload_mana']

#Выбор игрока, показывать ли обучение
tutorial_choose = str(input('Want to see tutorial?(y/n): '))

#Показ обучения в случае согласия
if tutorial_choose == 'y':
    print(f'Hello! This is tutorial.'
          f'\n------------------------------------------'
          f'\n{player} <- This is you  |  This is an enemy -> {enemy1.get("enemy_name")}'
          f'\nYou have HP = {player_HP}'
          f'\nAnd you have mana = {player_mana}'
          f'\nAlso you have different weapons with different properties: '
          f'{", ".join(list_of_weapon)}'
          f'\n------------------------------------------')
else:
    print('Okay')

#Выбор оружия на игру
weapon = int(input('Choose your weapon ('
                   'sword - 1, '
                   'pistol - 2, '
                   'magic_wand - 3): '))

#Сила, выбранного оружия
attack = power_of_weapon[weapon - 1]

#Проверка на класс воина
if player_class == 1:
    attack += 15

#Цикл, отвечающий за кол-во пройденных уровней и результат победы
while number_of_levels != 0 and player_HP > 1:

    #Выбор случайного противника
    enemy = random.choice(list_of_enemies)

    #Характеристики противника
    enemy_name = enemy.get("enemy_name")
    enemy_HP = enemy.get("enemy_HP")
    enemy_mana = enemy.get("enemy_mana")
    enemy_damage = enemy.get("enemy_damage")

    #Проверка на класс бронированного
    if player_class == 3:
        enemy -= 10
    mana_per_attack = enemy.get('mana_per_attack')
    enemy_mana_reload = enemy.get('enemy_mana_reload')

    #Цикл, отвечающий за сам игровой процесс и за результат поражения
    while enemy_HP > 0 and player_HP > 1:

        #Игровой интерфейс
        print(f'------------------------------------------'
              f'\nLevel: {current_level}     |  Enemy: {enemy_name}'
              f'\n{player} HP: {player_HP}  |  {enemy_name} HP: '
              f'{enemy_HP}'
              f'\n{player} mana: {player_mana}  |  {enemy_name} mana: '
              f'{enemy_mana}'
              f'\n------------------------------------------')

        #Выбор действий игрока
        player_action = int(input("Choose an action ("
                                  "attack - 1, "
                                  "reload_mana - 2): "))

        #Проверка на достаточное кол-во маны для атаки и сама атака
        if player_action == 1:
            if player_mana >= mana_of_weapon[weapon - 1]:
                enemy_HP = enemy_HP - attack
                player_mana = player_mana - mana_of_weapon[weapon - 1]
            else:
                print(f'------------------------------------------'
                      f'\nYou have no mana! You will get 10 mana instead of '
                      f'25 '
                      'for mistake!')
                player_mana += 10

        #Восстановление маны игрока
        if player_action == 2:
            player_mana = player_mana + player_mana_reload

        #Проверка хватает ли у противника маны для атаки и сама атака либо
        #перезарядка маны
        if enemy_HP > 0:
            if enemy_mana >= mana_per_attack:
                player_HP = player_HP - enemy_damage
                enemy_mana = enemy_mana - mana_per_attack
            else:
                enemy_mana = enemy_mana + enemy_mana_reload

    #Счётчик уровней
    current_level += 1
    number_of_levels -= 1

    #Восстановление маны, в случае победы
    if player_mana + 45 <= player_max_mana:
        player_mana += 45

    #Проверка на проигрышь и сообщение о нём или в случае победы на уровне,
    #игрок восстановит здоровье
    if player_HP <= 0:
        print('You lost!')
    else:

        #Проверка на класс доктора
        if player_class == 2:
            if player_HP + 25 <= player_max_HP:
                player_HP += 25
        else:
            if player_HP + 10 <= player_max_HP:
                player_HP += 10

#Проверка на победу и сообщение о ней
if player_HP > 0:
    print('Congratulations! You win!')
