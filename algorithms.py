def search(puzzle, a, b):
    if not puzzle.solvable:
        return None            # parity, can't solve it

    import Queue
    pq = Queue.PriorityQueue()
    pq.put((0, 0, puzzle.initial_state))
    parent = {}
    parent[puzzle.initial_state] = None

    while not pq.empty():
        (_, distance, cur) = pq.get()
        if cur == puzzle.goal_state:  # found solution
            path = [cur]
            while parent[cur]:
                path.append(parent[cur])
                cur = parent[cur]
            return path[::-1]
        for nxt in puzzle.sucessors(cur):
            if nxt not in parent:
                parent[nxt] = cur
                pq.put((a * distance + b * puzzle.heuristic(nxt), distance + 1, nxt))

    return None             # cannot find solution


def a_star(puzzle):
    return search(puzzle, 1, 1)


def weighted_a_start(puzzle, weight):
    return search(puzzle, 1, weight)


def greedy_best_fisrt_search(puzzle):
    return search(puzzle, 0, 1)
