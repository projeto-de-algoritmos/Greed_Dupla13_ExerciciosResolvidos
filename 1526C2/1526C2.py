import heapq

number_potions = int(input())
potions = [int(x) for x in input().split()]

pq = []
heapq.heapify(pq)

curr_health = 0
potions_drinked = 0

for potion in potions:
  curr_health += potion
  heapq.heappush(pq, potion)
  while(curr_health < 0):
    curr_health -= pq[0]
    heapq.heappop(pq)

print(len(pq))