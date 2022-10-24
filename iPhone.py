##################################IPHONE SUBROUTINE#############################

import random
import time
import sys
def ending():
        print("Thank you for using Rahman Troubleshoots Ltd. \nI hope we were able to be of help.\n\n")
        time.sleep(1.5)
        print("\n...\n\n")
        input("Please press ENTER to end")
        sys.exit()
        
solution = open('iPhone_solutions.txt', 'r+')
solutions = solution.readlines()


print('Welcome to Rahman Troubleshooting Services Ltd., for iPhone.')
print('You will now be asked to state what the problem with your device is.')

customer = input('What is the issue with your mobile device?: ').lower()

applications = ('apps', 'application', 'apps freezing', 'freezing', 'freeze', 'frozen')
if any(i in customer for i in applications):
    print(solutions[0])    

update = ('software', 'version', 'ios', 'updates', "can't update", 'not able to update', 'updating')
if any(i in customer for i in update):
    print(solutions[1])    
    
display = ('display', 'display is slow', 'running slow', 'slow', 'unresponsive', 'phone screen is slow', 'phone is slow')
if any(i in customer for i in display):
    print(solutions[2])

charge = ('charger', "charger won't work", 'not charging', 'charge', 'port damaged')
if any(i in customer for i in charge):
    print(solutions[3])

camera = ('my camera is blurry', 'camera', 'noise', 'scratches', ' scratched', 'fuzzy', 'blurry')
if any(i in customer for i in camera):
    print(solutions[4])

mic = ('microphone', "im not heard", "can't hear", "incomprehensible", 'speak', 'voice' 'can hear' 'calls')
if any(i in customer for i in mic):
    print(solutions[5])
    
coverage = ('networks', 'signal', 'wifi', 'internet', "can't connect")
if any(i in customer for i in coverage):
    print(solutions[6])

else:
        time.sleep(2.0)
        print("Unfortunately, we are unable to assist you at this moment as your device's data is not within our online database, could you please kindly answer a few questions and we will get back to you as soon as possible.")
        time.sleep(3.5)
        first_name = input('Hi user, What is your first name?:   ').title()
 
        surname = input("What is your surname?:   ").title()
        no = random.randint(1000,999999)
        Case_ID = (first_name + str(no))

        solutions= open(Case_ID+ ".txt","w+")
        solutions.write("Customers Full Name:   " +first_name+ " " +surname+ "\n")
        
        device_make = input("What is the make of your mobile device?: ")
        solutions.write("Customers Mobile Device Make:   "+device_make+"\n")

        model = input("What is the model of the mobile device? \n")
        solutions.write("Mobile Device Model:   "+model+ "\n")

        storage = input("How much internal storage space does your mobile device have? \nFor example, 16GB or 32GB or 64GB. \n").upper()
        solutions.write("Internal Storage Space:   "+storage+"\n")

        mods = input("Have you modified or tampered your mobile device in any way?\nIf so, please state the modifications or damages caused to your mobile device. \nFor example, LCD and speaker has been replaced or none. \n")
        solutions.write("Modifications Or Damage To The Mobile Device:   "+mods+"\n")


        issue = input('What is the issue that you are experiencing with the mobile device?: \n')
        solutions.write('Customers Issue:   '+issue+"\n")
        
        solutions.close()
        time.sleep(1.5)
        print("We shall assign you with a caseID, so that we can have your issue analysed and fixed by a technician. You will be contacted by our support services within the next 72 hours.\n")
        time.sleep(4.5)
        print("We will use your CaseID to contact you regarding the specific issue you are currently facing.\nYour CaseID is displayed below.")
        time.sleep(1.5)
        print(Case_ID)
        time.sleep(2)
        print("\n...\n")
        ending()
