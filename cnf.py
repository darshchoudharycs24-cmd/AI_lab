import re

def fol_to_cnf(expr):
    term = r"~?\w+\([^()]*(?:\([^()]*\)[^()]*)*\)"

    expr = re.sub(rf"({term})\s*->\s*(\([^&|]+&[^|]+\)|{term})", r"~\1 | \2", expr)

    expr = expr.replace("~forall ", "exists ~").replace("~exists ", "forall ~")
    expr = expr.replace("~~", "")

    univ_vars = re.findall(r"forall\s+(\w+)", expr)
    skolem_idx = 1
    for var in re.findall(r"exists\s+(\w+)", expr):
        skolem = f"f{skolem_idx}({','.join(univ_vars)})" if univ_vars else f"C{skolem_idx}"
        expr = re.sub(rf"exists\s+{var}\s*", "", expr)
        expr = re.sub(rf"\b{var}\b", skolem, expr)
        skolem_idx += 1

    expr = re.sub(r"forall\s+\w+\s*", "", expr).strip()
    if expr.startswith("(") and expr.endswith(")"):
        expr = expr[1:-1].strip()

    expr = re.sub(rf"({term})\s*\|\s*\(\s*({term})\s*&\s*({term})\s*\)", r"(\1 | \2) & (\1 | \3)", expr)
    expr = re.sub(rf"\(\s*({term})\s*&\s*({term})\s*\)\s*\|\s*({term})", r"(\1 | \3) & (\2 | \3)", expr)

    clauses = []
    for c in expr.split("&"):
        c = c.strip()
        if c.startswith("(") and c.endswith(")"):
            c = c[1:-1].strip()
        clauses.append(c)

    return expr, clauses

fol = "forall x exists y (P(x) -> (Q(x, y) & R(y)))"
cnf, clauses = fol_to_cnf(fol)

print("Input  :", fol)
print("CNF    :", cnf)
print("Clauses:", clauses)
