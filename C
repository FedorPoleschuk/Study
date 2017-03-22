from heapq import *


def dey(G, a):
    """дейкстра с кучей"""
    distances = [float('+inf')] * len(G)
    distances[a] = 0
    Q = [(0, a)]
    used = set()
    while Q:
        curr_d, curr = heappop(Q)
        if curr_d != distances[curr]:
            continue
        for neibor in G[curr]:
            if neibor not in used:
                new_dist = distances[curr] + G[curr][neibor]
                if new_dist < distances[neibor]:
                    distances[neibor] = new_dist
                    heappush(Q, (new_dist, neibor))
        used.add(curr)
    return distances


# reading
input_data = [int(x) for x in input().split()]
n = input_data[0]  # количество вершин
m = input_data[1]  # рёбер
main_cities = input_data[2:]

G = {x: {} for x in range(n)}
for main_city in range(m):
    a, b, w = [int(x) for x in input().split()]
    G[a][b] = w
    G[b][a] = w

# finding
distances = {main_city:[] for main_city in main_cities}
for main_city in main_cities:
    distances[main_city] = dey(G, main_city)

for city in range(n):
    # ищем ближайший
    if city in main_cities:
        print(city)
    else:
        min_d = float("+inf")
        center = -1
        for main_city in main_cities:
            if distances[main_city][city] < min_d:
                min_d = distances[main_city][city]
                center = main_city
        print(center)
