## Instrukcje uruchamiania programów PoCs

[1. Przewodnik standardowy](#przewodnik-standardowy)
[2. Przewodnik Docker (Linux Host)](#przewodnik-docker-linux-host)
[3. Przewodnik Docker (Windows Host)](#przewodnik-docker-windows-host)

### Przewodnik standardowy

Wymaga zainstalowanego GITa oraz Python3.

##### Krok 1: Pobierz kod źródłowy

Sklonuj repozytorium i przejdź do katalogu głównego

```bash
git clone https://github.com/Bembnias/AmbientGuide.git
cd AmbientGuide
```

##### Krok 2: Wybierz branch PoC

Przełącz się na branch `PoC` zawierający aktualne Proof of Concepts.

```bash
git checkout PoC
```

##### Krok 3: Utwórz środowisko wirtualne

Utwórz środowisko wirtualne w celu izolacji projektu.

```bash
python3 -m venv agpoc
source venv/bin/activate  # Na systemach Linux/MacOS
venv\Scripts\activate  # Na systemach Windows
```

##### Krok 4: Wybór PoC

Przejdź do katalogu z wybranym PoC, np.: "DistanceMeasurement_2":

```bash
cd DistanceMeasurement_2
```

##### Krok 5: Instalacja pakietów

Zainstaluj wszystkie wymagane zależności używając `pip`:

```bash
pip install -r requirements.txt
```

##### Krok 6: Uruchom wybrany PoC

Po zainstalowaniu wszystkich zależności, możesz uruchomić wybrany Proof of Concept:

```bash
python main.py
```

### Przewodnik Docker (Linux Host)

Wymaga zainstalowanego GITa oraz Docker.

##### Krok 1: Pobierz kod źródłowy

Sklonuj repozytorium i przejdź do katalogu głównego

```bash
git clone https://github.com/Bembnias/AmbientGuide.git
cd AmbientGuide
```

##### Krok 2: Wybierz branch PoC

Przełącz się na branch `PoC` zawierający aktualne Proof of Concepts.

```bash
git checkout PoC
```

##### Krok 3: Wybór PoC

Przejdź do katalogu z wybranym PoC, np.: "DistanceMeasurement_2":

```bash
cd DistanceMeasurement_2
```

##### Krok 4: Znajdź prawidłową ścieżkę do kamery

Docker będzie wymagał przyznania uprawnień do korzystania z kamery twojego laptopa, lub podpiętej przez USB.
Urządzenia kamery mogą mieć różne ścieżki w zależności od tego, jak są rozpoznawane przez system. Aby sprawdzić dostępne urządzenia kamery, możesz użyć polecenia ls w terminalu:

```bash
ls /dev/video*
```

Jeśli system znajdzie jakąś kamerę to powinno się wyświetlić coś takiego: `/dev/video0`, lub `/dev/video1` w zależności od tego ile kamer zostało podpiętych.

##### Krok 5: Zbuduj obraz docker

Mając zainstalowanego dockera i będąc w wybranym katalogu PoC, wpisz:

```bash
docker build -t nazwa-poc .
```

##### Krok 6: Uruchom obraz docker

Po poprawnym zbudowaniu obrazu i znając ścieżkę do kamery, można uruchomić obraz (tu dla przykładu ścieżka do kamey to: `dev/video`).

```bash
docker run --device /dev/video0:/dev/video0 -it nazwa-poc
```

### Przewodnik Docker (Windows Host)

Jako że system Windows nie udostępnia ścieżki do kamery jak jest to w przypadku Linuxa to uruchomienie takiego jest problematyczne. Sposobem na obejście może być uruchomienie aplikacji w docker na zwirtualizowanej maszynie z Linux poprzez Virtual Box.

##### Krok 1: Instalacja VirtualBox

Przejdź na stronę twórców VirtualBox i pobierz, a następnie zainstaluj program.

[Link do strony VirtualBox](https://www.virtualbox.org/wiki/Downloads)

##### Krok 2: Zainstaluj Dodatki dla Gościa w VirtualBox

Aby zapewnić obsługę USB, upewnij się, że zainstalowałeś Dodatki dla Gościa (Guest Additions) na swojej maszynie wirtualnej z systemem Linux. Zazwyczaj instaluje się je z poziomu menu urządzenia VM w VirtualBox.

##### Krok 3: Skonfiguruj Przekazywanie USB w VirtualBox

1. Z zamkniętą maszyną wirtualną (VM nie może być uruchomiona podczas tej konfiguracji), otwórz ustawienia VM w VirtualBox.
2. Przejdź do sekcji „USB”.
3. Wybierz opcję, która pozwala na przekazywanie USB 2.0 lub USB 3.0, w zależności od tego, co obsługuje twoja kamera (USB 3.0 wymaga VirtualBox Extension Pack).
4. Kliknij ikonę z symbolem plusa (+) po prawej stronie, aby dodać nowe urządzenie USB do listy filtrów. Powinno to otworzyć okno z listą dostępnych urządzeń USB. Wybierz swoją kamerę z listy.
5. Zatwierdź zmiany i zamknij ustawienia VM.

##### Krok 4: Uruchom VM z Linux

Uruchom maszynę wirtualną z zainstalowanym systemem Linux, a następnie postępuj zgodnie z przewodnikiem: [Przewodnik Docker (Linux Host)](#przewodnik-docker-linux-host).
