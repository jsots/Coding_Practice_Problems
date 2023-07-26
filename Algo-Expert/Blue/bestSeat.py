
def bestSeat(seats):
    # Write your code here.
    best_seat = -1
    best_distance = 0
    l = 0
    while l < len(seats):
        r = l + 1
        while r < len(seats) and seats[r] == 0:
            r += 1
        
        available_space = r - l - 1
        if available_space > best_distance:
            best_seat = (r + l) // 2
            best_distance = available_space
        l = r
    return best_seat
