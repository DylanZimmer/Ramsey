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
        for edge, freq in edge_freq[k].most_common():
            print(edge, freq)
        print()

    return results, edge_freq