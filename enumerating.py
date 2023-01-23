values = [10, 9, 8]

# so enumerate gives back the count and the value
"""
0 10
1 9
2 8
"""
for count, value in enumerate(values):
    print(count, value)

# the start parameters allows the change the starting counter
for count, value in enumerate(values, start=5):
    print(count, value)

# use enumerate to fill in a dictionary
weekdays = {
    s: i+1 for i, s in enumerate(['Mon', 'Tue', 'Wed', 'Thu', 'Fr', 'Sat', 'Sun'])    
}

print(weekdays)