"""
python manually_determine_orders.py
"""

from itertools import combinations
from collections import defaultdict, Counter

def find_next_order(v, xy, colored=None):
    if colored is None:
        colored = set()

    results = {}
    edge_freq = defaultdict(Counter)

    for clq in combinations(range(v), xy):
        edges = list(combinations(clq, 2))

        unaffected = [e for e in edges if e not in colored and (e[1], e[0]) not in colored]
        count = len(unaffected)

        results[count] = results.get(count, 0) + 1

        for e in unaffected:
            edge_freq[count][e] += 1

    print("Clique counts:")
    print(results)
    print()

    for k in sorted(edge_freq):
        print(f"Edge frequencies for cliques with {k} untouched edges:")

        freq_groups = defaultdict(list)

        for edge, freq in edge_freq[k].items():
            freq_groups[freq].append(edge)

        for freq in sorted(freq_groups, reverse=True):
            print(freq, "  ->", freq_groups[freq])
        print()

    return results, edge_freq

def edges_not_in_all(*lists):
    sets = [set(lst) for lst in lists]

    union = set.union(*sets)
    intersection = set.intersection(*sets)
    print(sorted(union-intersection))
    return sorted(union - intersection)

if __name__ == "__main__":
    find_next_order(12,5,[(0,1),(2,3),(4,5),(6,7),(8,9),(10,11),(0,2),(4,6)])