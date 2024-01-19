#hangman but you do trivia to reveal letters, and can guess it at any moment
#you get more points the more letters are hidden when you guess it
#the topics will be movies & video games

import random

#CONSTANTS
GAME_NAME = "Trivia Hangman"

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#WORD CHOICES
MOVIES = ["INTERSTELLAR", "INDIANA JONES", "MISSION IMPOSSIBLE", "JOHN WICK", "OPPENHEIMER", "PULP FICTION",
          "BARBIE", "FINDING NEMO", "TOY STORY", "TERMINATOR", "DIE HARD", "THE HUNGER GAMES", "GODZILLA",
          "THE CREATOR", "THE IMITATION GAME", "HOME ALONE", "AVENGERS", "AQUAMAN", "BATMAN", "IRON MAN",
          "TITANIC", "THE GODFATHER", "THE LORD OF THE RINGS", "WILLY WONKA", "THE MATRIX", "PYSCHO", 
          "GOOD BURGER", "INCEPTION", "FORREST GUMP", "GROUNDHOG DAY", "THE LION KING", "BAMBI", "ALADDIN",
          "TOP GUN", "SPIDER MAN", "HARRY POTTER", "TENET", "NAPOLEON DYNAMITE", "DUNE", "GRAN TURISMO",
          "FAST AND THE FURIOUS", "GUARDIANS OF THE GALAXY", "SAW", "AVATAR", "AUSTIN POWERS", "HALLOWEEN",
          "PACIFIC RIM", "STAR WARS", "YOUR NAME", "BULLET TRAIN", "THE NUN", "KUNG FU PANDA", "THE WOLF OF WALL STREET", 
          "GREEN BOOK", "CRAZY RICH ASIANS", "THE TRUMAN SHOW", "EVERYTHING EVERYWHERE ALL AT ONCE", "MOONFALL", 
          "THE BIG LEBOWSKI", "GET OUT", "GREASE", "MEGAMIND"]

GAMES = ["GOD OF WAR", "MINECRAFT", "TETRIS", "PORTAL", "HALO", "STREET FIGHTER", "WII SPORTS", "VALORANT",
         "FORTNITE", "AMONG US", "SUPER SMASH BROS", "TERRARIA", "COUNTER STRIKE", "RAINBOW SIX SIEGE", 
         "CALL OF DUTY", "ROBLOX", "FIRE EMBLEM", "PERSONA", "LETHAL COMPANY", "OSU", "GEOMETRY DASH", 
         "UNDERTALE", "CUPHEAD", "HALF LIFE", "HOLLOW KNIGHT", "MEGA MAN", "MARIO KART", "SONIC THE HEDGEHOG", 
         "LEAGUE OF LEGENDS", "CLASH OF CLANS", "CLASH ROYALE", "SPACE INVADERS", "TEKKEN", "KINGDOM HEARTS", 
         "DEAD SPACE", "DARK SOULS", "POKEMON", "GRAND THEFT AUTO", "ANGRY BIRDS", "CANDY CRUSH", "BORDERLANDS",
         "THE LAST OF US", "PONG", "BEAT SABER", "FINAL FANTASY", "XENOBLADE CHRONICLES", "ANIMAL CROSSING", 
         "MORTAL KOMBAT", "FRUIT NINJA", "SEA OF THIEVES", "STARDEW VALLEY", "FALLOUT", "POWERWASH SIMULATOR",
         "GANG BEASTS", "PAYDAY", "GOAT SIMULATOR", "HITMAN", "DEAD BY DAYLIGHT", "SKYRIM", "GEARS OF WAR",
         "OVERCOOKED", "HUMAN FALL FLAT", "DOOM", "SUBNAUTICA", "RAFT", "SCRAP MECHANIC", "PLAGUE INC", 
         "HELLO NEIGHBOR", "FORZA", "SLIME RANCHER", "GUILTY GEAR", "WOLFENSTEIN", "HADES", "YAKUZA", 
         "INJUSTICE", "METAL GEAR SOLID", "METAL GEAR RISING", "STARFIELD", "CELESTE", "QUAKE", "DEAD CELLS",
         "UNCHARTED", "THE SIMS", "SPLATOON", "RESIDENT EVIL"]
#TRIVIA QUESTIONS
#format is ("question", "answer 0", "answer 1", "answer 2", "answer 3", correct answer index)
MOVIE_QUESTIONS = [("When was Episode IV of Star Wars released", "1977", "1988", "1999", "2010", 0),
                   ("How many Harry Potter movies are there?", "6", "7", "8", "9", 2),
                   ("What was the first feature-length animated movie ever released?", "Snow White and the Seven Dwarfs", "Cinderella", "Treasure Island", "Beauty & The Beast", 0),
                   ("In \"The Matrix\", what colour is the pill Neo takes to escape the Matrix?", "Blue", "Red", "Orange", "Purple", 1),
                   ("Who voices Joy in Pixar's Inside Out?", "Tina Fey", "Kathryn Hahn", "Ellen DeGeneres", "Amy Poehler", 3),
                   ("Where were The Lord of the Rings movies filmed?", "Ireland", "Iceland", "New Zealand", "Australia", 2),
                   ("Which country does Forrest Gump travel to as part of the All-American Ping-Pong Team?", "Vietnam", "China", "Sweden", "France", 1),
                   ("Which famous Pulp Fiction scene was filmed backward?", "Vincent and Mia's dance scene", "Mia's overdose scene", "The \"royale with cheese\" scene", "The Ezekiel 25:17 scene", 1),
                   ("Which is not the name of a child selected to tour the Wonka factory in Willy Wonka and the Chocolate Factory?", "Billy Warp", "Veruca Salt", "Mike Teavee", "Charlie Bucket", 0),
                   ("Freddy Krueger wears a striped sweater that is which colors?", "Red and blue", "Orange and green", "Red and green", "Orange and brown", 2),
                   ("Who did the cat in the classic movie The Godfather belong to?", "Francis Ford Coppola", "Diane Keaton", "Al Pachino", "No one-the cat was a stray.", 3),
                   ("What is the name of the fictional land where Frozen takes place?", "Arendelle", "Naples", "Florin", "Grimm", 0),
                   ("What was the top-grossing movie of 2014?", "The Hunger Games: Mockingjay Part 1", "The Lego Movie", "Captain America: The Winter Soldier", "Guardians of the Galaxy", 3),
                   ("Who directed the hit 2017 movie Get Out?", "James Wan", "Jordan Peele", "Guillermo del Toro", "Tim Story", 1),
                   ("If you watch the Marvel movies in chronological order, which movie would you watch first?", "Iron Man", "Captain America: The First Avenger", "Doctor Strange", "Captain Marvel", 1),
                   ("Which two movies started from the same script?", "Star Wars and Close Encounters of the Third Kind", "E.T. and Poltergeist", "The Goonies and Indiana Jones", "Jurassic Park and The Land Before Time", 1),
                   ("In Mean Girls, Cady moves to Illinois from which continent?", "Australia", "Europe", "Africa", "Asia", 2),
                   ("Which movie was not directed by Tim Burton?", "The Witches", "Pee-Wee's Big Adventure", "Corpse Bride", "Big Fish", 0),
                   ("What object was Toy Story's Woody originally?", "Ventriloquist dummy", "Puppet", "Clown doll", "Nesting doll", 0),
                   ("Which Star Wars characters appear in Indiana Jones?", "R2-D2 and C-3PO", "Luke Skywalker and Princess Leia", "Yoda and Obi-Wan Kenobi", "Han Solo and Chewbacca", 0),
                   ("In The Ring, how long do people have to live after they watch a cursed videotape?", "Three days", "Seven days", "Five days", "One day", 1)]
GAME_QUESTIONS = [("What year was the original Super Mario Bros released?", "1980", "1985", "1990", "1995", 1),
                  ("What year was the first Five Nights at Freddy's game released?", "2011", "2012", "2013", "2014", 3),
                  ("Which of these is the best selling video game of all time?", "Minecraft", "Grand Theft Auto V", "Tetris", "Red Dead Redemption 2", 0),
                  ("What is the name of the language spoken in The Sims franchise?", "Gibberish", "English", "Simlish", "Spanish", 2),
                  ("In Mario Kart, the power-up that seeks out the player in first position and explodes on impact is a shell that is what color?", "Red", "Blue", "Green", "Purple", 1),
                  ("Pocket, Light, Color, and Advance were all styles or variants of what video game hardware system?", "Game Boy", "Gamecube", "Game Child", "Game Box", 0),
                  ("What game does the acronym \"LoL\" stand for?", "Laugh out Loud", "Legends of Lore", "League of Legends", "Leauge of Lords", 2),
                  ("What character of the game Valorant comes from Germany?", "Killjoy", "Phoenix", "Breach", "Omen", 0),
                  ("How long is a full day cycle in Minecraft?", "5 minutes", "10 minutes", "15 minutes", "20 minutes", 3),
                  ("What game engine was used to make Fortnite?", "Unity", "Unreal Engine", "GameMaker", "Godot", 1),
                  ("Who designed most of the characters and movesets for the Super Smash Bros franchise?", "Masahiro Sakurai", "Reggie Fils-Aimé", "Doug Bowser", "Satoru Iwata", 0),
                  ("Which Valve game features a main character named \"Chell\"?", "Half-Life", "Portal", "Team Fortress 2", "Left 4 Dead", 1),
                  ("Which of these is NOT a first person shooter?", "Destiny", "Apex Legends", "GoldenEye 007", "Splatoon", 3),
                  ("How many installments are there in the Legend of Zelda Series?", "15", "17", "23", "29", 3),
                  ("Which of these studios is Street Fighter developed by?", "Capcom", "Konami", "Bandai Namco", "Nintendo", 0),
                  ("Which of these games were released in 2016?", "Overwatch", "Hitman", "Dark Souls III", "All the above", 3),
                  ("What year was the Xbox 360 released?", "2003", "2005", "2007", "2009", 1),
                  ("What year was the Wii released?", "2004", "2006", "2008", "2010", 1),
                  ("What year was the PS4 released?", "2011", "2013", "2015", "2017", 1),
                  ("What is the name of the classic game where players clear a board of mines?", "Minesweeper", "Minebreaker", "Minedestroyer", "Mineclearer", 0),
                  ("Which video game series features a character named Master Chief?", "Fallout", "Doom", "Halo", "Borderlands", 2)]

# create an array storing which questions have been asked already
question_indexes = []
#ask trivia function
def trivia(game_option):
    #empty tuple to store question
    question = ()
    
    #prevention of the same questions one after another
    randomQuestionNum = 0

    #check if all questions have been asked, if so clear the list and make all questions askable again
    if game_option == "movies" and len(question_indexes) == len(MOVIE_QUESTIONS):
        question_indexes.clear()    
    elif game_option == "video games" and len(question_indexes) == len(GAME_QUESTIONS):
        question_indexes.clear()
    
    # pick a random question and check if it's not been chosen, if it hasn't ask and add it to the asked list
    if game_option == "movies":
        #loops until unasked question is pulled
        while True:
            #get random question
            randomQuestionNum = random.randint(0, len(MOVIE_QUESTIONS) - 1)
            #check if its not been asked yet, if so append to asked list and break
            if randomQuestionNum not in question_indexes:
                question_indexes.append(randomQuestionNum)
                break
        question = MOVIE_QUESTIONS[randomQuestionNum]
    elif game_option == "video games":
        #loops until unasked question is pulled
        while True:
            #get random question
            randomQuestionNum = random.randint(0, len(GAME_QUESTIONS) - 1)
            #check if its not been asked yet, if so append to asked list and break
            if randomQuestionNum not in question_indexes:
                question_indexes.append(randomQuestionNum)
                break
        question = GAME_QUESTIONS[randomQuestionNum]
    else:
        #just in case
        print("An unexpected error occured! We're sorry!")
    
    #tell user question and ask for answer
    while True:
        #print question and break
        print("-------------------------------")
        print(question[0])
        print("A: " + question[1])
        print("B: " + question[2])
        print("C: " + question[3])
        print("D: " + question[4])
        #ask user for answer
        answer = input("Enter choice: ").lower()
        #check if it's either a, b, c, or d
        if answer == "a" or answer == "b" or answer == "c" or answer == "d":
            #convert the string answer to an index
            converter = {
                "a": 0,
                "b": 1,
                "c": 2,
                "d": 3,
            }
            answer_num = converter.get(answer)
            #check if the answer is correct
            if answer_num == question[5]:
                #if it is, tell user and return true
                print("That is correct!")
                input("Press enter to continue ")
                return True
            else:
                #if it isnt tell user and return false
                print("That is incorrect!")
                input("Press enter to continue ")
                return False
        else:
            #failsafe if something weird happens
            print("That is not a valid input, please try again")

#stores what titles have been used already
title_indexes = []

#hangman game function
def game(game_option):
    #WHERE THE ACTUAL GAME BEGINS
    hangman_state = 0 #stores what state the hangman is in
    words_completed = 0 #how many titles player completes
    game_over = False #check if user is dead
    
    #clear both lists for holding asked questions and titles
    question_indexes.clear()
    title_indexes.clear()

    #loops until player loses
    while game_over == False:
        print("---------------------------------")
        
        #randomize what word the player will have to guess
        the_word = ""
        if game_option == "movies":
            #check if asked list is full, if it is clear the list and all titles are askable again
            if len(title_indexes) == len(MOVIES):
                title_indexes.clear()
            randomNum = 0
            while True:
                # pick a random index from the title list
                randomNum = random.randint(0, len(MOVIES) - 1)
                # if index hasn't been picked yet, add it to the asked list and break
                if randomNum not in title_indexes:
                    title_indexes.append(randomNum)
                    break
            the_word = MOVIES[randomNum]
        elif game_option == "video games":
            #check if asked list is full, if it is clear the list and all titles are askable again
            if len(title_indexes) == len(GAMES):
                title_indexes.clear()
            randomNum = 0
            while True:
                # pick a random index from the title list
                randomNum = random.randint(0, len(GAMES) - 1)
                # if index hasn't been picked yet, add it to the asked list and break
                if randomNum not in title_indexes:
                    title_indexes.append(randomNum)
                    break
            the_word = GAMES[randomNum]
        else:
            #safety net just in case game option isnt valid
            print("An unexpected error occured, we are sorry")
            break
        
        #initalize arrays for word letters, unique letters, and if they've been revealed
        word_letters = []
        word_unique_letters = []
        word_completed = []
        
        # loops for how long the word is
        for letter in the_word:
            word_letters.append(letter) #add letter to list
            #if theres a space make it show already
            if letter == " ":
                word_completed.append(True)
            else:
                #if its a normal letter append that it's not complete
                word_completed.append(False)
                #if its a unique letter append it to the unique letter list
                if letter not in word_unique_letters:
                    word_unique_letters.append(letter)
        
        #loops until user completes word or dies
        while True:
            #print current state of hangman
            print(HANGMANPICS[hangman_state])

            #print what letters are revealed
            for i in range(len(word_letters)):
                if word_completed[i] == True:
                    print(word_letters[i], end=" ")
                else:
                    print("_", end=" ")
            print("\n")

            fully_revealed = False
            #check if all letters are revealed
            for complete in word_completed:
                if complete == True:
                    fully_revealed = True
                else:
                    fully_revealed = False
                    break

            
            #check if player has run out of lives, has revealed all letters, or give options if none are true
            if(hangman_state > 5):
                #hangman is at 6, begin game over procedure
                print("GAME OVER!")
                print(f"You completed {words_completed} title(s)!")
                input("Press enter to continue ")
                game_over = True
                break
            elif fully_revealed == True:
                #player has fully revealed the title through trivia, move to next level
                print("You have fully revealed the title!")
                print(f"The title was {the_word}!")
                hangman_state = 0 #reset hang man
                words_completed += 1 #add 1 to completed words
                input("Press enter to continue ")
                break
            else:
                #ask user if they want to guess the title, trivia, or quit
                word_or_trivia = ""
                #loops until user gives a proper response
                while True:
                    print("Pick an option:")
                    print("A. Guess the title")
                    print("B. Answer trivia for a letter")
                    print("C. Quit")
                    word_or_trivia = input("Enter choice: ").lower() #ask user for choice
                    #if it's a valid choice break
                    if word_or_trivia == "a" or word_or_trivia == "b" or word_or_trivia == "c":
                        break
                    else:
                        #user didn't give valid choice, tell them it's invalid and loop again
                        print("\nInput not valid, please try again\n")
                if word_or_trivia == "a":
                    print("-------------------------------")
                    #the user wants to guess the word
                    guess = input("Enter your guess: ").upper()
                    print("")
                    #check if the guess is correct
                    if guess == the_word:
                        #guess is correct, tell user and move to next level
                        print("Your guess is correct!")
                        print(f"The title was {the_word}!")
                        hangman_state = 0
                        words_completed += 1
                        input("Press enter to continue ")
                        break
                    else:
                        #guess is wrong, tell user and add one to hangman state
                        print("Your guess is wrong.")
                        print("That was not the title.")
                        input("Press enter to continue ")
                        hangman_state += 1
                    print("---------------------------------")
                elif word_or_trivia == "b":
                    #run trivia game and check if they get it correct
                    if trivia(game_option) == True:
                        #reveal one letter
                        #pick one random letter to reveal
                        uncover_index = random.randint(0, len(word_unique_letters) - 1)
                        uncover_letter = word_unique_letters[uncover_index]
                        #reveal all cases of that letter
                        for i in range(len(word_letters)):
                            if word_letters[i] == uncover_letter:
                                word_completed[i] = True
                        #remove from unqiue letters
                        word_unique_letters.pop(uncover_index)
                    else:
                        #add to hangman state
                        hangman_state += 1
                    print("-------------------------------")
                elif word_or_trivia == "c":
                    #ask user if they want to quit, and if they want to, set the hangman to fully hung
                    confirm = input("Are you sure you want to quit (yes/no)? ").lower()
                    if(confirm == "yes"):
                        hangman_state = 6
                else:
                    #safety net just in case something weird happens
                    print("\nAn unexpected error has occured, we're sorry!\n")

def menu():
    #get users choice of topic, help, or quit
    while True:
        print("=================================")
        print(f"Welcome to {GAME_NAME}! Please pick a topic, get help, or quit.")
        print("A. Movies")
        print("B. Video Games")
        print("C. Help")
        print("D. Quit")
        #user chooses
        game_choice = input("Enter choice: ").lower()
        #check if user wants to begin game, get help, or quit
        if(game_choice == "a"):
            #begin game with movie topic
            game("movies")
        elif(game_choice == "b"):
            #begin game with video game topic
            game("video games")
        elif(game_choice == "c"):
            #tutorial
            print("---------------------------------")
            print("TUTORIAL")
            print("Each round you will get a title with it's letters hidden.")
            print("You can either guess the full title or reveal all the letters.")
            print("Every time you fully reveal/guess the title, the hangman will reset.")
            print("In order to reveal letters, you must answer a multiple choice trivia question.")
            print("If you answer the trivia question correctly, you will reveal all cases of one letter.")
            print("If you get the trivia question wrong or guess the wrong title, you will add one to your hangman.")
            print("If you mess up 6 times, the game is over.")
            input("Press enter to continue ")
        elif(game_choice == "d"):
            #quit the game
            print("Thanks for playing!")
            break
        else:
            #user inputs invalid choice, tell them and loop again
            print("Invalid choice, please pick again.")
menu() #run the menu
