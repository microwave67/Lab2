

def calculate_bmi(height, weight):
    
    calculatedbmi = weight / (height*height)

    print("BMI = " + str(calculatedbmi))

    if calculatedbmi < 18.5 :
        print ("Underweight")
    elif 18.5 <= calculatedbmi <= 25.0 :
        print ("Normal")
    else :
        print ("Overweight")




calculate_bmi(weight=57, height=1.73)