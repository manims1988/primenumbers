x = int(input('enter a no:'))
if x > 1:
        if x == 2 or x == 3:
                print(f'{x} prime number')
        else:
                y = x % 2
                z = x % 3
                if y == 1 or z == 1:
                        print(f'{x} prime number')
                else:
                        print(f'{x} not prime number')
