class tamil:
    
    def subject():
        sub1=int(input("Enter the Marks:"))
        sub2=int(input("Enter the Marks:"))
        sub3=int(input("Enter the Marks:"))
        sub4=int(input("Enter the Marks:"))
        if(sub1<35):
            print("Need to improve")
            message="Need to improve"
        elif(sub1<50):
            print("Good")
            message="Good"
        elif(sub1<80):
            print("Very Good")
            message="Very Good"
        else:
            print("Excellent")
            message="Excellent"
        if(sub2<35):
            print("Need to improve")
            message="Need to improve"
        elif(sub2<50):
            print("Good")
            message="Good"
        elif(sub2<80):
            print("Very Good")
            message="Very Good"
        else:
            print("Excellent")
            message="Excellent"
        if(sub3<35):
            print("Need to improve")
            message="Need to improve"
        elif(sub3<50):
            print("Good")
            message="Good"
        elif(sub3<80):
            print("Very Good")
            message="Very Good"
        else:
            print("Excellent")
            message="Excellent"
        if(sub4<35):
            print("Need to improve")
            message="Need to improve"
        elif(sub4<50):
            print("Good")
            message="Good"
        elif(sub4<80):
            print("Very Good")
            message="Very Good"
        else:
            print("Excellent")
            message="Excellent"
        return message
    ran=int(input("Enter a number:"))
    def number():
        if(ran%2==0):
            print(ran,"is Even number")
            result=(ran,"is Even number")
        else:
            print(ran,"is Odd number")
            result=(ran,"is Odd number")
        return result