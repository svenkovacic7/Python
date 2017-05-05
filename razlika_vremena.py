def vrijeme_u_sekunde(a):
    b = int(a[0])*3600 + int(a[1])*60 + int(a[2])
    return(b)

def sekunde_u_vrijeme(a):
    b = ["0","0","0"]
    a = int(a)
    while a >= 60:
        if a >= 3600:
            b[0] = str(a//3600)
            a -= (a//3600)*3600
        else:
            b[1] = str(a//60)
            a -= (a//60)*60
    b[2] = str(a)
    return(":".join(b))

def razlika_vremena(vrem1,vrem2):
    vrem1 = vrijeme_u_sekunde(vrem1)
    vrem2 = vrijeme_u_sekunde(vrem2)
    rez = abs(vrem2-vrem1)
    rez = sekunde_u_vrijeme(rez)
    return(rez)

def main():
    x = input(">").split(":")
    y = input(">").split(":")
    print(razlika_vremena(x,y))

if __name__ == "__main__":
    main()
