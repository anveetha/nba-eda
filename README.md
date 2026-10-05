# NBA Exploratory Data Analysis (EDA)

This project performs exploratory data analysis (EDA) on NBA player and team statistics to uncover patterns, distributions, and correlations across various performance metrics.

---

## What It Does

The repository contains analysis scripts and a Jupyter Notebook designed to:

* **Load and Inspect Data:** Ingests NBA datasets containing player statistics, game logs, or season totals.
* **Data Cleaning & Preprocessing:** Handles missing entries, normalizes data types, and filters relevant statistical categories (e.g., points, rebounds, assists, shooting percentages, usage rates).
* **Statistical Analysis:** Calculates summary metrics, distribution parameters, and correlations between different performance dimensions.
* **Visualization:** Generates exploratory plots (scatter plots, histograms, correlation heatmaps, or box plots) to identify trends, performance tiers, and outliers among NBA players.

---

## Project Structure

```text
nba-eda/
├── eda.ipynb      # Interactive Jupyter notebook for step-by-step EDA and plots
├── eda.py         # Modular script containing EDA utility functions or routines
└── nba_eda.py     # Main Python executable script for running the NBA analysis

```

(Directory structure based on package contents)

---

## Prerequisites

Ensure you have Python 3.8+ installed on your system.

Common libraries used for this type of analysis include:

* `pandas`
* `numpy`
* `matplotlib`
* `seaborn`
* `jupyter` / `notebook`

Install them via `pip`:

```bash
pip install pandas numpy matplotlib seaborn jupyter

```

---

## Step-by-Step Guide: How to Run

### Option 1: Running via Terminal (Python Scripts)

1. **Navigate to the project directory:**
```bash
cd nba-eda

```


2. **Execute the NBA EDA script:**
```bash
python nba_eda.py

```


(Alternatively, run `python eda.py` if running the base EDA pipeline).


3. **Check the outputs:**
* Script outputs (summary statistics, logs) will appear in the standard console output.
* Any generated charts will either display in pop-up windows or be saved to the current working directory.



---

### Option 2: Running via Jupyter Notebook (Interactive)

1. **Navigate to the project directory and launch Jupyter Notebook:**
```bash
cd nba-eda
jupyter notebook

```


2. **Open the notebook:**
* In your browser interface, locate and click on `eda.ipynb`.




3. **Run the cells:**
* Click **Cell > Run All** from the top menu, or step through individual cells sequentially using `Shift + Enter` to view intermediate data tables and inline plots.
