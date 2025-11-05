

def calculate_bmi(height, weight):
    
    calculatedbmi = weight / (height*height)

    print("BMI = " + str(calculatedbmi))

    if calculatedbmi < 18.5 :
        print ("Underweight")
        return (-1)
    elif 18.5 <= calculatedbmi <= 25.0 :
        print ("Normal")
        return (0)
    else :
        print ("Overweight")
        return (1)




print (calculate_bmi(weight=57, height=1.73))