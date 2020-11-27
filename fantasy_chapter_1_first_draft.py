import os
import sys
import time
import random



# Possible reponses
response_yes = ['y', 'Y', 'ye','yes', 'ya', 'yea', 'yep', 'yup', 'Yes']
response_no = ['n', 'N', 'no', 'na', 'nah', 'No']
response_a = ['a', 'A']
response_b = ['b', 'B']
response_c = ['c', 'C']
invalid_response = '\nThere is no time, you must choose quickly!\n'

# Randomise two halfs to generate weapon name
name_first = ['A', 'Ag', 'Ar', 'Ara', 'Anu', 'Bal', 'Bil', 'Boro', 'Bern', 'Bra', 'Cas', 'Cere', 'Co', 'Con',
    'Cor', 'Dag', 'Doo', 'Elen', 'El', 'En', 'Eo', 'Faf', 'Fan', 'Fara', 'Fre', 'Fro', 'Ga', 'Gala', 'Has',
    'He', 'Heim', 'Ho', 'Isil', 'In', 'Ini', 'Is', 'Ka', 'Kuo', 'Lance', 'Lo', 'Ma', 'Mag', 'Mi', 'Mo',
    'Moon', 'Mor', 'Mora', 'Nin', 'O', 'Obi', 'Og', 'Pelli', 'Por', 'Ran', 'Rud', 'Sam',  'She', 'Sheel',
    'Shin', 'Shog', 'Son', 'Sur', 'Theo', 'Tho', 'Tris', 'U', 'Uh', 'Ul', 'Vap', 'Vish', 'Ya', 'Yo', 'Yyr']

name_second = ['ba', 'bis', 'bo', 'bus', 'da', 'dal', 'dagz', 'den', 'di', 'dil', 'din', 'do', 'dor', 'dra',
    'dur', 'gi', 'gauble', 'gen', 'glum', 'go', 'gorn', 'goth', 'had', 'hard', 'is', 'ki', 'koon', 'ku',
    'lad', 'ler', 'li', 'lot', 'ma', 'man', 'mir', 'mus', 'nan', 'ni', 'nor', 'nu', 'pian', 'ra', 'rak',
    'ric', 'rin', 'rum', 'rus', 'rut', 'sek', 'sha', 'thos', 'thur', 'toa', 'tu', 'tur', 'tred', 'varl',
    'wain', 'wan', 'win', 'wise', 'ya']

# Player starting attributes
playerHP = ''
unarmed = 1
name = 'Traveler'

def generate_fantasy_name():
    return random.choice(name_first) + random.choice(name_second)

def slowType(t, mu=0.055, sigma=0.07):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(abs(random.gauss(mu, sigma)))
    print('')


def displayIntro():
    slowType('The chilling wind bites but the midday sun is shining strong and '
          'reinvigorates our adventurer...')
    time.sleep(5)
    slowType('\nIt is the day four on the seven-day trek to Mount Emcae')
    time.sleep(2.5)
    slowType('\nWith every step, your joints ache - the metronomic click in '
          'your left knee mere seconds before the tin cup and heirloom '
          'compass clang in your satchel')
    time.sleep(5)
    slowType('\nYou try not to remind yourself that the easiest part of the '
          'journey is only just ending and the remaining days will demand '
          'what willpower you have left... still you muster your strength '
          'and carry on')
    time.sleep(5)
    slowType('\nThe tip of Mount Emcae disappears in the far horizon as '
          'the roofs of the tall trees begin to shroud vision of your '
          'destination')
    time.sleep(5)
    slowType('\nRays of sunlight sprinkle through the gaps of the branches and '
          'leaves but are soon shielded completely')
    time.sleep(3)
    slowType('\nA loud scream splits through the silence of the whistling branches, '
          '"HEEEELP!"')
    choice_1()

def choice_1():
    slowType('\nDo you run toward the cries for help?\n[yes | no]\n')

    response_1 = input('>>> ')

    if response_1 in response_yes:
        slowType('You run toward the howling...')
        time.sleep(2)
        slowType('\nAs you approach the scene, you begin to hear monstrous hissing '
              'woven between the breaks in the loud cries')
        time.sleep(4)
        slowType('\nTwo adult forest spiders circle a shadowy figure')
        time.sleep(4)
        slowType('\nA tingling wave stampedes up your arm as the hairs shoot up')
        slowType('(Spiders don\'t get this big back home...)')
        time.sleep(4)
        choice_2()
    elif response_1 in response_no:
        slowType('You run away!')
        theCoward()
    else:
        print(invalid_response)
        choice_1()

def choice_2():
    slowType('\nAre you sure you want to help the stranger?\n[yes | no]\n')

    response_2 = input('>>> ')

    if response_2 in response_yes:
        slowType('You take out your trusty slingshot, place an acorn in its sling, and '
              'let loose...')
        time.sleep(4)
        acornCheck()
    elif response_2 in response_no:
        print('You run away!')
        theCoward()
    else:
        print(invalid_response)
        choice_2()

def acornCheck():
    acornHit = random.randint(1,10)
    if acornHit > 2:
        print('\nDirect hit!')
        time.sleep(1)
        print('\nThe acorn strikes one of the spiders in the abdomen '
              'and they quickly retreat into the dark forest')
        time.sleep(5)
        theMajismith()
    else:
        print('\nYou missed...')
        time.sleep(1)
        print('\nThe acorn darts pass the spider as it shifts its attention on you')
        time.sleep(2)
        print('\nYou did not survive...')
        print('\nPlay again?\n[yes | no]')

        subresponse = input('>>> ')

        if subresponse in response_yes:
            displayIntro()
            
def theMajismith():
    print('\n[Majismith]: "Blessed be - the savior o\' me - '
          'to be without thee - would\'o been tragedy"')
    print('\n\nHow do you respond?')
    print('''    A. "yup-yuppy" (You've never met an actual Majismith before, but they seem to enjoy rhymes)
    B. "anytime" (Is this an actual Majismith?! They hardly leave the highforge...)
    C. no response (Did you see how big those spiders were?!)''')

    choice = input('>>> ')

    if choice in response_a:
        print('The majismith gazes at you with glee')
        print('\nThe traveling majismith rummages through his bag')
        time.sleep(2)
        print('"A few tools in my bag - for your adventure I may have."')
        print('\nThe majismith presents you with three weapons')
        chooseWeapon()
    elif choice in response_b:
        print('The majismith nods and pulls out a handful of acorns')
    elif choice in response_c:
        print('The majismith stares at you and winces, then suddenly '
              'vanishes into thin air!')
    else:
        print(invalid_response)
        theMajismith()

def theCoward():
    time.sleep(2)
    print('\nAs you sprint away from the cries for help and the sunlight '
    'trickles back onto your skin and you find yourself at the edge of the forest')
    time.sleep(4)
    print('\nThe only way to the mountain cuts directly through the now '
          'echos of pain and agony, the screams have ceased...')
    time.sleep(4)
    print('\nYou must turn back around and continue toward the mountain...')
    time.sleep(2)
    print('\nYou slowly make your way back deeper into the woods where you see '
          'bloody trail leading into the darkest corners of the forest. All '
          'that remains is a glowing blue bag. You open the bag and get a glimpse of '
          'the most beautiful battlegear you have ever seen as all the equipment '
          'in the bag turn to dust and evaporate into the air.')
    time.sleep(5)

    global unarmed
    unarmed = 1
    
    matronSpider()
            
def chooseWeapon():
    print('\n\nWhich do you choose?')
    print('''    A. sword
    B. dagger
    C. wand''')

    global playerClass
    global weapon
    global unarmed
    weapon = input('>>> ')
    unarmed = 0

    if weapon in response_a:
        weapon = 'sword'
        playerClass = 'warrior'
        print('You have chosen the sword, brave ' + playerClass + '.')
        weaponOrigins()
    elif weapon in response_b:
        weapon = 'dagger'
        playerClass = 'rogue'
        print('You have chosen the dagger, cunning ' + playerClass + '.')
        weaponOrigins()
    elif weapon in response_c:
        weapon = 'wand'
        playerClass = 'mage'
        print('You have chosen the wand, clever ' + playerClass + '.')
        weaponOrigins()
    else:
        print(invalid_response)
        chooseWeapon()

def weaponOrigins():    
    print('\n[Magismith]: "A most excellent selection - thy new ' + weapon + ' will provide great '
              'protection"')
    time.sleep(2)
    print('\nIt begins to rattle in your hand')
    time.sleep(2)
    print('\n[Magismith]: "Oh m\'y - what a nuh\'ice - lovely surp\'rice"')
    print('[Magismith]: "The ' + weapon + ' has chosen - O\' oath unbroken"')
    print('\nA small humming begins in your ear')
    time.sleep(4)
    print('\nThe deafining hum grows louder until it is near unbearable '
          'and you drop to your knees')
    time.sleep(3)
    print('(Is this ' + weapon + ' cursed?!)')
    time.sleep(2)
    print('\nAs the loud humming subsides, you hear the Majismith ask:')
    print('[Voice]: "What is your name?"')

    global name
    global weapon_name

    name = input('>>> ')
    weapon_name = generate_fantasy_name()
    

    print('\n"Hello ' + name.capitalize() + '. I am '
          + weapon_name + '."')
    time.sleep(2)
    print('\n"Where did that ironmaker go?", you wonder.')
    print('You realise you are not speaking at all - the thought of your '
          'newly-acquired ' + weapon + ' washes over you as you feel energy '
          'coursing from your fingertips to your chest')
    matronSpider()

def enemyEncounter():
    global name
    global enemy
    global playerHP
    global enemyHP
    global unarmed

    if unarmed == 1:
        hitMultiplier = 1
    else:
        hitMultiplier = 4

    while playerHP >= 1 and enemyHP >= 1:
        enemyHit = random.randint(2,3)
        print('The ' + enemy + ' does ' + str(enemyHit) + ' damage to you.')
        playerHP = playerHP - enemyHit
        print('[' + name.capitalize() + ' HP]: ' + str(playerHP))
        time.sleep(1.5)
        if playerHP >= 1:
            playerHit = random.randint(1,2) * hitMultiplier
            print('You do ' + str(playerHit) + ' damage to the ' + enemy + '.') 
            enemyHP = enemyHP - playerHit
            print('[' + enemy.capitalize() + ' HP]: ' + str(enemyHP))
            time.sleep(1.5)
    
    if enemyHP <= 0:
        print('\nThe ' + enemy + ' has been slain!')
    elif playerHP <= 0:
        print('\nYou did not survive...')
        print('\nPlay again?\n[yes | no]')

        subresponse = input('>>> ')

        if subresponse in response_yes:
            displayIntro()

def choice_fight():
    print('\n\nDo you wish to fight?\n[yes | no]')

    subresponse = input('>>> ')

    if subresponse in response_yes:
        if unarmed == 0:
            print('\nYou raise your ' + weapon)
        else:
            print('\nYou raise your fists')
    elif subresponse in response_no:
        print('\nYou cannot escape the ' + enemy)
    else:
        print(invalid_response)
        choice_fight()

def matronSpider():
    global name
    global enemy
    global weapon_name
    global playerHP
    global enemyHP
    global unarmed
    
    enemy = 'matron spider'
    enemyHP = 8
    playerHP = 8 
    
    print('\nA giant spider with two smaller spiders on its back approaches...')

    if unarmed == 0:
        print('(The two forest spiders that fled before!)')
        print('\n[' + weapon_name + ']: "We can take them"')

    choice_fight()
    time.sleep(3)

    print('\nThe giant spider lunges at you with fangs raised\n')

    enemyEncounter()

    print('\nThe two forest spiders scatter back into the darkness')

    if unarmed == 0:
        if weapon == 'sword':
            print('\nAn electric crackling emits from the sword')        
        elif weapon == 'dagger':
            print('\nA gust of wind begins to envelop around you')
        elif weapon == 'wand':
            print('\nA gravitational pull around you uproots surrounding trees')

        print(weapon_name + ' has awoken!')
        time.sleep(3)

    print('\n\nCongratulations! You have reached the end of Chapter 1: '
          + name.capitalize() + '\'s Beginning')
    print('Thanks for playing!')
    time.sleep(3)
    print('(This terminal will self-destruct in ten seconds)')
    time.sleep(10)

displayIntro()
