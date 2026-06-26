# Χωροθέτηση Αεροδρομίων - Τεχνική Νοημοσύνη ΙΙ

Αυτό το project υλοποιεί αλγορίθμους βελτιστοποίησης για την εύρεση βέλτιστων θέσεων αεροδρομίων με βάση τις τοποθεσίες και τον πληθυσμό των πόλεων.

## 👥 Ομάδα Εργασίας
* Μιχάλης: Μαθηματική Μοντελοποίηση & Στάδια Α, Β
* Αγγελική/Θοδωρής: Μεταευρετικοί Αλγόριθμοι (PSO, Genetic) & Σύγκριση
* Γιώργος: Οπτικοποίηση, GitHub, Βελτιστοποίηση & Παραγωγή Δεδομένων 


CROSS-PLATFORM DOCKER INSTRUCTIONS (WINDOWS / LINUX / MACOS)


Η διαδικασία χωρίζεται σε δύο βήματα: το χτίσιμο της εικόνας (κοινό για όλους)
και την εκτέλεση του container (ανάλογα με το λειτουργικό σας σύστημα, 
λόγω του GUI forwarding της Matplotlib).


ΒΗΜΑ 1: Universal Image Build (Κοινό για όλα τα λειτουργικά)

Ανοίξτε το τερματικό στο root directory του project και εκτελέστε:

> docker build -t airport-optimization .


ΒΗΜΑ 2: Container Run (Επιλέξτε ανάλογα με το λειτουργικό σας)


● Για περιβάλλον LINUX:
  1. Δώστε δικαιώματα πρόσβασης στον X11 Server:
     > xhost +local:root
  2. Τρέξτε το container:
     > docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix airport-optimization

● Για περιβάλλον WINDOWS:
  * Αν χρησιμοποιείτε WSL2 (με ενεργό το WSLg), η εκτέλεση γίνεται απευθείας:
    > docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix airport-optimization
  * Αν χρησιμοποιείτε απλό Command Prompt/PowerShell, βεβαιωθείτε ότι τρέχει ένας 
    X-Server (π.χ. VcXsrv / Xming) στα Windows και εκτελέστε:
    > docker run -it --rm -e DISPLAY=host.docker.internal:0 airport-optimization

● Για περιβάλλον MACOS:
  1. Βεβαιωθείτε ότι είναι εγκατεστημένο και ανοιχτό το XQuartz (με ενεργοποιημένη 
     την επιλογή "Allow connections from clients").
  2. Επιτρέψτε τη σύνδεση:
     > xhost + 127.0.0.1
  3. Τρέξτε το container:
     > docker run -it --rm -e DISPLAY=host.docker.internal:0 airport-optimization


  Χωρίς DOCKER (WINDOWS)
  
  --- Prerequisites ---
  
      Python 3.x (προσθήκη στο System PATH)
      Pip
  
  --- Installation --- Εκτελέστε στο root directory του project:
  
      pip install -r requirements.txt
  
  --- Execution --- Run συγκριτικό benchmark αλγορίθμων (PSO vs Genetic) με real-time visualization:
  
      python src/main_D_comparison.py
  
  --- Project Entry Points ---
  
      src/main_A.py : Στάδιο Α (1 Αεροδρόμιο - Unweighted)
      src/main_B.py : Στάδιο Β (1 Αεροδρόμιο - Weighted με p_i)
      src/main_C.py : Στάδιο Γ (Δίκτυο 2 Αεροδρομίων - Genetic)
      src/main_D_PSO.py : Στάδιο Δ (Global Best PSO Simulation)
      src/main_D_Genetic.py : Στάδιο Δ (Genetic Algorithm Simulation)
      src/main_D_comparison.py : Στάδιο Δ (Benchmark: Runtime & Convergence Curves)
