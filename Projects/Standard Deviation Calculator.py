while True:
    numbers = []
    no = int(input("enter the desired number of elements: "))
    for i in range(no):
        element = float(input("enter element number " + str(i+1)+": "))
        numbers.append(element)
    summation = 0
    for i in numbers:
        summation += i
    mean = summation / no
    print("mean equals :" + str(mean))
    sum_number_minus_mean_squared = 0
    for i in numbers:
        sum_number_minus_mean_squared += pow(i - mean, 2)
    variance = sum_number_minus_mean_squared / (no - 1)
    standard_deviation = pow(variance, 0.5)
    print("standard deviation equals :" + str(standard_deviation))
    leave = input(
        "to continue press 1\npressing anything else will terminate:")
    if leave != "1":
        break
