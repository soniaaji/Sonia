L = [[3,2,1], [3,2,1,4,5], [3,2,1,8,9], [3,2,1,5,7,8,9]]
newl = l[0]
if len(l)>1:
    for Li in L[1:]:
    newl = [X for X in newl if X in Li]
