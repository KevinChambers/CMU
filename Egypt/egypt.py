# Pythagorean theorem - Right Angle Triangle Check. 

while True:
    line = input()
    
    # split and validate number of elements
    parts = line.split()
    if len(parts) != 3:
        print("⚠️ Bad input: must provide exactly 3 numbers. Skipping...")
        continue

    try:
        a, b, c = map(int, parts)
    except ValueError:
        print("⚠️ Bad input: must be integers. Skipping...")
        continue

    # check for negative or zero sides
    if a < 0 or b < 0 or c < 0:
        print("⚠️ Bad input: all numbers must be non-negative. Skipping...")
        continue

    # sentinel check (last in flow)
    if a == 0 and b == 0 and c == 0:
        break

    # safe computation
    result = c**2 == a**2 + b**2
    print(result)
