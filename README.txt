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
 
1. Sklonuj ten repozytorium do swojego lokalnego œrodowiska:
 
    ```
    git clone https://github.com/adsz24/DockerProject.git
    ```
 
2. PrzejdŸ do katalogu projektu:
 
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
 
5.  Wywo³aj w terminalu polecenie (po uruchomieniu tego polecenia bêdziesz musia³ nadaæ swój login i has³o oraz mail dla konta admina)
 
    ```
    python manage.py createsuperuser
    ```
 
6. Jeœli chcesz mo¿esz dodaæ produkty skyptem, aby to wykonaæ wpisz w terminalu polecenie. Bêdziesz móg³ równie¿ dodaæ produkty póŸniej ,ale w inny sposób.
 
    ```
    python addproducts.py
    ```
 
7. Zbuduj obrazy w docker za pomoc¹
 
    ```
    docker-compose build
    ```
 
8.  Uruchom kontenery za pomoc¹
 
    ```
    docker-compose up
    ```
 
9.  Wyœwietli siê informacja ,¿e kontener zosta³ zatrzymany aby umo¿liwiæ mu dalszy ci¹g dzia³ania w pliku settings.py w databases nalezy zmieniæ host z 127.0.0.1 na mysql
   
    ```
    ctrl+s
    ```
 
10. Uruchom kontenery ponownie za pomoc¹
   
    ```
    docker-compose up
    ```
 
11. Po zakoñczeniu budowania kontenerów i uruchomieniu aplikacji, otwórz przegl¹darkê internetow¹ i przejdŸ pod adres:
 
    ```
    http://localhost:8000
    ```
 
12. Jeœli chcesz dodaæ produkty przejdŸ do strony administratora
 
    ```
    http://localhost:8000/admin
    ```