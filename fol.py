def is_var(x):
    return isinstance(x, str) and x[0].islower()


def unify(x, y, sub={}):
    if sub is None or x == y:
        return sub
    if is_var(x):
        return unify_var(x, y, sub)
    if is_var(y):
        return unify_var(y, x, sub)
    if isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y):
        for a, b in zip(x, y):
            sub = unify(a, b, sub)
        return sub
    return None


def unify_var(var, val, sub):
    if var in sub:
        return unify(sub[var], val, sub)
    if is_var(val) and val in sub:
        return unify(var, sub[val], sub)
    if var in str(val):
        return None  # Occur check
    return {**sub, var: val}


# Example: Knows(John, x) and Knows(y, Mother(y))
e1 = ("Knows", "John", "x")
e2 = ("Knows", "y", ("Mother", "y"))
print("MGU:", unify(e1, e2))  # Output: {'y': 'John', 'x': ('Mother', 'y')}
