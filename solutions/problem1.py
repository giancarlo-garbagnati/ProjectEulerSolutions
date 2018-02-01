mult_of_three_or_five = [x for x in range(1,1000) if (x%3==0) or (x%5==0)]

print(sum(mult_of_three_or_five))