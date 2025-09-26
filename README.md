## Popis funkce a použití

Tento program slouží ke stažení volebních dat z uživatelem zvoleného územního celku (rok 2017). V tomto odkazu: https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ si uživatel vybere územní celek kliknutím na "X" ve sloupci "Vyběr obce" a zkopíruje URL/odkaz dané stránky. Například pro Olomoucký kraj - Prostějov to bude: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103. Ten použije jako argument pro --url, druhý argument pro --output_file bude název výstupního souboru např.: prostejov.csv (název musí končit koncovkou .csv).
Volební data budou uložena do souboru ve složce se staženým programem.

## Použití ve Visual Studio Code

1. **Otevřete složku projektu**  
    Spusťte Visual Studio Code a otevřete složku s tímto staženým projektem.

    - Windows:  
      - PowerShell:  
        ```
        python -m venv .venv
        .\.venv\Scripts\activate
        ```
      - CMD:  
        ```
        python -m venv .venv
        .\.venv\Scripts\Activate.bat
        ```
    - macOS/Linux:  
      ```
      python3 -m venv .venv
      source .venv/bin/activate
      ```
      > **Poznámka:** Některé systémy mohou používat příkaz `python` místo `python3`. Pokud příkaz nefunguje, ověřte instalaci Pythonu pomocí `python --version` nebo `python3 --version`.

3. **Nainstalujte závislosti/knihovny**  
    V terminálu spusťte:  
    ```
    pip install -r requirements.txt
    ```

4. **Spusťte skript**  
    V terminálu spusťte příkaz s požadovanými parametry, například:  
    ```
    python main.py --url "https://www.volby.cz/pls/ps2017nss/obce?xjazyk=CZ&xkraj=11&xnumnuts=6205" --output_file "prostejov.csv"
    ```
    - `--url` určuje adresu webové stránky, ze které se budou stahovat data.
    - `--output_file` nastavuje název výsledného CSV souboru, do kterého se data uloží.

5. **Zkontrolujte výstup**  
    Výsledný CSV soubor najdete ve složce projektu.