# Demo projekt za FOI tjedan karijera

## Upute

### Priprema
1. Instalirati Python: https://www.python.org/
2. Ažurirati pip  
   `pip install -U pip`
3. Pripremiti virtualno okruženje  
   `pip install virtualenv`  
   `virtualenv ENV`  
   `. /ENV/Scripts/activate` # za windowse  
   `. /ENV/bin/activate` # za linux  
   Detaljnije upute: https://virtualenv.pypa.io/en/latest/

### Postavljanje projekta
1. Dohvatiti kod sa https://github.com/Styria-Digital/foi-demo
2. Pozicionirati se u korijensku mapu projekta
3. Instalirati pakete iz requirements.txt datoteke:  
   `pip install -r requirements.txt`
4. Migrirati bazu  
   `python manage.py migrate`
5. Pokrenuti razvojni poslužitelj  
   `python manage.py runserver`  
   Aplikacija je dostupna na 127.0.0.1:8000

### stvaranje superusera za pristup admin dijelu aplikacije
   `python manage.py createsuperuser`
