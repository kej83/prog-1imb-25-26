# SELECT-oppgaver

## Kopier denne koden i sqlliteonline eller pgadmin:
```sql
DROP TABLE IF EXISTS biler;
CREATE TABLE biler (
	id SERIAL PRIMARY KEY,
	merke TEXT,
	modell TEXT,
	pris NUMERIC(8, 2),
	km INT,
	aar INT
);

INSERT INTO biler (id, merke, modell, pris, km, aar) VALUES
(1,  'Toyota',    'Corolla',   179000.00,  82000, 2017),
(2,  'Volkswagen','Golf',      199000.00,  65000, 2018),
(3,  'Volvo',     'V60',       289000.00,  91000, 2016),
(4,  'BMW',       '320d',      319000.00,  74000, 2017),
(5,  'Audi',      'A4',        339000.00,  68000, 2018),
(6,  'Mercedes',  'C200',      349000.00,  60000, 2018),
(7,  'Skoda',     'Octavia',   189000.00,  88000, 2017),
(8,  'Ford',      'Focus',     169000.00,  95000, 2016),
(9,  'Hyundai',   'i30',       159000.00,  72000, 2018),
(10, 'Kia',       'Ceed',      164000.00,  69000, 2019),

(11, 'Nissan',    'Qashqai',   209000.00,  78000, 2017),
(12, 'Mazda',     'CX-5',      279000.00,  83000, 2016),
(13, 'Honda',     'Civic',     189000.00,  61000, 2018),
(14, 'Peugeot',   '308',       149000.00, 105000, 2016),
(15, 'Renault',   'Megane',    139000.00, 112000, 2015),
(16, 'Opel',      'Astra',     129000.00, 118000, 2015),
(17, 'Tesla',     'Model 3',   329000.00,  59000, 2019),
(18, 'Polestar',  '2',         369000.00,  42000, 2021),
(19, 'Volkswagen','Passat',    239000.00,  97000, 2017),
(20, 'Toyota',    'RAV4',      299000.00,  85000, 2018),

(21, 'Subaru',    'Outback',   259000.00,  93000, 2017),
(22, 'Mitsubishi','Outlander', 229000.00,  99000, 2016),
(23, 'Suzuki',    'Vitara',    179000.00,  77000, 2018),
(24, 'Fiat',      '500',       109000.00,  54000, 2017),
(25, 'Mini',      'Cooper',    199000.00,  62000, 2016),
(26, 'Citroen',   'C3',        119000.00,  68000, 2018),
(27, 'Seat',      'Leon',      159000.00,  73000, 2017),
(28, 'Dacia',     'Duster',    169000.00,  81000, 2019),
(29, 'Lexus',     'NX300h',    389000.00,  76000, 2018),
(30, 'Saab',      '9-3',        79000.00, 165000, 2011);

SELECT * FROM biler;
```
## Gjør oppgavene
Skriv riktig SQL-kode, f.eks. `SELECT * from biler;`. Bruk SQLliteonline dersom pgadmin ikke fungerer!

### 1–5: Enkelt (velg kolonner / `*`)

1. Vis **alle biler** (alle kolonner).
2. Vis bare **merke** og **modell** for alle biler.
3. Vis bare **id** og **pris** for alle biler.
4. Vis bare **merke**, **modell** og **år** for alle biler.
5. Vis bare **modell** og **km** for alle biler.

### 6–10: WHERE (enkle filtreringer)

6. Finn alle biler fra **2018**. (vis `*`)
7. Finn alle biler med **pris under 200000**. (vis `merke`, `modell`, `pris`)
8. Finn alle biler med **km over 100000**. (vis `*`)
9. Finn alle biler av merket **Toyota**. (vis `*`)
10. Finn alle biler fra **2016 eller eldre**. (vis `merke`, `modell`, `aar`)

### 11–15: WHERE med AND

11. Finn biler som er fra **2018** **OG** har **pris under 250000**. (vis `*`)
12. Finn biler som er **Toyota** **OG** har kjørt **under 90000 km**. (vis `merke`, `modell`, `km`)
13. Finn biler som har **pris mellom 150000 og 200000** (inkludert) **OG** er fra **2017 eller nyere**. (vis `*`)
14. Finn biler som er fra **2016** **OG** har **km under 90000**. (vis `merke`, `modell`, `km`, `aar`)
15. Finn biler som har **km over 70000** **OG** **pris over 300000**. (vis `*`)

### 16–20: AND + OR (kombinasjoner)

16. Finn biler som er **(Toyota ELLER Volkswagen)**. (vis `*`)
17. Finn biler som er fra **2018** **OG** (**Toyota ELLER Volkswagen**). (vis `merke`, `modell`, `aar`)
18. Finn biler som har **pris under 170000** **ELLER** **km over 110000**. (vis `*`)
19. Finn biler som er **fra 2017 eller nyere** **OG** (**pris under 200000 ELLER km under 70000**). (vis `merke`, `modell`, `pris`, `km`, `aar`)
20. Finn biler som er **(fra 2016 eller eldre OG km over 90000)** **ELLER** **(fra 2019 eller nyere OG pris under 250000)**. (vis `*`)


