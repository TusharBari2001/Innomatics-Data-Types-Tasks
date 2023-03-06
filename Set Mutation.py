if __name__ == '__main__':
    n = int(input())
    A = set(map(int, input().split()))
    N = int(input())

    for i in range(N):
        command = input().split()
        other_set = set(map(int, input().split()))

        if command[0] == "intersection_update":
            A.intersection_update(other_set)
        elif command[0] == "update":
            A.update(other_set)
        elif command[0] == "symmetric_difference_update":
            A.symmetric_difference_update(other_set)
        elif command[0] == "difference_update":
            A.difference_update(other_set)
        else:
            raise ValueError("Invalid command")

    print(sum(A))
