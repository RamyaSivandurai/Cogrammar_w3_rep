
                            ######## Pseudocode #######

'''
We are going to determine the award a person will receive competing in a triathlon
get the input time for swimming in minutes
get the input time for cycing in minutes
get the input time for running in minutes
calculate the total time taken by adding the above three events to complete the triathlon
print the total time
if total time is <= 100 then the person receives "Provincial Colours" award
if total time is > 100 and <=105 then the person receives "Provincial Half Colours" award
if total time is > 105 and <=110 then the person receives "Provincial Scroll" award
if total time is > 110 then the person receives "No award"
use \n(Escape sequence) for giving empty lines in between the outputs.
'''
                            ##########  Code #########

print("======================= Triathlon Awards =========================\n" )

swim_time = int(input("Enter your swimming event time in minutes: "))
cycling_time = int(input("Enter your cycling event time in minutes: "))
run_time = int(input("Enter your running event time in minutes: "))

total_time = swim_time + cycling_time + run_time 

print("")

print(f"Total time you took to complete the triathlon: {total_time} minutes \n")  

if total_time <= 100:
    print("Congrats,You're awarded with ''Provincial Colours'' award \n")  # within the qualifying time
elif total_time > 100 and total_time <= 105:
    print("Congrats,You're awarded with ''Provincial Half Colours'' award \n")  # within 5 mins of the qualifying time
elif total_time > 105 and total_time <= 110:
    print("Congrats,You're awarded with ''Provincial Scroll'' award \n")    # within 10 mins of the qualifying time
else:
    print("Sorry No award \n")   # more than 10 mins off from the qualifying time

print("==================================================================")