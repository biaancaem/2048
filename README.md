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

