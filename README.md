# Χωροθέτηση Αεροδρομίων - Τεχνική Νοημοσύνη ΙΙ

Αυτό το project υλοποιεί αλγορίθμους βελτιστοποίησης για την εύρεση βέλτιστων θέσεων αεροδρομίων με βάση τις τοποθεσίες και τον πληθυσμό των πόλεων.

## 👥 Ομάδα Εργασίας
* Μιχάλης: Μαθηματική Μοντελοποίηση & Στάδια Α, Β
* Αγγελική/Θοδωρής: Μεταευρετικοί Αλγόριθμοι (PSO)
* Αγγελική/Θοδωρής: Εναλλακτική Βελτιστοποίηση & Σύγκριση
* Γιώργος: Παραγωγή Δεδομένων & Οπτικοποίηση

========================================================================
AIRPORT LOCATION OPTIMIZATION - SETUP & RUN GUIDE (WINDOWS)
========================================================================

--- Prerequisites ---
* Python 3.x (προσθήκη στο System PATH)
* Pip

--- Installation ---
Εκτελέστε στο root directory του project:
> pip install -r requirements.txt

--- Execution ---
Run συγκριτικό benchmark αλγορίθμων (PSO vs Genetic) με real-time visualization:
> python src/main_D_comparison.py

--- Project Entry Points ---
* src/main_A.py             : Στάδιο Α (1 Αεροδρόμιο - Unweighted)
* src/main_B.py             : Στάδιο Β (1 Αεροδρόμιο - Weighted με p_i)
* src/main_C.py             : Στάδιο Γ (Δίκτυο 2 Αεροδρομίων - Genetic)
* src/main_D_PSO.py         : Στάδιο Δ (Global Best PSO Simulation)
* src/main_D_Genetic.py     : Στάδιο Δ (Genetic Algorithm Simulation)
* src/main_D_comparison.py  : Στάδιο Δ (Benchmark: Runtime & Convergence Curves)

========================================================================
