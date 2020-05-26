import random
l=range(0,5)
pc=0
pu=0
for u in l:
    print("ur turn")
    print("press s for stone")
    print("press p for paper")
    print("press sc for scissor")
    i = input()
    s = "s"
    p = "p"
    sc = "sc"
    lis = [s, p, sc]
    ra = random.choice(lis)

    if (i == s)&(ra==i):

        pu = pu + 0
        pc = pc + 0
        print("pc chose",ra)
        print("no one won")
    elif (i ==s)&(ra==p):
        pu = pu + 0
        pc = pc + 10
        print("pc chose",ra)
        print("pc won")
    elif (i==s)&(ra==sc):
        pu = pu + 10
        pc = pc + 0
        print("pc chose",ra)
        print("u won")
    elif (i==p)&(ra==i):
        pu = pu + 0
        pc = pc + 0
        print("pc chose",ra)
        print("no one won")
    elif (i == p ) &(ra == sc):
        pu = pu + 0
        pc = pc + 10
        print("pc chose",ra)
        print("pc won")
    elif(i == p)&(ra == s):
        pu = pu + 10
        pc = pc + 0
        print("pc chose",ra)
        print("u won")
    elif(i==sc)&(ra==i):
        pu=pu+0
        pc=pc+0
        print("pc chose",ra)
        print("no one won")
    elif(i==sc)&(ra==s):
        pu = pu + 0
        pc = pc + 10
        print("pc chose",ra)
        print("pc won")
    elif (i==sc)&(ra==p):
        pu = pu + 10
        pc = pc + 0
        print("pc chose",ra)
        print("u won ")
    elif (i!=sc)&(i!=p)&(i!=s):
        print("u have entered wrong digit")
        print("so u are a fool")


print("The Final Scores are :")
print("Total Points of User",pu)
print("Total Points of Comp",pc)