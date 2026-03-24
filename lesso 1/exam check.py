#take input for the studentthat he can attend the exam or not
medical_cause = input("Did you have a medical cause? (Y/N)").strip().upper()

if medical_cause=="Y":
    print("you are allowed")
else:
    atten= int(input("enterthe attendance of the student"))

    if atten >= 75 :
        print ("allowed")
    else:
        print (" not allowed")