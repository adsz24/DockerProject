Temat projektu: Aplikacja do przeglądania katalogu dostępnych produktów sportowych

Autorzy projektu:
Adam Szymczyk 39963
Janusz Kowalski 39954
Dawid Płużyński 39958

## Requirements
- Python 3.11.5
- Django 3.2.5

## Baza danych

Aby odpalić projekt będzie potrzebna baza danych Mysqsl.

## Uruchomienie projektu

1. Sklonuj ten repozytorium do swojego lokalnego środowiska:

    ```
    git clone https://github.com/adsz24/DockerProject.git
    ```

2. Przejdź do katalogu projektu:

    ```
    cd dockerprojekt
    ```

3. W terminalu należy wpisać polecenie 

    ```
    python manage.py makemigrations
    ```

4. Następnie wpisz polecenie 

    ```
    python manage.py migrate
    ```

5.  Wywołaj w terminalu polecenie (po uruchomieniu tego polecenia będziesz musiał nadać swój login i hasło oraz mail dla konta admina)

    ```
    python manage.py createsuperuser
    ```

6. Jeśli chcesz możesz dodać produkty skyptem, aby to wykonać wpisz w terminalu polecenie. Będziesz mógł również dodać produkty później ,ale w inny sposób.

    ```
    python addproducts.py
    ```

7. Zbuduj obrazy w docker za pomocą

    ```
    docker-compose build 
    ```

8.  Uruchom kontenery za pomocą 

    ```
    docker-compose up
    ```

9.  Wyświetli się informacja ,że kontener został zatrzymany aby umożliwić mu dalszy ciąg działania w pliku settings.py w databases nalezy zmienić host z 127.0.0.1 na mysql
    
    ```
    ctrl+s
    ```

10. Uruchom kontenery ponownie za pomocą
    
    ```
    docker-compose up
    ```

11. Po zakończeniu budowania kontenerów i uruchomieniu aplikacji, otwórz przeglądarkę internetową i przejdź pod adres:

    ```
    http://localhost:8000
    ```

12. Jeśli chcesz dodać produkty przejdź do strony administratora 

    ```
    http://localhost:8000/admin
    ```

