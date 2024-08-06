"""

*     *
**   **
* * * *
*  *  *
* * * *
**   **
*     *

"""

# limit = int(input('enter a limit : '))
limit = 7

for i in range(1, limit + 1):
    for j in range(1, limit + 1):
        if j == 1:
            print("*", end="")

        if i % 2 == 0:
            if j == i + 1 or j == limit - i:
                print("*", end=" ")
            else:
                print(" ", end="")

    print()
