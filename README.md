# Interesting Algorithms 🧠

A collection of classic algorithms implemented in Python.

---

## 📁 Repository Content

### 🎮 1. Minimax with Alpha-Beta Pruning
An AI agent designed to play Tic-Tac-Toe optimally.

* **Core Principle:** The algorithm builds a decision tree of all possible future moves. It assumes both players play perfectly: the "Maximizer" (+1) tries to achieve the highest score, while the "Minimizer" (-1) tries to force the lowest score.
* **Optimization:** Implements **Alpha-Beta Pruning** to skip searching branches that cannot possibly influence the final decision, significantly improving performance.
* **File:** `minimax.py`

---

### 👑 2. Backtracking (N-Queens Problem)
A recursive approach to solving the famous N-Queens puzzle on a chessboard.

* **Core Principle:** The algorithm places queens row by row. If it detects a conflict (two queens attacking each other), it "backtracks" to the previous row and tries a different column.
* **Key Logic:** Uses a safety check to ensure no two queens share the same row, column, or diagonal.
* **File:** `backtracking.py`

---

### 🎒 3. Genetic Algorithm (Knapsack Problem)
A heuristic search inspired by Charles Darwin’s theory of natural evolution.

* **Core Principle:** Solves the Knapsack optimization problem by evolving a population of candidate solutions through selection, crossover, and mutation.
* **Evolutionary Process:** * **Selection:** Picks the best-performing individuals based on a fitness function (total value vs. capacity).
    * **Crossover:** Combines "DNA" from two parents to create offspring.
    * **Mutation:** Introduces random changes to maintain genetic diversity and avoid local optima.
* **File:** `genetic_algorithm.py`

---

## 🚀 Getting Started

### Prerequisites
* Python 3.x
* NumPy (required for `minimax.py`)

### Running the Scripts
You can run each algorithm independently:
```bash
python minimax.py
python backtracking.py
python genetic_algorithm.py
