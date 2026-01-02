it_companies = {'facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
print(it_companies)
print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['Uber', 'LinkedIn'])
print(it_companies)
it_companies.remove('IBM')
print(it_companies)

A = {19, 22, 24, 20, 25}
B = {19, 22, 20, 25, 26, 24, 28}
C = A.union(B)
print(C)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
AwB = A.union(B)
BwA = B.union(A)
print(AwB == BwA)
print(A.symmetric_difference(B))
A.clear()
print("Cleared set A: ", A)
B.clear()
print("Cleared set B: ", B)
del A
del B

A_list = [19, 22, 24, 20, 25]
print(type(A_list))
A_set = set(A_list)
print(type(A_set))
if (len(A_list) > len(A_set)):
    print("List Is Bigger Than Set")
elif (len(A_list) < len(A_set)):
    print("Set Is Bigger Than List")
else:
    print("Both Are Equal")
A_list.clear()
del A_list
A_set.clear()
del A_set
