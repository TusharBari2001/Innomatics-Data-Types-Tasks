# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    countries = set()

    for i in range(n):
        country = input()
        countries.add(country)

    print(len(countries))
