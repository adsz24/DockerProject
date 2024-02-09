Temat projektu: Aplikacja do przegl¹dania katalogu dostêpnych produktów sportowych
 
Autorzy projektu:
Adam Szymczyk 39963
Janusz Kowalski 39954
Dawid P³u¿yñski 39958
 
## Requirements
- Python 3.11.5
- Django 3.2.5
- MySQL 8.0.36
 
## Baza danych
 
Aby odpaliæ projekt bêdzie potrzebna baza danych Mysqsl.
 
## Uruchomienie projektu
 
1. Sklonuj to repozytorium do swojego lokalnego œrodowiska:
 
    ```
    git clone https://github.com/adsz24/DockerProject.git
    ```
 
2. Upewnij siê, ¿e masz uruchomiony terminal i upewnij siê, ¿e jesteœ w katalogu projektu, jeœli nie wpisz polecenie
 
    ```
    cd dockerprojekt
    ```
 
3. W terminalu nale¿y wpisaæ polecenie
 
    ```
    python manage.py makemigrations
    ```
 
4. Nastêpnie wpisz polecenie
 
    ```
    python manage.py migrate
    ```
 
5. Zbuduj obrazy w docker za pomoc¹
 
    ```
    docker-compose build
    ```
 
6.  Uruchom kontenery za pomoc¹
 
    ```
    docker-compose up
    ```
 
7.  Wyœwietli siê informacja ,¿e kontener zosta³ zatrzymany. Anuluj akcjê 

    ```
    Ctrl+C
    ```

    Aby umo¿liwiæ mu dalszy ci¹g dzia³ania w pliku settings.py w databases nalezy zmieniæ host z '127.0.0.1' na 'mysql'i zapisaæ zmiany
   
    ```
    Ctrl+s
    ```
 
8. Uruchom kontenery z terminalu ponownie za pomoc¹
   
    ```
    docker-compose up
    ```
 
9. Po zakoñczeniu budowania kontenerów i uruchomieniu aplikacji, otwórz przegl¹darkê internetow¹ i przejdŸ pod adres:
 
    ```
    http://localhost:8000
    ```
 
10. Jeœli chcesz dodaæ produkty przejdŸ do strony administratora
 
    ```
    http://localhost:8000/admin
    ```

11. PrzejdŸ na te adresy, przegl¹daj katalog produktów lub jeœli chcesz skorzystaj z wyszukiwarki produktów
 
    ```
    http://localhost:8000/produkty
    ```
    http://localhost:8000/szukaj
    ```