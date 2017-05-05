imena = ["pero","ivo","franka","anastazija"]
while len(imena) != 1:
    for i in range(len(imena)//2): #Ovo radi, ne diraj
        if ((len(imena[i]) + len(imena[i+1])) % 2):
            del imena[i]
        else:
            del imena[i+1]
print("".join(imena).title())
