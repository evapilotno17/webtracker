import string

VALID_CHARS = "abcdefghijklmnopqrstuvwxyz0123456789."
N = len(VALID_CHARS)

def F(s: str, perm: str) -> str:
    assert len(perm) == N and set(perm) == set(VALID_CHARS), "Invalid permutation"
    table = str.maketrans(VALID_CHARS, perm)
    return s.translate(table)

def F_inv(s: str, perm: str) -> str:
    assert len(perm) == N and set(perm) == set(VALID_CHARS), "Invalid permutation"
    inv_perm = ''.join(sorted(VALID_CHARS, key=lambda c: perm.index(c)))
    table = str.maketrans(perm, VALID_CHARS)
    return s.translate(table)
