print("question: which organ is important")
print("A: Brain")
print("B: Heart")
print("C: Lungs")
print("D: NONE OF THE ABOVE")
a=input("enter answer here")
if a=="B":
    print("Correct")
    print("question: what goes up but doesn't come down")
    print("A: age")
    print("B: gravity")
    print("C: baloon")
    print("D: NONE OF THE ABOVE")
    b=input("enter answer here")
    if b=="A":
        print("Correct")
        print("question: what has a head and a tail but no body")
        print("A: remote")
        print("B: clock")
        print("C: coin")
        print("D: NONE OF THE ABOVE")
        c=input("enter answer here")
        if c=="C":
            print("YOU PAST THE QUIZES!")
        else:
            print("TRY AGAIN!")
    else:
        print("TRY AGAIN!")
else:
    print("TRY AGAIN!")    