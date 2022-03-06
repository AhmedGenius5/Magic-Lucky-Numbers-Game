print("\nHELLO THERE! This a Magic Lucky Numbers Game\n")

while True: 
    try:
        lucky_list = str(input("\nPlease insert your magic lucky numbers or words!\n")).split()
        unique_lucky_list = set(lucky_list)
        if len(unique_lucky_list) < 2:
            print("Lucky list must be more than 1 input!")
            continue     
    except Exception as e:
        print("Your input cause {}".format(e))
        print("Please check your input and try again!\n")
    else:
        if unique_lucky_list is not None:
            print("\nVery nice! Your lucky list has been created successfully!\n")
        while True:
            try:
                mode = int(input("\n1- Individual player\n2- Multi players\nPlease choose your mode (1, 2) "))
                if mode == 1:
                    print("Here is your LUCK! '{}'".format(unique_lucky_list.pop()))    
                    break  
                elif mode == 2:
                    while True:
                        try:
                            participants = int(input("\nPlease enter the number of participants: "))
                            while participants < 2 or participants > len(unique_lucky_list):
                                participants = int(input("Please enter the number of participants in range from 2 up to {}: ".format(len(unique_lucky_list))))
                            participants_names = []
                            while len(participants_names) < participants:
                                participant = str(input("Please insert participant number {}: ".format(len(participants_names)+1)))
                                if participant.isalpha():
                                    participants_names.append(participant.title())
                                else:
                                    print("Only alphabet characters are allowed!\n")
                        except Exception as e: 
                            print("Your input cause {}".format(e))
                            print("Please check your input and try again!\n")
                        else: 
                            unique_participants_names = set(participants_names)         
                            for name in unique_participants_names:
                                print("\n{}, Here is your LUCK! '{}'".format(name,unique_lucky_list.pop()))
                            break
                    break
                else:
                    print("\nYour selected mode is not recognized!\nPlease try again with only (1, 2)\n")
            except Exception as e: 
                        print("Your input cause {}".format(e))
                        print("Please check your input and try again!\n")
    finally:
        another_try = input("\nWould you like to try again :) (y, n) ")
        if another_try != 'y':
            if another_try != 'n':
                print("Didn't Got It!")
            print("Hope to see you again ^_^, Good Bye!\n")
            break
 
