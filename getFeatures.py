import networkx as nx


# 1. number of active neighboors

# 2. Personal Network Exposure

# 3. Average in neighboor count of active neighboors


def get_f1(N, user):
    return list(N.neighbors(user))

def get_f2(N):
    pass


def get_f3(N, users): # G.out_degree(1) average
    sum = 0
    for usr in users:
        sum += (N.in_degree(usr))
    return sum/len(users)    
