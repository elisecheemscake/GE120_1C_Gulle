print("---------- AUTO-LEVEL ----------")
print("A handy program that does all the levelling calculations for you!")
print("Created by Jo Elise G. Gulle")

#to be used in computing allowable error
from math import sqrt 

#initializing variables to be used
levelling_table = []
total_distance = 0
tp_counter = 1

def floatInput(prompt):
    '''
    Checks if the input is a float variable. Converts the variable into float if not.
    Input: prompt
    Return: prompt, converted to float
    '''

    if type(prompt) != float:
        prompt = float(prompt)
    
    return prompt

#asks for initial elevation
print("\n")
true_elev = floatInput(input("Initial elevation of BM0: "))
obs_elev = float(0)

while True:
    print()
    print("TP", tp_counter)

    #necessary levelling calculations here
    backsight = floatInput(input("Backsight (m): "))
    foresight = floatInput(input("Foresight (m): "))
    dist_bet_tp = floatInput(input("Distance between this TP and previous TP (m): "))
    ins_height = obs_elev + backsight
    obs_elev = ins_height - foresight
    
    print("Instrument Height: ", ins_height)
    print("Elevation: ", obs_elev)
    total_distance = total_distance + dist_bet_tp

    #tuple including all needed values
    tp_data = (tp_counter, backsight, ins_height, foresight, obs_elev)
    levelling_table.append(tp_data)

    #loop if yes, stop if no
    yesno = input("Add new line? (Y/N): ")
    if yesno.lower() == "Yes" or yesno.lower() == "y":
        tp_counter = tp_counter + 1
        continue
    elif yesno.lower() == "No" or yesno.lower() == "n":
        break

#formatting the table
print("\n\n")
print("----- LEVELLING TABLE -----")
print('{: ^10} {: ^10} {: ^10} {: ^10} {: ^10}'.format("Sta.","B.S","H.I","F.S","Elev."))

for tp_data in levelling_table:
    print('{: ^10} {: ^10} {: ^10} {: ^10} {: ^10}'.format(tp_data[0], tp_data[1], tp_data[2], tp_data[3], tp_data[4]))

#error and accuracy calculations
error = true_elev - obs_elev
firstorder_error_allowable = (4.80*1000) * sqrt(total_distance/1000)
secondorder_error_allowable = (8.40*1000) * sqrt(total_distance/1000)
thirdorder_error_allowable = (12.0*1000) * sqrt(total_distance/1000)

print("\n\n")
print("ACCURACY:")

if error < thirdorder_error_allowable:
    print("THIRD ORDER")
elif error < secondorder_error_allowable and error > thirdorder_error_allowable:
    print("SECOND ORDER")
elif error < firstorder_error_allowable and error > secondorder_error_allowable:
    print("FIRST ORDER")
elif error > thirdorder_error_allowable:
    print("ERROR TOO LARGE")

print()
print("---------- END ----------")