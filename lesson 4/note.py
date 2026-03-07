amount=int(input("please enter the amount for withdraw"))
note1 =amount//100
note2 =(amount%100)//50
note3 =((amount%100)%50)//10
print("notes of a hundred",note1)
print("notes of fifty",note2)
print("notes of ten",note3)