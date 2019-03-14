def palalala(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and palalala(s[1:-1])
