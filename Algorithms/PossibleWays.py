def number_of_ways(score):
    if score == 0:
        return 1 
    ways = 0
    for i in possible_steps:
        if i <= score:
            ways += number_of_ways(score - i)
    return ways

possible_steps = sorted([3,5,10])
print number_of_ways(int(raw_input()))
            
            