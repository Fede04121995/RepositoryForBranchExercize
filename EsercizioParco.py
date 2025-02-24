import numpy as np
import pandas as pd

# Impostazioni
np.random.seed(42) 
giorni = 365
media_visitatori = 2000
deviazione_standard = 500

# Generazione dei dati casuali
visitatori_casuali = np.random.normal(loc=media_visitatori, scale=deviazione_standard, size=giorni)

# Aggiunta di un trend crescente
trend = np.linspace(start=0, stop=1000, num=giorni)  # Aumento graduale fino a 1000 visitatori in più

# Serie temporale finale
visitatori_giornalieri = visitatori_casuali + trend




print("ciao", visitatori_giornalieri)