# Engeto-Project-3

Třetí projekt do Engeto Online Python Akademie – Elections Scraper

## Popis
Skript [`main.py`](main.py) slouží ke stažení a zpracování volebních dat z webu volby.cz. Výsledky jsou uloženy do CSV souboru, kde každý řádek odpovídá jedné obci a obsahuje počty hlasů pro jednotlivé strany.

## Použití

1. Aktivujte virtuální prostředí (volitelné):
   ```sh
   .\moje-virt-prostredi\Scripts\activate
   ```

2. Nainstalujte potřebné knihovny:
   ```sh
   pip install -r requirements.txt
   ```

3. Spusťte skript s parametry:
   ```sh
   python main.py --url "URL_SEZNAMU_OBCÍ" --output_file "vystup.csv"
   ```

   - `--url` – URL stránky se seznamem obcí (např. https://www.volby.cz/pls/ps2017nss/obce?xjazyk=CZ&xkraj=11&xnumnuts=6205)
   - `--output_file` – název výstupního CSV souboru (musí končit na `.csv`)

## Příklad
```sh
python main.py --url "https://www.volby.cz/pls/ps2017nss/obce?xjazyk=CZ&xkraj=11&xnumnuts=6205" --output_file "prostejov.csv"
```

## Výstup
Výsledný CSV soubor bude obsahovat:
- Kód obce
- Název obce
- Počet registrovaných voličů
- Počet vydaných obálek
- Počet platných hlasů
- Počty hlasů pro jednotlivé strany

Výstupní soubor bude uložen ve stejné složce, kde spouštíte skript.

## Poznámky
- Skript je určen pro volby do Poslanecké sněmovny 2017 (ELECTION_PATH = "ps2017nss").