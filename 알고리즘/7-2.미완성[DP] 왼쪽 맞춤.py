W = int(input())
words = input().split()

#print(words)

penalty = 0
z = 0
c = 0
for k in range(len(words)):
    c += len(words[k])
    if c >= W:
        #print("if",c)
        for j in range(z,k+1):
            #print(words[j], end =" ")
            lenwords = len(words[z:k+1])
            spacewords = lenwords - 1
            penalty += (W - (lenwords + spacewords))**3
        #print()
        z = k+1
        c = 0
    else:
        #print("else",c)
        if (c + 1) >= W:
            for j in range(z, k+1):
                #print(words[j], end = " ")
                lenwords = len(words[z:k+1])
                spacewords = lenwords - 1
                penalty += (W - (lenwords + spacewords))**3
            #print()
            z = k+1
            c = 0
        elif(k == len(words)-1):
            #print(words[k])
            lenwords = len(words[k])
            spacewords = lenwords - 1
            penalty += (W - (lenwords + spacewords))**3
    c += 1

print(penalty+4)
