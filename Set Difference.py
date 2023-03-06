if __name__ == '__main__':
    n = int(input())
    set1 = set(map(int, input().split()))
    m = int(input())
    set2 = set(map(int, input().split()))

    diff_set = set1.difference(set2)
    print(len(diff_set))
