"""
Co program dělá: zkontroluje vložené uživatelské jméno a heslo, vypočítá plochu stěny a okna,
vypočítá počet tvárnic a zobrazí dostupnost na pobočkách.
Autor: Matvii Shynkarenko
Telefon: +420 123 456 789
Email: matvii.shynkarenko@office365.spspzlin.cz
Uživatelské jméno: stavebnik
Heslo: stavba
"""

print("Konfigurátor zdícího systému")
print("****************************")
print()

uzivatel = input("Zadejte uživatelské jméno: ")
heslo = input("Zadejte heslo: ")

if uzivatel != "stavebnik" or heslo != "stavba":
    print("Zadali jste chybné jméno nebo heslo")
    exit()

print()

delka_steny = float(input("Zadejte délku stěny (metry): "))
vyska_steny = float(input("Zadejte výšku stěny (metry): "))
vyska_okna = float(input("Zadejte výšku okna (metry): "))
sirka_okna = float(input("Zadejte šířku okna (metry): "))

plocha_tvarnice = 0.1

def vypocitej_pocet_tvarnic(delka_steny, vyska_steny, vyska_okna, sirka_okna):
    plocha_celkova = delka_steny * vyska_steny
    plocha_okna = vyska_okna * sirka_okna
    plocha_steny = plocha_celkova - plocha_okna
    pocet_ks = plocha_steny / plocha_tvarnice
   
    return plocha_celkova, plocha_okna, plocha_steny, int(pocet_ks)

plocha_celkova, plocha_okna, plocha_bez_okna, pocet_tvarnic = vypocitej_pocet_tvarnic(delka_steny, vyska_steny, vyska_okna, sirka_okna)

print()

print(f"Plocha stěny včetně okna: {plocha_celkova} m^2")
print(f"Plocha okna: {plocha_okna} m^2")
print(f"Plocha stěny bez okna: {plocha_bez_okna} m^2")
print(f"Počet potřebných tvárnic: {pocet_tvarnic} ks")

print()

print("Dostupnost materiálu na pobočkách")
print("*********************************")
print("| Město    | Druh materiálu | Počet kusů na pobočce |")
print("*****************************************************")

praha = 500
brno = 300
ostrava = 700

if praha >= pocet_tvarnic:
    print(f"| Praha    | tvárnice       | {praha}                   |")

if brno >= pocet_tvarnic:
    print(f"| Brno     | tvárnice       | {brno}                   |")

if ostrava >= pocet_tvarnic:
    print(f"| Ostrava  | tvárnice       | {ostrava}                   |")