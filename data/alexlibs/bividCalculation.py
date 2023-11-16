import re

Answer = ""
print("Answer Down:")
print(Answer)

def globalVar(variableToMakeGlobal):
    global Answer
    Answer = variableToMakeGlobal

with open("store2.bd", "w") as storeBD:
    storeBD.write(Answer)

def addAndSubtract(val, usr_inp):
    value = val
    user_input = usr_inp

    print("Analyzing + & -")
    if "+" in value:
        # Addition
        problem = user_input
        problem_LH = re.split("[+]", problem)
        number_of_values = len(problem_LH)
        if number_of_values == 2:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 + num2)

            globalVar(Answer)


        elif number_of_values == 3:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            num3 = int(problem_LH[2])
            Answer = str(num1 + num2 + num3)

            globalVar(Answer)
        elif number_of_values == 4:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            num3 = int(problem_LH[2])
            num4 = int(problem_LH[3])
            Answer = str(num1 + num2 + num3 + num4)

            globalVar(Answer)
        elif number_of_values == 5:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            num3 = int(problem_LH[2])
            num4 = int(problem_LH[3])
            num5 = int(problem_LH[4])
            Answer = str(num1 + num2 + num3 + num4 + num5)

            globalVar(Answer)
        elif number_of_values == 6:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            Answer = str(num1 + num2)

            globalVar(Answer)
        elif number_of_values == 7:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            Answer = str(num1 + num2)

            globalVar(Answer)
        elif number_of_values == 8:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            Answer = str(num1 + num2)

            globalVar(Answer)
        elif number_of_values == 9:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            Answer = str(num1 + num2)

            globalVar(Answer)
        elif number_of_values == 10:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            num2 = int(problem_LH[1])
            Answer = str(num1 + num2)

            globalVar(Answer)
        elif number_of_values == 11:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 + num2)

            globalVar(Answer)
        elif number_of_values == 12:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 + num2)

            globalVar(Answer)
        elif number_of_values == 13:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 + num2)

            globalVar(Answer)
        elif number_of_values == 14:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 + num2)

            globalVar(Answer)
        elif number_of_values == 15:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 + num2)

            globalVar(Answer)
        elif number_of_values == 16:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 + num2)

            globalVar(Answer)
        elif number_of_values == 17:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 + num2)

            globalVar(Answer)
        elif number_of_values == 18:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 + num2)

            globalVar(Answer)
        # print(Answer)

    elif "-" in value:
        # Subtraction
        problem = user_input
        problem_LH = re.split("[-]", problem)
        number_of_values = len(problem_LH)
        if number_of_values == 2:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 - num2)

            globalVar(Answer)
        elif number_of_values == 3:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 - num2)

            globalVar(Answer)
        elif number_of_values == 4:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 - num2)

            globalVar(Answer)
        elif number_of_values == 5:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 - num2)

            globalVar(Answer)
        elif number_of_values == 6:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 - num2)

            globalVar(Answer)
        elif number_of_values == 7:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 - num2)

            globalVar(Answer)
        elif number_of_values == 8:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 - num2)

            globalVar(Answer)
        elif number_of_values == 9:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 - num2)

            globalVar(Answer)
        elif number_of_values == 10:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 - num2)

            globalVar(Answer)
        elif number_of_values == 11:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 - num2)

            globalVar(Answer)
        elif number_of_values == 12:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 - num2)

            globalVar(Answer)
        elif number_of_values == 13:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 - num2)

            globalVar(Answer)
        elif number_of_values == 14:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 - num2)

            globalVar(Answer)
        elif number_of_values == 15:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 - num2)

            globalVar(Answer)
        elif number_of_values == 16:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 - num2)

            globalVar(Answer)
        elif number_of_values == 17:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 - num2)

            globalVar(Answer)
        elif number_of_values == 18:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 - num2)

            globalVar(Answer)
        
        # print(Answer)

def divideAndMultiply(val, usr_inp):
    value = val
    user_input = usr_inp

    print("Analyzing * & /")
    if "*" in value:
        # Multiplication
        problem = user_input
        problem_LH = re.split("[*]", problem)
        number_of_values = len(problem_LH)
        if number_of_values == 2:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 * num2)

            globalVar(Answer)
        elif number_of_values == 3:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 * num2)

            globalVar(Answer)
        elif number_of_values == 4:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 * num2)

            globalVar(Answer)
        elif number_of_values == 5:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 * num2)

            globalVar(Answer)
        elif number_of_values == 6:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 * num2)

            globalVar(Answer)
        elif number_of_values == 7:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 * num2)

            globalVar(Answer)
        elif number_of_values == 8:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 * num2)

            globalVar(Answer)
        elif number_of_values == 9:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 * num2)

            globalVar(Answer)
        elif number_of_values == 10:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 * num2)

            globalVar(Answer)
        elif number_of_values == 11:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 * num2)

            globalVar(Answer)
        elif number_of_values == 12:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 * num2)

            globalVar(Answer)
        elif number_of_values == 13:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 * num2)

            globalVar(Answer)
        elif number_of_values == 14:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 * num2)

            globalVar(Answer)
        elif number_of_values == 15:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 * num2)

            globalVar(Answer)
        elif number_of_values == 16:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 * num2)

            globalVar(Answer)
        elif number_of_values == 17:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 * num2)

            globalVar(Answer)
        elif number_of_values == 18:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 * num2)

            globalVar(Answer)

    elif "/" in value:
        # Division
        problem = user_input
        problem_LH = re.split("[/]", problem)
        number_of_values = len(problem_LH)
        if number_of_values == 2:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 / num2)

            globalVar(Answer)
        elif number_of_values == 3:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 / num2)

            globalVar(Answer)
        elif number_of_values == 4:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 / num2)

            globalVar(Answer)
        elif number_of_values == 5:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 / num2)

            globalVar(Answer)
        elif number_of_values == 6:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 / num2)

            globalVar(Answer)
        elif number_of_values == 7:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 / num2)

            globalVar(Answer)
        elif number_of_values == 8:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 / num2)

            globalVar(Answer)
        elif number_of_values == 9:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 / num2)

            globalVar(Answer)
        elif number_of_values == 10:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 / num2)

            globalVar(Answer)
        elif number_of_values == 11:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 / num2)

            globalVar(Answer)
        elif number_of_values == 12:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 / num2)

            globalVar(Answer)
        elif number_of_values == 13:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 / num2)

            globalVar(Answer)
        elif number_of_values == 14:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 / num2)

            globalVar(Answer)
        elif number_of_values == 15:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 / num2)

            globalVar(Answer)
        elif number_of_values == 16:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 / num2)

            globalVar(Answer)
        elif number_of_values == 17:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 / num2)

            globalVar(Answer)
        elif number_of_values == 18:
            num1 = int(problem_LH[0])
            num2 = int(problem_LH[1])
            Answer = str(num1 / num2)

            globalVar(Answer)
