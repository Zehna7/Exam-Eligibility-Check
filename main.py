medical_cause=input("did you have a medical cause Y or N: ")
atten = int(input("Enter the attendance of the student: "))
if medical_cause == "Y":
    print("You are allowed")
    if atten>=75: 
     print("You are allowed")
    else:
     print("Not allowed")
else:
    print("No Medical cause not allowed")
