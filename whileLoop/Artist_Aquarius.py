from math import gcd

a = int(input())
b = int(input())

volume_vessel_1 = 0
volume_vessel_2 = 0

N = int(input())
done = False

while volume_vessel_1 != N or volume_vessel_2 != N:
    if N > a and N > b:
        print("Impossible")
        break
    if N % gcd(a, b) != 0:
        print("Impossible")
        break

    if max(a, b) == a:
        volume_vessel_1 += a
        print(">A")
        if volume_vessel_1 == N:
            break
        while volume_vessel_1 >= b:
            tmp = b - volume_vessel_2
            volume_vessel_2 += tmp
            volume_vessel_1 -= tmp
            print("A>B")
            if volume_vessel_1 == N or volume_vessel_2 == N:
                done = True
                break

            volume_vessel_2 = 0
            print("B>")

        if not done:
            volume_vessel_2 += volume_vessel_1
            volume_vessel_1 = 0
            print("A>B")

        else:
            break
    else:
        volume_vessel_2 += b
        print(">B")
        if volume_vessel_2 == N:
            break
        while volume_vessel_2 >= a:
            tmp = a - volume_vessel_1
            volume_vessel_1 += tmp
            volume_vessel_2 -= tmp
            print("B>A")
            if volume_vessel_1 == N or volume_vessel_2 == N:
                done = True
                break

            volume_vessel_1 = 0
            print("A>")

        if not done:
            volume_vessel_1 += volume_vessel_2
            volume_vessel_2 = 0
            print("B>A")

        else:
            break

