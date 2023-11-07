# 1. und 2.: Datenbank erstellen und Skripte laufen lassen

# 3. Tabelle Fluglinie erstellen:
#drop table fluglinie;
use projektflughafen;

create table fluglinie(
	fluglinie_id 		int 			not null auto_increment,   
    iata	 			varchar(8)		not null unique,
    namen_fluglinie		varchar(18)		not null,
    flughafen_id		smallint		not null,
    
    primary key (fluglinie_id),
	foreign key (flughafen_id) references flughafen(flughafen_id) 
    );
    
# 4. Import Daten airline.csv:

select *
from fluglinie;

# 5. decribe airline --> stehen alles Infos drin über Type, Null, Key, Default, Extra

describe fluglinie;

# 6: Die Tabelle buchung_sample heißt schon buchung.....?? Code wäre: 
# alter table buchung_sample    
# rename table buchung_sample to buchung

# 7. Output Show tables --> bekomme alle Tabellen der database projekt-flughafen

show tables;

# 8. Neue Zeile in Passagiertabelle 
# neue Zeile mit Passagiernummer 36100

insert into passagier(passagier_id, passnummer, vorname, nachname)
values(null, "", "", "");

# 9. neue Spalte nationality

alter table passagier
add nationalität varchar(20);

# 10. Nationalität an Passagier Nr. 36100

update passagier                         
set nationalität = "Italien"
where passagier_id = 36100;

# 11. neue Spalte Nationalität aus Tabelle entfernen

alter table passagier
drop column nationalität;
