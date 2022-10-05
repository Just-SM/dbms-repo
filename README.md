# DBMS

Simple dbms based on the python qt. At the time of creation it wasn't supposed to be a published or showed, thus it contains 0 supplement information about the code itself.


# Short guide to Doccano
> [Polska wersja](#przygotowanie-doccano)


##  Setting up the Doccano

### Initialization of Doccano 

==Taken from  [off. site](https://doccano.github.io/doccano/install_and_upgrade_doccano/#install-with-pip)==
After you install doccano, start the server with the following command:
```bash
# Initialize database. First time only.
doccano init
# Create a super user. First time only.
doccano createuser --username admin --password pass
# Start a web server.
doccano webserver --port 8000
```
In another terminal, run the following command:
```bash
# Start the task queue to handle file upload/download.
doccano task
```
Open  [http://localhost:8000/](http://localhost:8000/).

### Creation of the project 

- On the front page click `Create`.

- Select `Sequence Labeling`.

- A bit below, give `project name` and `description` for the project.

- On the bottom click `Create`.

### Load documents 

- On the left panel of the project page select `Dataset`.
- Go `Actions` -> `Import Dataset`.
- Select  `File format` as  `JSONL`.
- Click on `Drop files here...` and select prepared dataset in `.jsonl` format. (It can be file received from SoftMatcher as the result).
- Click `Import`.

### Load labels
- On the left panel of the project page select `Labels`.
- Go `Actions` -> `Import Labels`.
- Click on `file input` and select prepared labels in `.json` format.

### Adding Annotators  
-  Go to http://127.0.0.1:8000/admin/auth/user/
- Login as the admin (credentials same as used here `doccano createuser --username admin --password pass` , so `admin  pass` for example ).
- On the right side there is a button `Create user`.
- Create login and password for user  -> Click `Save`.
- Now You can close page, and login to  http://127.0.0.1:8000/ as the admin (credentials same as used here `doccano createuser --username admin --password pass` , so `admin  pass` for example ).
- Choose the project You want to add this user to.
- Go to `Members` on Left bar.
- `Add` -> in `User Search Api` choose the login of the new created user pick role as `Annotator`.

### Annotating of the Document 
-  Go to http://127.0.0.1:8000/
-  Click `Login` .
- Use Your given credentials to Login.
- Pick the project You would like to annotate.
- On left bar select `Start Annotation`.
- To Annotate a text just select text (as usual selection of text in Word), and select the label form the dropdown list.
- To Remove Annotation just right click on it.
- After You finish with the document click on cross ( it is exactly on the right from `Start Annotation` button).
- To go to the next document click on right arrow( it is on the same level as the cross, but from left side of screen).
- After finish You can just close the page.


## Przygotowanie Doccano

### Inicjalizacja Doccano

==Pochodzą z [off. site](https://doccano.github.io/doccano/install_and_upgrade_doccano/#install-with-pip)==
Po zainstalowaniu doccano uruchom serwer za pomocą następującego polecenia:

```bash
# Zainicjuj bazę danych. Tylko pierwszy raz.
doccano init
# Utwórz superużytkownika. Tylko pierwszy raz.
doccano createuser --username admin --password pass
#   Uruchom serwer
doccano webserver --port 8000
```
W innym terminalu uruchom następujące polecenie:
```bash
# Start the task queue to handle file upload/download.
doccano task
```
Otwórz [http://localhost:8000/](http://localhost:8000/).

### Stworzenie projektu

-   Na pierwszej stronie kliknij `Create`.

-   Wybierz `Sequence Labeling`.

-   Nieco poniżej podaj `project name` i `description` projektu

-   Na dole kliknij `Create`.

### Załaduj dokumenty

- W lewym panelu strony projektu wybierz `Dataset`.
- Kliknij `Actions` -> `Import Dataset`.
- Wybierz `File format` as  `JSONL`.
- Kliknij  `Drop files here...`i wybierz przygotowany zestaw danych w formacie `.jsonl`. (Może to być plik otrzymany z SoftMatcher jako wynik).
- Kliknij  `Import`.
- 
### Dodawanie adnotatorów
-  Otwórz  http://127.0.0.1:8000/admin/auth/user/
- Zaloguj się jako administrator (poświadczenia takie same jak tutaj `doccano createuser --username admin --password pass` , więc na przykład `admin pass` ).
- Po prawej stronie znajduje się przycisk `Create user`.
- Utwórz login i hasło dla użytkownika -> Kliknij  `Save`.
- Teraz możesz zamknąć stronę i zalogować się do  http://127.0.0.1:8000/ się jako administrator (poświadczenia takie same jak tutaj `doccano createuser --username admin --password pass` , więc na przykład `admin pass` ).
- Wybierz projekt, do którego chcesz dodać tego użytkownika.
- Przejdź do `Members` na lewym panelu strony.
- `Add` -> w `User Search Api` wybierz login nowo utworzonego użytkownika wybierz rolę jako `Annotator`.

### Adnotacja dokumentu
- Otwórz   http://127.0.0.1:8000/
-  Kliknij  `Login` .
- Użyj podanych danych logowania, aby się zalogować.
- Wybierz projekt, który chcesz annotować.
- Na lewym panelu strony wybierz `Start Annotation`.
- Aby dodać adnotację do tekstu, po prostu zaznacz tekst (jak zwykle zaznaczenie tekstu w programie Word) i wybierz etykietę z listy rozwijanej.
- Aby usunąć adnotację, kliknij ją prawym przyciskiem myszy.
-   Po zakończeniu pracy z dokumentem kliknij krzyżyk (jest dokładnie po prawej stronie przycisku `Start Annotation`).
- Aby przejść do następnego dokumentu kliknij strzałkę w prawo (jest na tym samym poziomie co krzyżyk, ale od lewej strony ekranu).
- Po zakończeniu możesz po prostu zamknąć stronę.
