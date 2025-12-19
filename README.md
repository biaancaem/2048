# 2048-


README
1) initializarea jocului 2048
-	acest fisier se ocupa de initializarea logica a jocului 2048, avand rolul de a pregati tabla de joc inainte ca utilizatorul sa inceapa efectiv sa joace
-	este definita o constanta pentru obstacole, reprezentate prin valoarea -1, care blocheaza miscarea si combinarea numerelor
-	functia create_empty_board creeaza o tabla patrata de dimensiune aleasa, in care toate celulele sunt initializate cu valoarea 0, ceea ce inseamna ca sunt libere
-	pentru a preveni erori, functia is_board_valid verifica daca tabla este corecta din punct de vedere logic, asigurand existenta tablei, forma patrata si valori valide
-	functia add_nr_random adauga un numar nou pe tabla intr-o celula libera aleasa aleator, valoarea fiind de regula 2, iar mai rar 4
-	functia init_game initializeaza complet jocul, adaugand doua valori initiale, obstacolele daca modul este activ, scorul initial si starea jocului
-	functia returneaza toate valorile necesare pentru ca jocul sa poata incepe intr-o stare corecta si stabila

2) logica mutarilor si regulile jocului 2048
-	acest fisier contine logica centrala a jocului 2048, fiind responsabil de modul in care tabla se modifica in urma actiunilor utilizatorului
-	obstacolele sunt definite prin valoarea -1 si impart tabla in segmente independente care sunt procesate separat
-	pentru a evita modificarea directa a tablei originale, functia copy_board creeaza o copie completa a tablei, necesara pentru verificarea mutarilor
-	functia compress elimina valorile zero si apropie valorile diferite de zero, pastrand ordinea acestora
-	functia merge combina valorile egale aflate una langa alta, dubland valoarea si calculand scorul obtinut
-	functia process_segment reuneste comprimarea si combinarea pentru un segment delimitat de obstacole
-	mutarile sunt implementate prin patru functii separate: move_left, move_right, move_up si move_down, fiecare adaptata directiei corespunzatoare
-	functia move_board primeste directia ca text, aplica mutarea corecta si verifica daca tabla s-a modificat
-	functia any_moves_possible verifica daca jocul poate continua, analizand existenta celulelor libere sau a combinarilor posibile
-	logica pentru dificultate este gestionata prin get_obstacle_count si get_moves_by_difficulty, care ajusteaza numarul de obstacole si mutari disponibile


3) grafica pentru salvarea jocului, undo/redo

    Unul dintre primele lucruri realizate in acest fisier este alegerea modului de joc. Atunci cand jocul porneste, jucatorul este intrebat daca doreste sa joace in modul normal sau in modul cu timp. Acest lucru se face printr-un ecran cu textul centrat, in care utilizatorul apasa o tasta pentru a face alegerea. Daca apasa T, jocul va avea timp limitat. Daca apasa N sau ENTER, jocul va fi fara timp. Functia nu porneste cronometrul, ci doar memoreaza ce tip de joc a fost ales.

    Dupa ce jocul incepe, se afiseaza in partea de sus un HUD. HUD este zona unde apar scorul curent, cel mai bun scor si, daca este cazul, numarul de mutari ramase. Sub acest HUD este desenat un panou suplimentar care contine butoanele UNDO si REDO, precum si timpul ramas, daca jocul este in modul cu timp.

    Codul calculeaza centrul zonei HUD si foloseste acest centru pentru a aseza casutele UNDO si REDO, astfel incat ele sa fie aliniate.

    Afisarea timpului este realizata doar daca jocul este in modul cu timp. Timpul este afisat intr-o casuta separata, sub UNDO si REDO, iar culoarea acesteia se schimba in functie de cat timp mai ramane. Cand timpul este mai mare de 10 secunde, casuta este gri. Cand timpul scade sub 10 secunde, casuta devine rosie.

    Cronometrul in sine functioneaza pe baza timpului intern al Pygame. La pornirea jocului se memoreaza momentul de start, iar la fiecare frame se calculeaza cat timp a trecut de atunci. Diferenta dintre timpul total permis si timpul trecut reprezinta timpul ramas.

    La fiecare desenare a ecranului, toate elementele sunt afisate din nou, iar la final se face un update complet al ferestrei, astfel incat jucatorul sa vada orice schimbare.

5) modul de salvare

    Fisierul de salvare si incarcare este cel care permite jocului sa fie inchis si redeschis fara pierderea progresului.

    Atunci cand jocul este salvat, toate informatiile importante sunt puse intr-un dictionar. Acest dictionar contine tabla de joc, scorul curent, cel mai bun scor, numarul de mutari ramase, informatia despre modul cu timp, timpul ramas, obstacolele si stivele de undo si redo. Acest dictionar este scris intr-un fisier JSON.

    La pornirea jocului, se verifica daca acest fisier de salvare exista. Daca nu exista, jocul porneste normal. Daca exista, utilizatorul este intrebat daca doreste sa continue jocul anterior sau sa inceapa unul nou. Aceasta intrebare este afisata intr-un ecran simplu, iar utilizatorul raspunde prin apasarea tastelor Y sau N (yes sau no).

    Daca utilizatorul alege sa continue, jocul citeste fisierul JSON si restaureaza toate valorile salvate. Tabla de joc este refacuta exact asa cum era, scorurile sunt restaurate, iar starile interne, precum win screen sau undo si redo, sunt repuse in memorie.

    In cazul modului cu timp, la continuarea jocului cronometrul este repornit de la momentul reluarii.

    Daca utilizatorul alege sa nu continue jocul, fisierul de salvare este sters, iar jocul porneste de la zero, ca un joc nou.
