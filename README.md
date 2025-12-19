# 2048

## Autori și contribuții
Proiectul a fost realizat în echipă, fiecare membru având contribuții distincte în dezvoltarea proiectului.
- **Militaru Elena-Bianca** – dezvoltarea interfeței grafice a aplicației, implementarea meniurilor de configurare pentru modurile de joc, realizarea ecranelor de start și final
- **Artîc Diana-Andreea** – logică de joc, manipularea tablei, mutarea și combinarea casetelor, moduri de joc (obstacole, mutări limitate)
- **Draica Diana Andreea** – gestionarea scorului, condiții de câștig/pierdere, functii de undo/redo, optiune pentru timp si sunet

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

##  Contributie proiect - Diana Artic

In cadrul acest proiect am contribuit la dezvoltarea jocului 2048, fiind implicata in special in implementarea logicii de initializare a jocului, a regulilor de mutare, precum si a sistemelor de configurare si dificultate. Accentul a fost pus pe separatea clara intre logica jocului si interfata grafica, pentru a obtine un cod clar.

## Initializarea jocului 2048

Acest fisier se ocupa de initializarea logica a jocului 2048, avand rolul de a pregati tabla de joc inainte ca utilizatorul sa inceapa efectiv sa joace.

Principalele responsabilitati ale acestui fisier sunt:

- definirea unei constante pentru obstacole, reprezentate prin valoarea `-1`, care blocheaza miscarea si combinarea numerelor;
- crearea tablei de joc prin functia `create_empty_board`, care genereaza o tabla patrata de dimensiune aleasa, initializata complet cu valoarea `0`, corespunzatoare celulelor libere;
- verificarea corectitudinii tablei folosind functia `is_board_valid`, care asigura existenta tablei, forma patrata si utilizarea exclusiva a valorilor permise;
- adaugarea numerelor initiale pe tabla prin functia `add_nr_random`, care plaseaza in mod aleator valori de `2` sau `4` in celule libere, respectand regulile clasice ale jocului;
- initializarea completa a jocului prin functia `init_game`, care adauga doua valori initiale, insereaza obstacolele daca modul este activ, initializeaza scorul si stabileste starea initiala a jocului;
- returnarea tuturor valorilor necesare pentru pornirea jocului, astfel incat celelalte componente ale aplicatiei sa poata continua executia in mod corect.

---

## Logica mutarilor si regulile jocului 2048

Acest fisier contine logica centrala a jocului 2048, fiind responsabil de modul in care tabla de joc se modifica in urma actiunilor utilizatorului. Aici sunt implementate regulile de miscare, combinare a valorilor si conditiile de continuare sau terminare a jocului.

Functionalitatile principale implementate in acest fisier sunt:

- definirea obstacolelor prin valoarea `-1`, care impart tabla in segmente independente procesate separat;
- utilizarea functiei `copy_board` pentru crearea unei copii complete a tablei, evitand modificarea directa a starii originale si permitand verificarea mutarilor valide;
- implementarea functiei `compress`, care elimina valorile zero si apropie valorile diferite de zero in directia mutarii;
- implementarea functiei `merge`, care combina valorile egale aflate una langa alta, dubland valoarea obtinuta si calculand scorul corespunzator;
- reunirea acestor operatii in functia `process_segment`, care proceseaza corect fiecare segment delimitat de obstacole;
- implementarea mutarilor prin patru functii distincte: `move_left`, `move_right`, `move_up` si `move_down`, fiecare adaptata directiei corespunzatoare;
- utilizarea functiei `move_board` ca interfata generala pentru aplicarea unei mutari si verificarea modificarii tablei;
- verificarea posibilitatii de continuare a jocului prin functia `any_moves_possible`, care analizeaza existenta celulelor libere sau a combinarilor posibile.

---

## Sistem de dificultati si moduri de joc

Pentru a oferi o experienta de joc variata, aplicatia include mai multe niveluri de dificultate si moduri speciale de joc. Acestea influenteaza atat dinamica jocului, cat si strategiile necesare pentru a ajunge la valoarea 2048.
Elementele principale ale sistemului de dificultate sunt:

- dificultatea obstacolelor, care controleaza numarul de obstacole plasate pe tabla in functie de dimensiunea acesteia si de nivelul ales;
- modul cu mutari limitate, in care jucatorul are la dispozitie un numar fix de mutari pentru a atinge obiectivul;
- functia `get_obstacle_count`, care calculeaza automat numarul de obstacole in functie de dimensiunea tablei si dificultatea selectata;
- functia `get_moves_by_difficulty`, care stabileste numarul maxim de mutari permise pentru fiecare nivel de dificultate;
- adaptarea automata a dificultatii pentru a mentine un echilibru

---
 ## Dificultăți întâmpinate și soluții aplicate
- separarea clara intre logica si grafica
initial, anumite functii combinau operatii de desenare cu reguli de joc, ceea ce facea codul greu de intretinut. Problema a fost rezolvata prin separarea completa a logicii jocului (mutari, validari, dificultati) de partea grafica, astfel incat fiecare modul sa aiba o responsabilitate clara.
- echilibrarea nivelurilor de dificultate
echilibrarea dificultatii jocului, in special in modul cu obstacole, a reprezentat o provocare. Numărul de obstacole trebuia adaptat atât la dimensiunea tablei, cât și la nivelul de dificultate ales. Această problemă a fost rezolvată prin implementarea unei funcții dedicate care calculează automat numărul de obstacole în funcție de acești parametri.
- implementarea obstacolelor in logica clasica 2048
dificultatea a fost rezolvata prin impartirea randurilor si coloanelor in segmente delimitate de obstacole, fiecare segment fiind procesat independent.
De asemenea, **echilibrarea dificultății jocului**, în special în modul cu obstacole, a reprezentat o provocare. Numărul de obstacole trebuia adaptat atât la dimensiunea tablei, cât și la nivelul de dificultate ales. Această problemă a fost rezolvată prin implementarea unei funcții dedicate care calculează automat numărul de obstacole în funcție de acești parametri.

##  Contributie proiect - Diana Draica

In acest proiect am contribuit prin:

## Grafica pentru salvarea jocului, undo/redo

Unul dintre primele lucruri realizate in acest fisier este alegerea modului de joc. Atunci cand jocul porneste, jucatorul este intrebat daca doreste sa joace in modul normal sau in modul cu timp. Acest lucru se face printr-un ecran cu textul centrat, in care utilizatorul apasa o tasta pentru a face alegerea. Daca apasa T, jocul va avea timp limitat. Daca apasa N sau ENTER, jocul va fi fara timp. Functia nu porneste cronometrul, ci doar memoreaza ce tip de joc a fost ales.

Dupa ce jocul incepe, se afiseaza in partea de sus un HUD. HUD este zona unde apar scorul curent, cel mai bun scor si, daca este cazul, numarul de mutari ramase. Sub acest HUD este desenat un panou suplimentar care contine butoanele UNDO si REDO, precum si timpul ramas, daca jocul este in modul cu timp.

Codul calculeaza centrul zonei HUD si foloseste acest centru pentru a aseza casutele UNDO si REDO, astfel incat ele sa fie aliniate.

Afisarea timpului este realizata doar daca jocul este in modul cu timp. Timpul este afisat intr-o casuta separata, sub UNDO si REDO, iar culoarea acesteia se schimba in functie de cat timp mai ramane. Cand timpul este mai mare de 10 secunde, casuta este gri. Cand timpul scade sub 10 secunde, casuta devine rosie.

Cronometrul in sine functioneaza pe baza timpului intern al Pygame. La pornirea jocului se memoreaza momentul de start, iar la fiecare frame se calculeaza cat timp a trecut de atunci. Diferenta dintre timpul total permis si timpul trecut reprezinta timpul ramas.

La fiecare desenare a ecranului, toate elementele sunt afisate din nou, iar la final se face un update complet al ferestrei, astfel incat jucatorul sa vada orice schimbare.

---
## Modul de salvare

Fisierul de salvare si incarcare este cel care permite jocului sa fie inchis si redeschis fara pierderea progresului.

Atunci cand jocul este salvat, toate informatiile importante sunt puse intr-un dictionar. Acest dictionar contine tabla de joc, scorul curent, cel mai bun scor, numarul de mutari ramase, informatia despre modul cu timp, timpul ramas, obstacolele si stivele de undo si redo. Acest dictionar este scris intr-un fisier JSON.

La pornirea jocului, se verifica daca acest fisier de salvare exista. Daca nu exista, jocul porneste normal. Daca exista, utilizatorul este intrebat daca doreste sa continue jocul anterior sau sa inceapa unul nou. Aceasta intrebare este afisata intr-un ecran simplu, iar utilizatorul raspunde prin apasarea tastelor Y sau N (yes sau no).

Daca utilizatorul alege sa continue, jocul citeste fisierul JSON si restaureaza toate valorile salvate. Tabla de joc este refacuta exact asa cum era, scorurile sunt restaurate, iar starile interne, precum win screen sau undo si redo, sunt repuse in memorie.

In cazul modului cu timp, la continuarea jocului cronometrul este repornit de la momentul reluarii.

Daca utilizatorul alege sa nu continue jocul, fisierul de salvare este sters, iar jocul porneste de la zero, ca un joc nou.
   
## Dificultăți întâmpinate și soluții aplicate

O dificultate a fost alinierea corecta a elementelor din HUD. Butoanele UNDO si REDO, scorurile si afisarea timpului trebuiau pozitionate coerent si centrate, indiferent de dimensiunea ferestrei. Acest lucru a necesitat calcule suplimentare pentru pozitionare si testare vizuala pentru a evita suprapunerile sau spatiile neuniforme.

Implementarea sistemului de undo si redo a fost, de asemenea, o provocare. A fost important ca fiecare mutare valida sa salveze corect starea tablei si scorul, fara a afecta performanta jocului. De asemenea, a fost necesara golirea stivei de redo atunci cand se face o mutare noua, pentru a pastra un comportament corect si intuitiv.

Salvarea si incarcarea jocului a ridicat dificultati legate de consistenta datelor. Toate starile importante ale jocului, inclusiv tabla, scorurile, mutarile ramase, modul de joc si stivele de undo si redo, au trebuit salvate si restaurate exact asa cum erau. Orice informatie omisa ar fi dus la un comportament incorect dupa reincarcare.

##  Contributie proiect - Bianca
In cadrul acestui proiect m-am ocupat de realizarea unei părți semnificative a interfeței grafice și a sistemelor de configurare ale jocului. Responsabilitatile mele au fost:

- dezvoltarea interfeței grafice a jocului;
- afișarea tablei de joc și a elementelor vizuale aferente;
- afisarea ecranelor de start, logo și reguli;
- implementare meniurilor interactive pentru configurarea modurilor de joc;
- implementarea modului de joc cu obstacole din punct de vedere al interfeței și configurării;
- implementarea modului de joc cu mutări limitate din punct de vedere al interfeței și configurării;
- implementarea sistemului de selectare a dificultății pentru fiecare mod de joc.

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

---

- `show_start_screen(screen)`

Această funcție afișează ecranul de start al jocului, care conține titlul, regulile jocului și opțiunile pentru alegerea dimensiunii tablei.  
Interacțiunea se face prin tastatură, iar funcția returnează dimensiunea tablei selectate de utilizator.

- `show_logo_screen(screen)`

Funcția afișează un ecran de tip splash la pornirea aplicației.  
Aceasta încarcă și afișează o imagine reprezentativă pentru joc și așteaptă o acțiune din partea utilizatorului (tastă sau click) pentru a continua.

Fisierul `obstacole_options.py` contine urmatoarele functii:
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

O dificultate suplimentară a fost **afișarea overlay-urilor pentru stările de Game Over și Win**, fără a afecta vizibilitatea tablei de joc. Inițial, overlay-urile acopereau complet elementele grafice. Am rezolvat această problemă prin utilizarea suprafețelor `pygame.Surface` și setarea transparenței acestora cu metoda `set_alpha`.

