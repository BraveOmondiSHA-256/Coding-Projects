print(r'''
#############################################################################
#(@@@@)                    (#########)                   (@@@@@@@@(@@@@@@@@@#
#@@@@@@)___                 (####)~~~   /\                ~~(@@@@@@@(@@@@@@@#
#@@@@@@@@@@)                 ~~~~      /::~-__               ~~~(@@@@@@@@)~~#
#@@@)~~~~~~                           /::::::/\                  ~~(@@@@)   #
#~~~                              O  /::::::/::~--,                 ~~~~    #
#                                 | /:::::/::::::/{                         #
#                 |\              |/::::/::::::/:::|                        #
#                |:/~\           ||:::/:::::/::::::|                        #
#               |,/:::\          ||/'::: /::::::::::|                       #
#              |#__--~~\        |'#::,,/::::::::: __|   ,,'`,               #
#             |__# :::::\       |-#"":::::::__--~~::| ,'     ',     ,,      #
#,    ,,     |____#~~~--\,'',.  |_#____---~~:::::::::|         ',','  ',    #
# '.,'  '.,,'|::::##~~~--\    `,||#|::::::_____----~~~|         ,,,     '.''#
#____________'----###__:::\_____||#|--~~~~::::: ____--~______,,''___________#
#^^^  ^^^^^   |#######\~~~^^O, | ### __-----~~~~_____########'  ^^^^  ^^^   #
#,^^^^^','^^^^,|#########\_||\__O###~_######___###########;' ^^^^  ^^^   ^^ #
#^^/\/^^^^/\/\^^|#######################################;'/\/\/^^^/\/^^^/\/^#
#   /\/\/\/\/\  /\|####################################'      /\/\/\/\/\    #
#\/\/\     /\/\/\  /\/\/\/\    /\/\/\/\/\   /\/\/\    /\/\/\/\      /\/\/\/\#
#spb\/\/\    /\/\/\/\    /\/\/\/\    /\/\/\/\   /\/\/\/\    /\/\/\/\/\      #
#############################################################################
''')

print("Welcome to Treasure island.")
print("Your mission is to find the treasure.")

choice1 = input('The treasure map is leading you to sail down two different paths, either left or right. '
                'One will lead to riches and spoils, the other to imminent doom. '
                'Only a true pirate will know the bath to choose.'
                'The choice is yours. "left" or "right"? ').lower()

if choice1 == "left":
    choice2 = input('Aye Aye matey! Great choice, pirate blood flows within you. '
                    'But now land ahoy and you have struck pointy rocks. '
                    'The ship is sinking! Do you "swim" ashore or "wait" and rescue the rest of your crew? '
                    'The choice is yours. ').lower()
    if choice2 == "wait":
        choice3 = input('Way to go matey! A true pirate never abandons his crew, '
                        'You are so close now, can almost smell the treasure. '
                        'The map has led you to a hidden passage with three different colored doors, '
                        '"red", "blue and "yellow". only one leads to glory, '
                        'the rest gruesome death, the choice is yours. ').lower()
        if choice3 == "yellow":
            print('Aye Aye! A pirates dream, the fortune and spoils all yours to enjoy. '
                  'Way to go matey, now onto the next adventure!')
        elif choice3 == "red":
            print('OH NO! You\'ve chosen the fiery pit of doom and been scorched to death by the roaring flames. '
                  'This is not a prirate\'s way to perish')
        elif choice3 == "blue":
            print('OH NO! You\'ve chosen the sea monsters layer and been swallowed whole. '
                  'This is not a prirate\'s way to perish')
        else:
            print('OH NO! You\'ve tried to deceive the see by not selecting a valid door, '
                  'and now the cave has collapsed and engulfed you. '
                  'This is not a prirate\'s way to perish')
    else:
        print('OH NO! You coward, you jumped into the sea and abandoned your crew mates to swim to shore '
              'just to be attacked by a hoard of hungry sharks. . '
              'This is not a prirate\'s way to perish')
else:
    print('OH NO! You\'ve chosen the wrong path and steered you and your crew to sure death. '
          'This is not a prirate\'s way to perish')


