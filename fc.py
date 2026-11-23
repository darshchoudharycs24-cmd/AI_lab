facts = {
    ("American", "West"),
    ("Enemy", "Nono", "America"),
    ("Owns", "Nono", "M1"),
    ("Missile", "M1")
}

rules = [
    ([("Missile", "x")], ("Weapon", "x")),
    ([("Enemy", "x", "America")], ("Hostile", "x")),
    ([("Missile", "x"), ("Owns", "Nono", "x")], ("Sells", "West", "x", "Nono")),
    ([("American", "x"), ("Weapon", "y"), ("Sells", "x", "y", "z"), ("Hostile", "z")], ("Criminal", "x"))
]

query = ("Criminal", "West")

def match(pattern, fact, theta):
    if pattern[0] != fact[0] or len(pattern) != len(fact):
        return None
    new_theta = theta.copy()
    for p, f in zip(pattern[1:], fact[1:]):
        if p.islower():  
            if p in new_theta and new_theta[p] != f:
                return None
            new_theta[p] = f
        elif p != f:    
            return None
    return new_theta

def forward_chaining(facts, rules, query):
    while query not in facts:
        added = False
        for premises, conclusion in rules:
            matches = [{}]
            for premise in premises:
                matches = [m for theta in matches for fact in facts if (m := match(premise, fact, theta)) is not None]
            for theta in matches:
                new_fact = tuple(theta.get(x, x) for x in conclusion)
                if new_fact not in facts:
                    print("Inferred:", new_fact)
                    facts.add(new_fact)
                    added = True
        if not added:
            return False
    return True

print("Proved:", forward_chaining(facts, rules, query))
