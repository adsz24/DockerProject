Temat projektu: Aplikacja do przegl�dania katalogu dost�pnych produkt�w sportowych
 
Autorzy projektu:
Adam Szymczyk 39963
Janusz Kowalski 39954
Dawid P�u�y�ski 39958
 
## Requirements
- Python 3.11.5
- Django 3.2.5
- MySQL 8.0.36
 
## Baza danych
 
Aby odpali� projekt b�dzie potrzebna baza danych Mysqsl.
 
## Uruchomienie projektu
 
1. Sklonuj to repozytorium do swojego lokalnego �rodowiska:
 
    ```
    git clone https://github.com/adsz24/DockerProject.git
    ```
 
2. Upewnij si�, �e masz uruchomiony terminal i upewnij si�, �e jeste� w katalogu projektu, je�li nie wpisz polecenie
 
    ```
    cd dockerprojekt
    ```
 
3. W terminalu nale�y wpisa� polecenie
 
    ```
    python manage.py makemigrations
    ```
 
4. Nast�pnie wpisz polecenie
 
    ```
    python manage.py migrate
    ```
 
5. Zbuduj obrazy w docker za pomoc�
 
    ```
    docker-compose build
    ```
 
6.  Uruchom kontenery za pomoc�
 
    ```
    docker-compose up
    ```
 
7.  Wy�wietli si� informacja ,�e kontener zosta� zatrzymany. Anuluj akcj� 

    ```
    Ctrl+C
    ```

    Aby umo�liwi� mu dalszy ci�g dzia�ania w pliku settings.py w databases nalezy zmieni� host z '127.0.0.1' na 'mysql'i zapisa� zmiany
   
    ```
    Ctrl+s
    ```
 
8. Uruchom kontenery z terminalu ponownie za pomoc�
   
    ```
    docker-compose up
    ```
 
9. Po zako�czeniu budowania kontener�w i uruchomieniu aplikacji, otw�rz przegl�dark� internetow� i przejd� pod adres:
 
    ```
    http://localhost:8000
    ```
 
10. Je�li chcesz doda� produkty przejd� do strony administratora
 
    ```
    http://localhost:8000/admin
    ```

11. Przejd� na te adresy, przegl�daj katalog produkt�w lub je�li chcesz skorzystaj z wyszukiwarki produkt�w
 
    ```
    http://localhost:8000/produkty
    ```
    http://localhost:8000/szukaj
    ```