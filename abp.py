def alphabeta(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or isinstance(node, int):
        return node

    if maximizingPlayer:
        for child in node:
            alpha = max(alpha, alphabeta(child, depth - 1, alpha, beta, False))
            if beta <= alpha:
                break 
        return alpha
    else:
        for child in node:
            beta = min(beta, alphabeta(child, depth - 1, alpha, beta, True))
            if beta <= alpha:
                break 
        return beta

tree = [
    [[3, 5], [6, 9]],
    [[1, 2], [0, -1]]
]

result = alphabeta(tree, 3, float('-inf'), float('inf'), True)
print("Optimal Value:", result)
