n = int(input())

list = [int(x) for x in input().split()]

m = int(input())

id = [int(x) for x in input().split()]



for i in id:
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end )//2
        if list[mid] == i:
            print("Preparem o vidro de dragao!!!")
            exit()
        elif list[mid] > i:
            end = mid - 1
        elif list[mid] < i:
            start = mid + 1 
print("E assim termina nossa vigilia")
