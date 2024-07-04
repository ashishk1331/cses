import heapq

# n, m, k = list(map(int, input().split()))
# apl = list(map(int, input().split()))
# apt = list(map(int, input().split()))

n, m, k = list(map(int, "4 3 5".split()))
apl = list(map(int, "60 45 80 60".split()))
apt = list(map(int, "30 60 75".split()))

heapq.heapify(apl)
heapq.heapify(apt)
