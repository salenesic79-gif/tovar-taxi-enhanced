# Tovar Taxi - Proširena Logistička Aplikacija

Moderna Django aplikacija za upravljanje logističkim uslugama, podržana za naručioci i vozače.

## Instalacija

1. Kloniraj repozitorijum (ili copy-paste fajlove):
```bash
git clone https://github.com/salenesic79-gif/tovar-taxi-by-nesako.git  # Ili ručno kreiraj
cd tovar-taxi-by-nesako  # Ili tvoj folder
```

2. Kreiraj virtuelno okruženje:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Instaliraj zavisnosti:
```bash
pip install -r requirements.txt
```

4. Pokreni migracije:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Kreiraj superuser (opciono):
```bash
python manage.py createsuperuser
```

6. Pokreni server:
```bash
python manage.py runserver
```

Pristupite na http://127.0.0.1:8000/register/ za registraciju (izaberite ulogu).

## Funkcionalnosti

- ✅ Registracija i prijava sa ulogama (naručilac/vozač)
- ✅ Prošireni profil (telefon, adresa, premium status)
- ✅ Zatraživanje vožnje (naručioci) sa simulacijom uštede
- ✅ Prihvatanje i praćenje vožnji (vozači) sa ekstra zaradom i dopunjavanjem tura
- ✅ Dashboard sa flow praćenjem (status vožnje, zarada/ušteda)
- ✅ Moderni Bootstrap UI, responsive dizajn
- ✅ Srpski jezik, jednostavna upotreba

## Struktura Projekta
```
tovar_taxi/
├── transport/          # Glavna aplikacija
│   ├── models.py      # Profile i Ride modeli
│   ├── views.py       # Dashboard, request/accept ride
│   ├── forms.py       # Register i Ride forme
│   └── urls.py        # URL routing
├── templates/         # HTML templejti sa Bootstrap
├── static/           # CSS, JS
└── manage.py         # Django management
```

## Tehnologije

* Django 4.2+
* Bootstrap 5
* SQLite baza podataka
* Python 3.8+

## Napomene

- Za premium uslugu: Postavite `is_premium=True` u admin-u za prioritet.
- Skaliranje: Dodajte Google Maps API za realne rute i cene.
- Sigurnost: Promenite SECRET_KEY u produkciji.

© 2025 Tovar Taxi by NESAKO (Enhanced)
