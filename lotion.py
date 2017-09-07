#! /usr/bin/python3

'''This is a tribute to the pit scene from Silence of the Lambs.  This script will ask you to rub the
lotion on your skin or else you get the hose again.  You will be prompted with an ok/no option.  
If no, the statement will be looped until you do enter ok.  From there, you will be asked
to put the lotion into the basket. If No, the statement will be looped until greater than four then 
Buffalo Bill will freak out.  If ok, the statement ends.  Whatever the user input is, it is converted
via .lower to convert it to lowercase.  
'''

#Statements.  Can be added or modded without having to dive into the code.
lotionOn = "\nBuffalo Bill - It rubs the lotion on It's skin, or else It gets the hose again...\n"
basketIn = "\nBuffalo Bill - Now It puts the lotion into the basket.\n"
basketAngry = "\nBuffalo Bill - Put the FUCKIN' lotion into thuh buuuaaasskuutt!\n" 
basketGood = "\nBuffalo Bill - Guuuuddd... guuuuddd... \n"
billMoan = "\n Uuuuwahhhhhhaaaaahhhh!!!!\n"
precious = "\nPrecious - Arf! Arf!\n"
preciousHose = "\nBuffalo Bill - The hose, Precious, It will get the hose... \n"
lectorReminder = '\nHannibal Lector - Quid pro quo... enter "OK" or "no" \n'

#Lotion block.  Enter OK to break loop, otherwise loop will go 3 times until Precious barks.  If
#you are reminded by Lector of the syntax, Precious barks.
lotionCount = 0 #the starting point for the loop
while True:
    print(lotionOn)
    lotionCount = lotionCount + 1 #will increase the number of times to loop by 1
    if lotionCount == 3: #every 3rd iteration of the loop.  Every 3 times
        print(precious)
        print(preciousHose)
        lotionCount = 0
    answerLotion = input()
    if answerLotion.lower() == 'ok': #the .lower converts the user input into lowercase
        break
    elif answerLotion.lower() == 'no': #the .lower converts the user input into lowercase
        continue
    else:
        print(lectorReminder)

#Basket part.  Bill asks you to put the lotion into the basket.  This will loop 3 times and then 
# he freaks out.  But if you break the loop with an OK, he praises you (sort of).  As ususal
# Lector will be there to remind you of the syntax. 
  
basketCount = 0
while basketCount < 3:
    basketCount = basketCount + 1 
    print(basketIn)
    answerBasket = input()
    if answerBasket.lower() == 'ok':
        print(basketGood)
        break
    
    elif basketCount == 3:
        print(basketAngry)
        basketCount = 0
        answerBasket = input()
        if answerBasket.lower() == 'ok':
            print(billMoan)
            break
        continue

    elif answerBasket.lower() == 'no':
        continue

    else:
        print(lectorReminder)