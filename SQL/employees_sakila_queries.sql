#__________________________________________________________________________________________________________
# AUFGABEN EMPLOYEES DATENBANK:
#__________________________________________________________________________________________________________

# Frage 1: Was ist das durchschnittliche Gehalt für jedes Geschlecht in den unterschiedlichen Abteilungen?

select 
e.gender,
d.dept_name,
avg(salary) as 'Durchschnittliches Gehalt'

from salaries s

inner join employees e on s.emp_no = e.emp_no
inner join dept_emp d_e on d_e.emp_no = e.emp_no
inner join departments d on d.dept_no = d_e.dept_no

where d_e.to_date > curdate() and s.to_date > curdate()

group by e.gender,d.dept_name
;

# Antwort 1: Bitte durchlaufen lassen :-)

# Frage 2: Welche Abteilung verdient am besten?

select 
e.gender,
d.dept_name,
avg(salary) as 'Durchschnittliches Gehalt'

from salaries s

inner join employees e on s.emp_no = e.emp_no
inner join dept_emp d_e on d_e.emp_no = e.emp_no
inner join departments d on d.dept_no = d_e.dept_no

where d_e.to_date > curdate() and s.to_date > curdate()

group by e.gender,d.dept_name
order by avg(salary) desc
;

# Antwort 2: Die Abteilung "sales" verdient am Besten

# Frage 3: Wie viele Mitarbeiter arbeiten in den Abteilungen?

select 
e.gender,
d.dept_name,
avg(salary) as 'Durchschnittliches Gehalt',
count(distinct e.emp_no) as "Anzahl Mitarbeiter"

from salaries s

inner join employees e on s.emp_no = e.emp_no
inner join dept_emp d_e on d_e.emp_no = e.emp_no
inner join departments d on d.dept_no = d_e.dept_no

where d_e.to_date > curdate() and s.to_date > curdate()

group by e.gender,d.dept_name
order by avg(salary) desc
;

# Antwort 3: Bitte durchlaufen lassen :-)

# Frage 4: Welche und wie viele Abteilungs-Geschlecht-Kombinationen aus Aufgabe 3 haben mehr als 
# 10.000 Mitarbeiter.

select 
e.gender,
d.dept_name,
avg(salary) as 'Durchschnittliches Gehalt',
count(distinct e.emp_no) as "Anzahl Mitarbeiter"

from salaries s

inner join employees e on s.emp_no = e.emp_no
inner join dept_emp d_e on d_e.emp_no = e.emp_no
inner join departments d on d.dept_no = d_e.dept_no

where d_e.to_date > curdate() and s.to_date > curdate()

group by e.gender,d.dept_name
having count(distinct e.emp_no) > 10000
order by avg(salary) desc
;

# Antwort 4: Production und Development männlich

# Frage 5: Erstelle eine Tabelle mit allen Paaren von Mitarbeitern des gleichen Geschlechts, die vor 
# 1960 geboren sind. Benutze dabei keine WHERE-Bedingung und beachte die reflexive Relation, d.h.
# alle Reihen, wo ein Mitarbeiter mit sich selbst paart.

select
*
from employees e1

inner join employees e2  on e1.emp_no != e2.emp_no and
e1.gender = e2.gender and year(e1.birth_date) < 1960;

# Antwort 5: Bitte durchlaufen lassen :-)


#___________________________________________________________________________________________________________
# AUFGABEN SAKILA DATENBANK:
#___________________________________________________________________________________________________________

# Frage 1: Lass dir eine Tabelle ausgeben, die den Vor- und Nachnamen der Schauspielenden, die Anzahl an 
# Filmen, in denen sie mitgespielt haben und die durchschnittliche Länge des Filmes widerspiegelt.

select
a.first_name,
a.last_name,
count(f.film_id),
avg(f.length)

from actor a

inner join film_actor fa on a.actor_id = fa.actor_id
inner join film f on f.film_id = fa.film_id

group by a.actor_id;

# Antwort 1: Bitte durchlaufen lassen :-)


# Frage 2: Du möchtest die Genres category und den Umsatz rental_rate bewerten. Lass dir dazu eine Tabelle 
# ausgeben, die das Genre, die Anzahl an Titel, den durchschnittlichen Umsatz pro Titel und den 
# max. Umsatz pro Titel ausgibt.

select 
c.name as "Name",
count(c.category_id) as "Anzahl",
avg(f.rental_rate) as "Avg",
max(f.rental_rate) as "Max"

from film_category fc 

inner join category c on c.category_id = fc.category_id
inner join film f on f.film_id = fc.film_id

group by c.category_id;

# Antwort 2: Bitte durchlaufen lassen :-)

# Frage 3: Welche drei Genres haben den günstigsten Mietpreis?

select 
c.name as "Name",
min(f.rental_rate) as "Max"

from film_category fc 

inner join category c on c.category_id = fc.category_id
inner join film f on f.film_id = fc.film_id

group by c.name;

# Antwort 3: Bitte durchlaufen lassen :-)

# Frage 4: Finde alle Filme, die zur Kategorie Sci-Fi gehören und lass die restlichen Kategorien ohne Werte. 
# Hier soll wieder kein WHERE benutzt werden, sondern ein LEFT JOIN. 

select 
f.film_id,
f.title,
c.name

from film f

inner join film_category fc on fc.film_id = f.film_id

right join category c on fc.category_id = c.category_id and c.name = "Sci-Fi";

# Antwort 4: Bitte durchlaufen lassen :-)
