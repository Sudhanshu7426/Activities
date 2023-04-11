def factor(SP,CP):
    C = 13.12 + 0.6215 * SP * (0.3965 * SP - 11.37) * (CP**0.16)
    return C
factor(1,2)
