if __name__ == '__main__':
    n = int(input())
    set1 = set(map(int, input().split()))
    m = int(input())
    set2 = set(map(int, input().split()))

    sym_diff_set = set1.symmetric_difference(set2)
    print(len(sym_diff_set))
