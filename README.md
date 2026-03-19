# Interesting Algorithms 🧠

Sbírka zajímavých algoritmů implementovaných v Pythonu.

---

## 📁 Obsah repozitáře

### 🎮 1. Minimax s Alpha-Beta prořezáváním
AI agent navržený pro optimální hraní piškvorek (Tic-Tac-Toe).

* **Hlavní princip:** Algoritmus buduje rozhodovací strom všech možných budoucích tahů. Předpokládá, že oba hráči hrají dokonale: „Maximalizátor“ (+1) se snaží dosáhnout nejvyššího skóre, zatímco „Minimalizátor“ (-1) se snaží vynutit skóre co nejnižší.
* **Optimalizace:** Implementuje **Alpha-Beta prořezávání** (pruning), které přeskakuje prohledávání větví, jež nemohou ovlivnit konečné rozhodnutí, čímž výrazně zvyšuje výkon.
* **Soubor:** `minimax.py`

---

### 👑 2. Backtracking (Problém N dam)
Rekurzivní přístup k řešení hádanky rozmístění N dam na šachovnici.

* **Hlavní princip:** Algoritmus umisťuje dámy řádek po řádku. Pokud detekuje konflikt (dvě dámy se vzájemně ohrožují), vrátí se zpět (**backtrack**) do předchozího řádku a zkusí jiný sloupec.
* **Klíčová logika:** Používá kontrolu bezpečnosti, aby zajistil, že žádné dvě dámy nesdílejí stejný řádek, sloupec ani diagonálu.
* **Soubor:** `backtracking.py`

---

### 🎒 3. Genetický algoritmus (Problém batohu)
Heuristické vyhledávání inspirované Darwinovou teorií přirozené evoluce.

* **Hlavní princip:** Řeší optimalizační problém batohu evolucí populace kandidátních řešení pomocí selekce, křížení a mutace.
* **Evoluční proces:** * **Selekce:** Vybere nejúspěšnější jedince na základě fitness funkce (celková hodnota vs. kapacita).
    * **Křížení (Crossover):** Kombinuje „DNA“ dvou rodičů pro vytvoření potomka.
    * **Mutace:** Zavádí náhodné změny pro zachování genetické rozmanitosti a zabránění uvíznutí v lokálním optimu.
* **Soubor:** `genetic_algorithm.py`

---

## 🚀 Jak začít

### Požadavky
* Python 3.x
* NumPy (vyžadováno pro `minimax.py`)

### Spuštění skriptů
Každý algoritmus můžete spustit samostatně:
```bash
python minimax.py
python backtracking.py
python genetic_algorithm.py
