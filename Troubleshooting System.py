import sys #import library functions for system, random and time
import random
import time
def ending(): #this is a suroutine to end the program
        print("Thank you for using Rahman Troubleshoots Ltd. \nI hope we were able to be of help.\n\n")
        time.sleep(1.5)
        print("\n...\n\n")
        input("Please press ENTER to end")
        sys.exit()

time.sleep(0.25) #
print("Welcome to Rahman Troubleshoots Ltd.") #Greets the user to the program
time.sleep(0.75)
print("We aim to have your issue diagnosed and repaired within 2-3 working days. Please bear with us if you have already been assigned a CaseID")
time.sleep(3.0)

device_make = input ("What is the make of your device? \nFor example, Apple or Samsung or LG or Huawei.\n").lower()
time.sleep(1.5)
print("Transferring you over to our automated troubleshooting service...")
time.sleep(2.5)
print("\n               .....           \n")

if device_make == "iphone" or device_make == "apple" or device_make == "apple iphone":
        import iPhone
elif device_make == "samsung":
        import Samsung
elif device_make == "sony" or device_make == "xperia" or device_make == "sony xperia":
        import Sony
else:
        time.sleep(2.0)
        print("Unfortunately, we are unable to assist you at this moment as your device's data is not within our online database, could you please kindly answer a few questions and we will get back to you as soon as possible.")
        time.sleep(3.5)
        first_name = input('Hi user, What is your first name?:   ').title()
 
        surname = input("What is your surname?:   ").title()
        no = random.randint(1000,999999)
        Case_ID = (first_name + str(no))

        solutions= open(Case_ID+ ".txt","w+") #looks in folder, as no text file with name exists a new one is created
        solutions.write("Customers Full Name:   " +first_name+ " " +surname+ "\n")
        solutions.write("Customers Mobile Device:   "+device_make+"\n")

        model = input("What is the model of the mobile device? \n")
        solutions.write("Mobile Device Model:   "+model+ "\n")

        storage = input("How much internal storage space does your mobile device have? \nFor example, 128GB or 256GB or 512GB. \n").upper()
        solutions.write("Internal Storage Space:   "+storage+"\n")

        mods = input("Have you modified or tampered your mobile device in any way?\nIf so, please state the modifications or damages caused to your mobile device. \nFor example, LCD and speaker has been replaced or none. \n")
        solutions.write("Modifications Or Damage To The Mobile Device:   "+mods+"\n")

        issue = input('What is the issue that you are experiencing with the mobile device?: \n')
        solutions.write('Customers Issue:   '+issue+"\n")
        
        solutions.close()
        time.sleep(1.5)
        print("We shall assign you with a caseID, so that we can have your device assessed and fixed by a technician. You will be contacted by our support services within the next working day to book your device in for a repair.\n")
        time.sleep(4.5)
        print("We will use your CaseID to contact you regarding the specific issue you are currently facing.\n Please do not give anyone your details without confirming your CaseID and details. \n Your CaseID is displayed below.")
        time.sleep(1.5)
        print(Case_ID)
        time.sleep(2)
        print("\n...\n")
        ending()
