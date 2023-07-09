def darkRoom(n, intensities):
    neg_numbers = 0
    pos_numbers = 0
    for num in intensities:
        if num > 0:
            pos_numbers += 1
        if num < 0:
            neg_numbers += 1
    return 2**(neg_numbers-1)*2**(pos_numbers)


print(darkRoom(3, [-1, -2, -3, 2, 3]))