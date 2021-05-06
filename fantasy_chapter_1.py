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
weapon_name_first = ['A', 'Ag', 'Ar', 'Ara', 'Anu', 'Bal', 'Bil', 'Boro', 'Bern', 'Bra', 'Cas', 'Cere', 'Co', 'Con',
    'Cor', 'Dag', 'Doo', 'Elen', 'El', 'En', 'Eo', 'Faf', 'Fan', 'Fara', 'Fre', 'Fro', 'Ga', 'Gala', 'Has',
    'He', 'Heim', 'Ho', 'Isil', 'In', 'Ini', 'Is', 'Ka', 'Kuo', 'Lance', 'Lo', 'Ma', 'Mag', 'Mi', 'Mo',
    'Moon', 'Mor', 'Mora', 'Nin', 'O', 'Obi', 'Og', 'Pelli', 'Por', 'Ran', 'Rud', 'Sam',  'She', 'Sheel',
    'Shin', 'Shog', 'Son', 'Sur', 'Theo', 'Tho', 'Tris', 'U', 'Uh', 'Ul', 'Vap', 'Vish', 'Ya', 'Yo', 'Yyr']

weapon_name_second = ['ba', 'bis', 'bo', 'bus', 'da', 'dal', 'dagz', 'den', 'di', 'dil', 'din', 'do', 'dor', 'dra',
    'dur', 'gi', 'gauble', 'gen', 'glum', 'go', 'gorn', 'goth', 'had', 'hard', 'is', 'ki', 'koon', 'ku',
    'lad', 'ler', 'li', 'lot', 'ma', 'man', 'mir', 'mus', 'nan', 'ni', 'nor', 'nu', 'pian', 'ra', 'rak',
    'ric', 'rin', 'rum', 'rus', 'rut', 'sek', 'sha', 'thos', 'thur', 'toa', 'tu', 'tur', 'tred', 'varl',
    'wain', 'wan', 'win', 'wise', 'ya']

# Player starting attributes
playerHP = 20
unarmed = 1
name = 'Traveler'

def generate_weapon_name():
    return random.choice(weapon_name_first) + random.choice(weapon_name_second)

def slowType(t, mu=0.055, sigma=0.07):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(abs(random.gauss(mu, sigma)))
    print('')


def displayIntro():
    print('The chilling wind bites but the midday sun is shining strong and '
          'reinvigorates our adventurer...')
    print('\nIt is day four on the seven-day trek to Mount Emcae')
    print('\nWith every step, your joints ache - the metronomic click in '
          'your left knee mere seconds before the tin cup and heirloom '
          'compass clang in your satchel')
    print('\nYou try not to remind yourself that the easiest part of the '
          'journey is only just ending and the remaining days will demand '
          'what willpower you have left... still you muster your strength '
          'and carry on')
    print('\nThe tip of Mount Emcae disappears in the far horizon as '
          'the roofs of the tall trees begin to shroud vision of your '
          'destination')
    print('\nRays of sunlight sprinkle through the gaps of the branches and '
          'leaves but are soon shielded completely')
    print('\nA loud scream splits through the silence of the whistling branches, '
          '"HEEEELP!"')
    choice_1()

def choice_1():
    print('\nDo you run toward the cries for help?\n[yes | no]\n')

    response_1 = input('>>> ')

    if response_1 in response_yes:
        print('You run toward the howling...')
        print('\nAs you approach the scene, you begin to hear monstrous hissing '
              'woven between the breaks in the loud cries')
        print('\nTwo juvenile forest spiders circle a shadowy figure')
        print('\nA tingling wave stampedes up your arm as the hairs shoot up')
        print('(Spiders don\'t get this big back home...)')
        choice_2()
    elif response_1 in response_no:
        print('You run away!')
        theCoward()
    else:
        print(invalid_response)
        choice_1()

def choice_2():
    print('\nAre you sure you want to help the stranger?\n[yes | no]\n')

    response_2 = input('>>> ')

    if response_2 in response_yes:
        print('You take out your trusty slingshot, place an acorn in its sling, and '
              'let loose...')
        acornCheck()
    elif response_2 in response_no:
        print('You run away!')
        theCoward()
    else:
        print(invalid_response)
        choice_2()

def acornCheck():
    acornHit = random.randint(1,5)
    if acornHit > 4:
        print('\nDirect hit!')
        print('\nThe acorn strikes one of the spiders in the abdomen '
              'and they quickly retreat into the dark forest')
        theMajismith()
    else:
        print('\nYou missed...')
        print('\nThe acorn darts pass the spider as it shifts its attention on you')
        print('\nIt scurries towards you...')
        print('\nYou leap to your left as it blurs past you into the dark forest')
        print('\nLuck is on your side but you still manage to be slashed by '
            'spider\'s iron-like barbed hairy legs')
        print('\nYou take 1 damage')
        print('Your [HP]: ' + str(playerHP-1))

        theMajismith()

def theMajismith():
    print('\n[Stranger]: "Thank the heavens! You saved my behind. '
          'Those eight-legged beasts almost had me for lunch!"')
    print('\nYou nod at the stranger')
    print('\nThe stranger reaches out her hand and raises her hood to reveal her greenish face')
    print('\nYour slingshot slips out of your palms as you stumble backwards')
    print('\n"You-you-you\'re..."')
    print('\n[Majismith]: "... a Majismith. And you - you are the brave traveler '
        'who took on two spiderlings with a stick and an acorn."')
    print('\n"The stick has a sling on it."')
    print('\nYou stand up off the ground and reach out your hand')
    print('\n"Sorry, I\'ve just never seen a Majismith before"')
    print('\n[Majismith]: "I get that a lot..."')
    print('\nAs you shake the Majismith\'s hand, her eyes begin to widen')
    print('\n[Majismith]: "You aren\'t headed to the mountain, are you?"')
    print('\n"I am"')
    print('\n[Majismith]: "With a stick and a pile of acorns?"')
    print('\n"A stick with a sling"')
    print('\n[Majismith]: "Ah-yes, and a sling"')
    print('\nThe Majismith reaches deep into her pockets and pulls out a golden wand')
    print('\nShe begins to draw a circle around herself while chanting under her breath')
    print('\nYou lean in to try and make out the words')
    print('\n[Majismith]: "You might want to take a few steps back"')
    print('\nYou take several large steps back')
    print('\n(Fwahhh!) The Majismith erupts in a combusting flare and vanishes before your eyes')
    print('\n(Was that an actual Majismith?! They hardly leave the highforge... '
        'I wonder what she was doing this far from the capitol)')
    print('\n(Fwahhh!) You feel a wave of heat tide over you as the Majismith reappears with a locked satchel')
    print('She drops the satchel in front of you')
    print('\n[Majismith]: "You\'ve a rough journey ahead, traveler."')
    print('\nYou look down at the bag, then back towards the Majismith')
    print('\n[Majismith]: "It\'s enchanted. You must answer its riddle.')
    print('\nYou bend down and inspect the enchanted padlock that fastens '
        'itself around the black satchel')
    print('\nThe symbols are not of any language you can recognize')
    print('\n[Majismith]: "Oh, I forgot. You\'ll need this..."')
    print('\nShe hands you a monocle with the same kind of swirling symbols etched in its wire ring')
    print('\nYou hold the monocle between your dominant eye and the glowing lock')
    print('\n[Enchanted Lock]: I am a mother\'s child and a father\'s '
        'child but nobody\'s son. What am I?')

    riddle_1_answers = ['A Daughter', 'Daughter']
    counter = 0

    while counter < 3:
        response = input('>>> ').title()

        if response in riddle_1_answers:
            print('The majismith gazes at you with glee')
            print('\nThe lock turns to ash')
            time.sleep(2)
            print('\nYou lean forward and look inside the open bag')
            print('\nThree weapons lay before you')
            print('\n[Majismith]: "Choose wisely brave one."')
            chooseWeapon()

        else:
           counter += 1
           print('You have ' + str(3-counter) + ' attempts left!')

    print('The lock begins to shake vigorously...')
    print('It begins turning molten red as the bag begins smoking until it is turned into ash')
    print('The lock - still steaming - lies still in the dirt as if it were mocking you')

def theCoward():
    print('\nAs you sprint away from the cries for help and the sunlight '
    'trickles back onto your skin and you find yourself at the edge of the forest')
    print('\nThe only way to the mountain cuts directly through the now '
          'echos of pain and agony, the screams have ceased...')
    print('\nYou mustn\'t abandon your quest now. '
        'Turn back around and continue toward the mountain...')
    print('\nYou slowly make your way back deeper into the woods where you see '
          'bloody trail leading into the darkest corners of the forest. All '
          'that remains is a glowing blue bag. You open the bag and get a glimpse of '
          'the most beautiful battlegear you have ever seen as all the equipment '
          'in the bag turn to dust and evaporate into the air.')

    global unarmed
    unarmed = 1

    matronSpider()

def chooseWeapon():
    print('\n\nWhich do you choose?')
    print('A. sword')
    print('B. dagger')
    print('C. staff')

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
        weapon = 'staff'
        playerClass = 'mage'
        print('You have chosen the staff, clever ' + playerClass + '.')
        weaponOrigins()
    else:
        print(invalid_response)
        chooseWeapon()

def weaponOrigins():
    print('\n[Magismith]: "A most excellent selection, traveler. Your new ' + weapon + ' will surely '
        ' protect you against any spiderlings you may come across. ')
    print('\nThe ' + weapon + ' begins to rattle in your hand')
    print('\n[Magismith]: "And it likes you too"')
    print('[Magismith]: "Much more than your stick and sling, no doubt"')
    print('(What\'s she got against my slingshot?)')
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
    weapon_name = generate_weapon_name()


    print('\n"Hello ' + name.capitalize() + '. I am '
          + weapon_name + '."')
    time.sleep(2)
    print('\nYou look up but the Majismith is nowhere to be seen')
    print('\n"Where did she go?", you wonder.')
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
        print('\nThe ' + enemy + ' does ' + str(enemyHit) + ' damage to you.')
        playerHP = playerHP - enemyHit
        print('[' + name.capitalize() + ' HP]: ' + str(playerHP))
        time.sleep(1.5)
        if playerHP >= 1:
            playerHit = random.randint(1,2) * hitMultiplier
            print('\nYou do ' + str(playerHit) + ' damage to the ' + enemy + '.')
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
    enemyHP = 30

    print('\nA giant spider with two smaller spiders on its back approaches...')
    print('(The two forest spiders that fled before!)')

    if unarmed == 0:
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
