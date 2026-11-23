from itertools import combinations


def resolve(c1, c2):
    for l in c1:
        neg = l[1:] if l.startswith("~") else "~" + l
        if neg in c2:
            return (c1 - {l}) | (c2 - {neg})
    return None


def resolution(kb, neg_query):
    clauses = [set(c) for c in kb] + [set(neg_query)]
    while True:
        new = []
        for c1, c2 in combinations(clauses, 2):
            res = resolve(c1, c2)
            if res == set():
                return True  # Empty clause = Proved
            if res and res not in clauses and res not in new:
                new.append(res)
        if not new:
            return False  # No new clauses = Failed
        clauses.extend(new)


# Example: (R -> W), (W -> S), R  |-  S
kb = [{"~R", "W"}, {"~W", "S"}, {"R"}]
print("Proved:", resolution(kb, {"~S"}))  # Output: True
