def majorityElement(array):
    # Write your code here.
    majority_metric = len(array) / 2
    majority = array[0]
    counter = 0

    for i in range(1, len(array)):
        if array[i] == majority:
            counter += 1
        else:
            if counter == 0:
                majority = array[i]
            else:
                counter -= 1
    
    return majority
