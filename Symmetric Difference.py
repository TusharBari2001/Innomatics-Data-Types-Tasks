if __name__ == '__main__':
    m = int(input())
    set1 = set(map(int, input().split()))
    n = int(input())
    set2 = set(map(int, input().split()))

    sym_diff_set = set1.symmetric_difference(set2)
    sym_diff_list = list(sym_diff_set)
    sym_diff_list.sort()

    for i in sym_diff_list:
        print(i)
