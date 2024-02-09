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
 
1. Sklonuj ten repozytorium do swojego lokalnego �rodowiska:
 
    ```
    git clone https://github.com/adsz24/DockerProject.git
    ```
 
2. Przejd� do katalogu projektu:
 
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
 
5.  Wywo�aj w terminalu polecenie (po uruchomieniu tego polecenia b�dziesz musia� nada� sw�j login i has�o oraz mail dla konta admina)
 
    ```
    python manage.py createsuperuser
    ```
 
6. Je�li chcesz mo�esz doda� produkty skyptem, aby to wykona� wpisz w terminalu polecenie. B�dziesz m�g� r�wnie� doda� produkty p�niej ,ale w inny spos�b.
 
    ```
    python addproducts.py
    ```
 
7. Zbuduj obrazy w docker za pomoc�
 
    ```
    docker-compose build
    ```
 
8.  Uruchom kontenery za pomoc�
 
    ```
    docker-compose up
    ```
 
9.  Wy�wietli si� informacja ,�e kontener zosta� zatrzymany aby umo�liwi� mu dalszy ci�g dzia�ania w pliku settings.py w databases nalezy zmieni� host z 127.0.0.1 na mysql
   
    ```
    ctrl+s
    ```
 
10. Uruchom kontenery ponownie za pomoc�
   
    ```
    docker-compose up
    ```
 
11. Po zako�czeniu budowania kontener�w i uruchomieniu aplikacji, otw�rz przegl�dark� internetow� i przejd� pod adres:
 
    ```
    http://localhost:8000
    ```
 
12. Je�li chcesz doda� produkty przejd� do strony administratora
 
    ```
    http://localhost:8000/admin
    ```