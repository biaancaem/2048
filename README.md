# 2048

## Autori și contribuții
Proiectul a fost realizat în echipă, fiecare membru având contribuții distincte în dezvoltarea proiectului.
- **Militaru Elena-Bianca** – interfață grafică, meniuri de configurare, moduri de joc (obstacole, mutări limitate), ecrane de start și final, documentație
- **Artîc Diana-Andreea** – logică de joc, manipularea tablei, mutarea și combinarea casetelor
- **Draica Diana Andreea** – gestionarea scorului, condiții de câștig/pierdere, functii de undo/redo,optiune pentru timp

## Link catre repository
    Codul sursă al proiectului este disponibil la următorul link:
    https://github.com/biaancaem/2048.git

## Limbaje și tehnologii folosite
Aplicația a fost dezvoltată utilizând următoarele limbaje și tehnologii:
- **Python 3** – limbajul principal de programare, utilizat pentru implementarea logicii aplicației și coordonarea componentelor acesteia;
- **pygame** – bibliotecă Python folosită pentru realizarea interfeței grafice, desenarea elementelor vizuale, gestionarea evenimentelor de la tastatură și mouse, precum și pentru controlul timpului de rulare;
- **Git** – sistem de control al versiunilor, utilizat pentru gestionarea codului sursă și colaborarea în echipă;
- **GitHub** – platformă utilizată pentru stocarea și distribuirea repository-ului proiectului.

## Instrucțiuni de rulare și folosire
Aplicatia se ruleaza folosind comanda `python3 main_final.py`

## Scurtă descriere a aplicației

Aplicația implementată reprezintă o versiune extinsă a jocului 2048, dezvoltată în limbajul de programare Python, utilizând biblioteca pygame pentru realizarea interfeței grafice. Scopul aplicației este de a oferi utilizatorului o experiență de joc interactivă, care să permită combinarea casetelor numerice într-o tablă de joc, cu obiectivul obținerii valorii 2048 sau a unui scor cât mai ridicat.

Față de implementarea clasică, aplicația oferă funcționalități suplimentare care permit configurarea jocului, precum alegerea dimensiunii tablei, activarea unui mod de joc cu obstacole și utilizarea unui mod de joc cu mutări limitate. În plus, sunt implementate ecrane dedicate pentru pornirea aplicației, afișarea regulilor jocului și gestionarea stărilor finale, precum câștigul sau pierderea.

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


##  Contributie proiect - Bianca
In cadrul acestui proiect m-am ocupat de realizarea unei părți semnificative a interfeței grafice și a sistemelor de configurare ale jocului. Responsabilitatile mele au fost:

- dezvoltarea interfeței grafice a jocului;
- afișarea tablei de joc și a elementelor vizuale;
- afisarea ecranelor de start, logo și reguli;
- dezvoltarea meniurilor interactive pentru configurarea jocului;
- dezvoltarea modului de joc cu obstacole;
- dezvoltarea modului de joc cu mutări limitate;
- dezvoltarea sistemului de selectare a dificultății pentru fiecare mod.

##  Utilizarea metodelor din biblioteca pygame 
În cadrul acestui proiect am utilizat mai multe funcții și clase oferite de biblioteca **pygame**, necesare pentru realizarea interfeței grafice, gestionarea evenimentelor și afișarea elementelor vizuale. Mai jos sunt prezentate toate funcțiile din pygame utilizate efectiv în cod, împreună cu rolul fiecăreia.

- **`pygame.display.set_caption()`**
Această funcție este utilizată pentru setarea titlului ferestrei aplicației. În proiect, funcția este folosită pentru a afișa un titlu sugestiv în bara ferestrei jocului, îmbunătățind experiența utilizatorului.

- **`pygame.display.flip()`**
Funcția actualizează întregul ecran cu toate elementele desenate în cadrul frame-ului curent. Aceasta este esențială pentru afișarea modificărilor vizuale realizate în timpul jocului sau în meniuri.

- **`pygame.event.get()`**
Această funcție preia toate evenimentele generate de utilizator sau sistem, precum apăsarea tastelor, click-urile mouse-ului sau închiderea ferestrei. Este utilizată în toate ecranele interactive pentru a gestiona input-ul utilizatorului.

- **`pygame.QUIT`**
Este un tip de eveniment care indică închiderea ferestrei jocului. În proiect, acest eveniment este tratat pentru a închide aplicația în mod controlat.

- **`pygame.KEYDOWN`**
Acest eveniment este declanșat atunci când utilizatorul apasă o tastă. Este utilizat pentru navigarea prin meniuri și selectarea opțiunilor de joc.

-  **`pygame.MOUSEBUTTONDOWN`**
Eveniment care indică apăsarea unui buton al mouse-ului. În proiect, este utilizat pentru ieșirea din ecranul de tip splash.

- **`pygame.Rect`**
  Această metodă este utilizată pentru a defini dreptunghiuri invizibile care descriu poziția și dimensiunea elementelor grafice de pe ecran. În cadrul proiectului, `pygame.Rect` este folosit pentru stabilirea poziției casetelor din tablă, a panoului de scor și a altor elemente grafice. Dreptunghiurile create facilitează atât desenarea elementelor, cât și alinierea și centrarea acestora.

- **`pygame.draw.rect`**
  Metoda `pygame.draw.rect` este utilizată pentru desenarea efectivă a dreptunghiurilor pe ecran. În acest proiect, această funcție este folosită pentru afișarea casetelor din tablă, a casetelor de scor și a altor componente vizuale. Prin intermediul acestei metode se pot specifica culoarea, dimensiunea și colțurile rotunjite ale fiecărui element, contribuind la un aspect vizual plăcut.

- **`pygame.Surface()`**
Această funcție creează o suprafață grafică nouă. Este utilizată pentru realizarea overlay-urilor semi-transparente afișate în stările de GAME OVER și YOU WIN.

- **`Surface.set_alpha()`**
Metodă utilizată pentru a seta transparența unei suprafețe grafice. În proiect, este folosită pentru a crea efecte de estompare peste joc atunci când se afișează overlay-uri.

- **`Surface.fill()`**
Această metodă umple o suprafață cu o culoare specifică. Este utilizată atât pentru fundalul ferestrei, cât și pentru suprafețele de tip overlay.

- **`Surface.blit()`**
Metoda `blit` copiază o suprafață grafică (text sau imagine) pe o altă suprafață. Este esențială pentru afișarea textului, imaginilor și a elementelor grafice pe ecran.

- **`pygame.font.SysFont()`**
Această funcție creează un obiect de tip font folosind un font de sistem. În proiect, este utilizată pentru afișarea textului, scorurilor și mesajelor informative.


- **`font.render`**
  Metoda `font.render` este folosită pentru transformarea textului (de exemplu scorul, valorile numerice sau mesajele afișate) într-o suprafață grafică ce poate fi desenată pe ecran. Această metodă permite controlul fontului, al culorii și al netezirii marginilor textului, asigurând lizibilitate și un contrast corespunzător față de fundal.

- **`pygame.image.load()`**
Această funcție încarcă o imagine dintr-un fișier. În proiect, este utilizată pentru afișarea imaginii de start a jocului.

- **`convert_alpha()`**
Metodă utilizată pentru optimizarea imaginilor cu transparență. Aceasta îmbunătățește performanța și calitatea afișării imaginilor.

- **`pygame.transform.smoothscale()`**
Această funcție scalează o imagine la o dimensiune specificată, folosind un algoritm de interpolare care oferă o calitate mai bună a imaginii. Este utilizată pentru a adapta imaginea de start la dimensiunea ferestrei.

- **`pygame.time.Clock()`**
Această clasă este utilizată pentru controlul vitezei de rulare a aplicației. În proiect, este folosită pentru a limita jocul la un număr constant de cadre pe secundă.

- **`Clock.tick()`**
Metodă care limitează numărul de cadre pe secundă. În proiect, este utilizată pentru a asigura o rulare fluentă a aplicației.

- **`blit`**
  Metoda `blit` este utilizată pentru a copia o suprafață grafică (imagine, text sau overlay) pe suprafața principală a ferestrei de joc. În cadrul proiectului, `blit` este folosit pentru afișarea textului, a imaginilor și a suprapunerilor grafice (overlay-uri) precum ecranele de Game Over sau Win. Această metodă este esențială pentru afișarea finală a tuturor elementelor grafice pe ecran.

## Descrierea functiilor implementate
In cadrul acestui proiect au fost implementate mai multe functii,fiecare avand un rol bine definit in realizarea interfetei grafice.
Fisierul `graphics.py` contine urmatoarele functii:

- `dimensiune_fereastra(board_size)`
    Această funcție calculează dimensiunea ferestrei de joc în funcție de dimensiunea tablei alese de utilizator.  
Funcția ia în considerare dimensiunea casetelor, spațiul dintre acestea și înălțimea panoului de informații, asigurând afișarea corectă a tuturor elementelor grafice.  
Rezultatul returnat este un tuplu format din lățimea și înălțimea ferestrei.

- `draw_board(screen, board, font, score, best_score, moves_left, remaining_time, timed_mode, game_over, is_new_best, has_won, win_screen_active)`

Aceasta este funcția principală de desenare a jocului.
Rolul său este de a reda vizual starea curentă a jocului la fiecare actualizare a ecranului.

Funcția realizează următoarele operații:
- desenează fundalul ferestrei;
- afișează casetele de tip SCORE, BEST și MOVES;
- desenează tabla de joc și poziționează fiecare casetă corect;
- afișează valorile numerice și obstacolele;
- afișează overlay-urile pentru stările GAME OVER și YOU WIN.

- `show_start_screen(screen)`

Această funcție afișează ecranul de start al jocului, care conține titlul, regulile jocului și opțiunile pentru alegerea dimensiunii tablei.  
Interacțiunea se face prin tastatură, iar funcția returnează dimensiunea tablei selectate de utilizator.

- `show_logo_screen(screen)`

Funcția afișează un ecran de tip splash la pornirea aplicației.  
Aceasta încarcă și afișează o imagine reprezentativă pentru joc și așteaptă o acțiune din partea utilizatorului (tastă sau click) pentru a continua.

Fisierul `obstacole_options.py` contine urmatoarele functii:
- `get_obstacle_count(board_size, difficulty)`

Această funcție calculează numărul de obstacole ce vor fi plasate pe tabla de joc, în funcție de dimensiunea tablei și de dificultatea aleasă.
Funcția permite scalarea corectă a dificultății pentru diferite dimensiuni ale tablei.

- `choose_obstacle_mode(screen)`

Funcția afișează un ecran de selecție care permite utilizatorului să aleagă între modul de joc normal și modul cu obstacole.
Selecția este realizată prin apăsarea tastelor corespunzătoare.

- `choose_obstacle_difficulty(screen)`

Această funcție permite utilizatorului să selecteze dificultatea modului cu obstacole.
În funcție de opțiunea aleasă, funcția returnează nivelul de dificultate selectat.

- `choose_moves_mode(screen)`

Funcția oferă utilizatorului posibilitatea de a activa sau dezactiva modul de joc cu mutări limitate.
Aceasta returnează opțiunea aleasă de utilizator.

- `choose_moves_difficulty(screen)`

Această funcție stabilește numărul maxim de mutări disponibile în joc, în funcție de dificultatea aleasă.
Valoarea returnată este utilizată ulterior pentru controlul desfășurării jocului.

## Dificultăți întâmpinate și soluții aplicate

O primă dificultate întâmpinată a fost **gestionarea corectă a evenimentelor de la tastatură și mouse în biblioteca pygame**. Inițial, anumite apăsări de taste nu erau recunoscute sau produceau comportamente neașteptate. Această problemă a fost rezolvată prin utilizarea funcției `pygame.event.get()` și prin tratarea explicită a evenimentelor de tip `pygame.KEYDOWN` și `pygame.MOUSEBUTTONDOWN`, separând logica de input pentru fiecare ecran al aplicației.

O altă dificultate a fost **centrarea corectă a textului și a elementelor grafice pe ecran**, indiferent de dimensiunea ferestrei. Poziționarea manuală a elementelor ducea la erori vizuale. Am rezolvat această problemă prin utilizarea obiectelor `pygame.Rect` și a metodei `get_rect(center=...)`, care permit poziționarea dinamică și precisă a elementelor grafice.

De asemenea, **echilibrarea dificultății jocului**, în special în modul cu obstacole, a reprezentat o provocare. Numărul de obstacole trebuia adaptat atât la dimensiunea tablei, cât și la nivelul de dificultate ales. Această problemă a fost rezolvată prin implementarea unei funcții dedicate care calculează automat numărul de obstacole în funcție de acești parametri.

O dificultate suplimentară a fost **afișarea overlay-urilor pentru stările de Game Over și Win**, fără a afecta vizibilitatea tablei de joc. Inițial, overlay-urile acopereau complet elementele grafice. Am rezolvat această problemă prin utilizarea suprafețelor `pygame.Surface` și setarea transparenței acestora cu metoda `set_alpha`.

