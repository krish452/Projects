## Calculate average temperature of a set of days 
##return the number of days the temperature was above average

##Algorithm
#1. Enter number of days whose temperature needs to be recorded
#2. Enter temperature for each day
#3. Calculate average of temperature 
#4. Return average temperature
#5. Check how many days exceeded average temp
#6. Return number of days that exceeded avg temp

#Time Complexity and Space Complexity: O(n) - based on the number of elements in the list.

def enter_data(num):
    array1 = []
    for i in range(0,num):
        array1.append(float(input("Enter highest temperature of Day " + str(i+1) + ": \n")))
    return array1

def avg_temp(array1):
    count = 0
    avg = sum(array1)/len(array1)
    for i in array1:
        if i > avg: count += 1
    return avg, count

def main():
    num_days = int(input("Enter number of days whose temperature needs to be recorded: \n"))
    array_temp = enter_data(num_days)
    average,count = avg_temp(array_temp)
    print(f"The average temperature is:{average}")
    print(f"The number of days temperature exceeded average is: {count}")

main()