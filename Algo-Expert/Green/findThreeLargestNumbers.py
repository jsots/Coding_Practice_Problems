def findThreeLargestNumbers(array):
    # Write your code here.
    # ans = [float("-inf)"] * 3
    sm = float("-inf")
    med = float("-inf")
    lg = float("-inf")
    
    for num in array:
        if num > lg:
            sm = med
            med = lg
            lg = num
        elif num > med:
            sm = med
            med = num
        elif num > sm:
            sm = num
            
        
    return [sm, med, lg]