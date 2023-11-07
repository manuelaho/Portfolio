# 1. Was ist der minimale, maximale und der durchschnittliche Preis für eine Buchung?

select
min(preis) as "minimaler Buchungspreis",
max(preis) as "maximaler Buchungspreis",
avg(preis) as "durchschnittlicher Buchungspreis"

from buchung;

# 2. Wie heißen die Reisenden mit der teuersten Buchung?

select
p.nachname,
p.vorname,
b.preis

from buchung b
inner join passagier p on b.passagier_id = p. passagier_id
where  b.preis = 
		(select max(preis) as "maximaler Buchungspreis" 
        from buchung);

# 3. Welche Fluglinie hat die durchschnittlich teuersten Tickets?

select
avg(sq1.preis) as "durchschnittlich teuerstes Ticket",
sq1.namen_fluglinie

from
	(select
    b.preis,
    fl.namen_fluglinie
	from
    fluglinie fl
	inner join flug f on fl.fluglinie_id = f.fluglinie_id
	inner join buchung b on f.flug_id = b.flug_id) as sq1

group by sq1.namen_fluglinie
order by avg(sq1.preis) desc
limit 1
;

# 4. Welche sind die fünf Flugzeuge mit der höchsten Kapazität, die vom Flughafen ALTAMIRA abgeflogen sind?
    
select
distinct fz.flugzeug_id,
fz.kapazitaet,
fh.name,
ft.bezeichnung

from flugzeug fz
inner join flug f on f.flugzeug_id = fz.flugzeug_id
inner join flughafen fh on fh.flughafen_id = f.von
inner join flugzeug_typ ft on ft.typ_id = fz.typ_id
where fh.name = "ALTAMIRA"

order by kapazitaet desc
limit 5
;

# 5. Wie viele Personen hat die Airline Spain Airlines vom 2015-06-06 bis zum 2015-06-08 transportiert?

select 
fl.namen_fluglinie,
count(distinct f.flug_id) "Anzahl Flüge Spain Airlines",
count(b.buchung_id) as "transportierte Personen"

from fluglinie fl
inner join flug f on fl.fluglinie_id = f.fluglinie_id 
inner join buchung b on f.flug_id = b.flug_id

where fl.namen_fluglinie = "Spain Airlines" and f.abflug between "2015-06-06 00:00:00" and  "2015-06-08 00:00:00"
;

# 6. Gebe für jeden Flug, die Flugnummer, die Kapazität des Flugzeuges und die Anzahl der Buchungen an. 
# Füge noch eine Spalte hinzu, die anzeigt, ob dieser Flug mehr als 50% ausgelastet war.

select
f.flug_id as "Flug",
f.flugnr as "Flugnummer",
fz.kapazitaet as "Kapazität",
sq.Anzahl_Buchungen,

CASE 
        WHEN sq.Anzahl_Buchungen >= (fz.kapazitaet / 2)
            THEN "mehr als 50 % ausgelastet"
        ELSE "weniger als 50 % ausgelastet"
    END as "Auslastung"

from flug f

inner join flugzeug fz on f.flugzeug_id = fz.flugzeug_id

inner join
		(select
        f.flug_id,
        count(b.buchung_id) as "Anzahl_Buchungen"
        from buchung b
        inner join flug f on f.flug_id = b.flug_id
        group by f.flug_id) as sq on sq.flug_id = f.flug_id

order by sq.Anzahl_Buchungen desc;

# 7. Welche Fluglinie fliegt am meisten zum Flughafen KAGOSHIMA?

select

fl.namen_fluglinie,
count(f.fluglinie_id) as "häufigste Fluglinien Richtung Kagoshima"

from flug f
inner join flughafen fh on fh.flughafen_id = f.nach
inner join fluglinie fl on f.fluglinie_id = fl.fluglinie_id
where fh.stadt = "KAGOSHIMA"

group by fl.namen_fluglinie;

# 8. Welche Flugzeuge einer Fluglinie mit einem italienischen Flughafen als Basis machen die meisten 
# Flüge und was für ein Typ sind sie?

select 
fl.namen_fluglinie as "Fluglinie",
count(fz.flugzeug_id) as "Anzahl_Flüge",
ft.bezeichnung "Typ Flugzeug"

from flughafen fh

inner join fluglinie fl on fl.flughafen_id = fh.flughafen_id
inner join flug f on f.fluglinie_id = fl.fluglinie_id
inner join flugzeug fz on fz.fluglinie_id = f.fluglinie_id
inner join flugzeug_typ ft on ft.typ_id = fz.typ_id

where fh.land = "Italy"
group by fl.namen_fluglinie, ft.bezeichnung 
order by Anzahl_Flüge desc
;

# 9. Wie groß sind die gesamten Anteile in Prozent aller Buchungen je nach Flugzeugtyp?

select 
ft.bezeichnung as "Flugzeugtyp",
(count(b.buchung_id) / (select count(buchung_id) from buchung)) * 100 as "Anteil_in_Prozent"

from buchung b

inner join flug f on f.flug_id = b.flug_id
inner join flugzeug fz on fz.flugzeug_id = f.flugzeug_id
inner join flugzeug_typ ft on ft.typ_id = fz.typ_id

group by ft.bezeichnung
order by Anteil_in_Prozent desc;