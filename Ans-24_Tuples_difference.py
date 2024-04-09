def main():
    user1 = input("Enter the string sepreted by (Space ) : ")
    u1 = set(user1.split())
    user2 = input("Enter the string sepreted by (Space) : ")
    u2 = set(user2.split())

    Mytuple = u1 - u2

    print("Element present in first set but not in second ")

    for e in Mytuple:
        print(e, end=" ")


main()
