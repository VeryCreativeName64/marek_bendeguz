def elso():
    print("I/A,B:")
    nev=input("Név: ")
    email=input("Email cím: ")
    jelszo=input("Jelszó: ")

    if(len(jelszo)>=6):
        print("I/C:")
        print(f"Sikeres regisztráció {nev} ({email})!")
    elif(jelszo==""):
        print("I/C:")
        print("Sikertelen regisztráció (üres jelszó).")
    else:
        print("I/C:")    
        print("Sikertelen regisztráció (kevés karakter).")