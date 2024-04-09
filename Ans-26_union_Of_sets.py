def main():

    set1 = input("Enter the characters with saprated spaces  : ")
    s1 = set(set1.split())
    set2 = input("Enter the characters with saprated spaces  : ")
    s2 = set(set2.split())

    print(s1.union(s2))


main()
