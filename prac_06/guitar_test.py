from prac_06.guitar import Guitar


def main():
    # gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    # another_guitar = Guitar("Another Guitar", 1959, 50)
    # print("{} get_age() 96? got {}".format(gibson.name, gibson.get_age()))
    # print("{} is_vintage() True? got {}".format(gibson.name, gibson.is_vintage()))

    print("My Guitars!")
    guitars = []
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.append(Guitar("Lag Arcane", 2009, 650.75))

    while True:
        name = input("Guitar Name: ")
        if name == '':
            break
        year = int(input("Guitar make Year: "))
        cost = int(input("Guitar Cost: "))
        guitars.append(Guitar(name, year, cost))

    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        vintage = "(vintage)" if guitar.is_vintage() else ""
        print("Guitar {}: {} ({}), worth ${:,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage))


main()
