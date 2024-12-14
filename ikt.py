#Készíts programot, amely bekér két számot (-10.000 és 10.000 között) és egy műveleti jelet (+, -, *, /). A program végezze el a megfelelő műveletet, és írja ki az eredményt. Ellenőrizze, hogy az osztó nem nulla-e, mielőtt osztást végez. Minden begépelt adat formai és tartalmi ellenőrzése kötelező! Tároljuk a kiszámolt eredményeket és adjuk meg az eredmények mediánját!
eredmenyek = []
ok = True
nulla_e = False
while ok:
    print("\nA bekért számokat a (-10.000 és 10.000 közötti) intervallumból adja meg!")
    szamja = input("Adjon meg egy számot amivel dolgozhatunk: ")
    if szamja == "":
        print("Kérjük írjon be vala milyen számot")
    else:
        if szamja.replace('.', '', 1).isdigit() or (szamja[0] == '-' and szamja[1:].replace('.', '', 1).isdigit()):
            szam = float(szamja)
            if szam > 10000 or szam < -10000:
                print("\nNem a megfelelő intervallumot használta!")
            else:
                osztoja = input("Adjon meg egy másik számot amivel dolgozhatunk: ")
                if osztoja == "":
                    print("Kérjük írjon be vala milyen számot")
                else:
                    if osztoja.replace('.', '', 1).isdigit() or (osztoja[0] == '-' and osztoja[1:].replace('.', '', 1).isdigit()):
                        oszto = float(osztoja)
                        if oszto > 10000 or oszto < -10000:
                            print("\nNem a megfelelő intervallumot használta!")
                        else:
                            muveleti_jel = input("Adjon meg egy műveleti jelet (+, -, *, /):")
                            if muveleti_jel != "+" and muveleti_jel != "-" and muveleti_jel != "/" and muveleti_jel != "*":
                                print("\nNem a megfelelő műveletijeleket használta!")
                            else:
                                if muveleti_jel == "+":
                                    osszeg = szam+oszto
                                elif muveleti_jel == "-":
                                    osszeg = szam-oszto
                                elif muveleti_jel == "*":
                                    osszeg = szam*oszto
                                elif muveleti_jel == "/":
                                    if oszto == 0:
                                        print("\nNullával való osztásnak nincs értelme!")
                                        nulla_e = True
                                    else:
                                        nulla_e = False
                                        osszeg = szam/oszto
                                if not nulla_e:
                                    eredmenyek.append(osszeg)
                                    print(osszeg)
                                    szeretne = input("\nSzeretne megadni új műveletet? Ha szeretne akkor ÜSS i-t, ha nem akkor ENTERT. ").lower()
                                    if szeretne == "n":
                                        print("Rendben akkor kilép. Viszlát!")
                                        ok = False
                                    elif szeretne == "":
                                        print("Rendben akkor kilép. Viszlát!")
                                        ok = False
                                    elif szeretne == "i":
                                        print("Rendben akkor tessék: ")
                                    elif szeretne != "i":
                                        print("Nem értjük mit szeretne!")
                                    else:
                                        ok = False
                                else:
                                    print("Leközelebb ne 0-ával osszon.")

                    else:
                        print("\nCsak szám karaktereket adhet meg!")
        else:
            print("\nCsak szám karaktereket adhet meg!")
    

kozep = len(eredmenyek) // 2

if len(eredmenyek) % 2 == 0:
    kozep1 = eredmenyek[kozep-1]
    kozep2 = eredmenyek[kozep]
    print("A középső értékek mediánja",(kozep1+kozep2)/2+"!")
else:
    kozep1 = eredmenyek[kozep]
    print("A középső érték mediánja",kozep1,".")
























