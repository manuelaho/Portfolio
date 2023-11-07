# EINFACHE QUERIES
#----------------------------------------------------------------------------------------------------------

# 1. Gib die Namen aller Mitarbeitenden und deren Titel aus:

select
firstName,
lastName,
jobTitle

from employees;

# 2. Gib alle Produktinformationen für die Produktlinie Motorcycles aus:

select
*
from products
where productLine = "Motorcycles";

# 3. Wie viele Motorräder haben wir noch auf Lager?

select
sum(quantityInStock)
from products
where productLine = "Motorcycles";

# 4. Wie viel kostet das günstigste, das teuerste und wie viel ein durchschnittliches Motorrad?

select
min(productCode),
min(productName),
min(buyPrice) as "günstigstes Motorrad",
max(buyPrice) as "teuerstes Motorrad",
avg(buyPrice) as "Preis durchschnittliches Motorrad"

from products
where productLine = "Motorcycles";

# 5. Gibt es Bestellungen, die später versandt wurden als gefordert?

select
*
from orders
where requiredDate < shippedDate;

# 6. Was sind die 3 häufigsten Kommentare einer Bestellung?

select
comments,
count(comments) as "Anzahl Kommentare"

from orders
group by comments
having comments = comments
order by count(comments) desc;

# 7. Wie lange benötigen unsere Produkte durchschnittlich vom Eingang der Bestellung bis zur Auslieferung? 

select
avg(datediff(shippedDate, orderDate)) as "durchschnittliche Auslieferungszeitspanne"

from orders;

# KOMPLEXERE QUERIES
#----------------------------------------------------------------------------------------------------------

# 8. Welches Sales-Mitglied bringt am meisten Umsatz (pm.amount) rein?

select
e.employeeNumber,
e.lastName, 
e.firstName,
sum(pm.amount) as "Umsatz" 

from employees e

inner join customers c on e.employeeNumber = c.salesRepEmployeeNumber
inner join payments pm on pm.customerNumber = c.customerNumber

group by e.employeeNumber
order by sum(pm.amount) desc
limit 1;

# 9. Gibt es Produkte, die keiner bestellt hat?

select
p.productCode,
sum(od.quantityOrdered)

from orderdetails od

right join products p on od.productCode = p.productCode
where od.productCode  is null

group by p.productCode;

# 10. Liste alle unterschiedlichen Porsches, die Verkaufsmenge, den erwarteten Umsatz aus dem MSRP
# und den erzeugten Umsatz aus dem Verkaufspreis auf:

select 
p.productName,
sum(od.quantityOrdered) as "Bestellmenge",
sum((p.MSRP - p.buyPrice) * od.quantityOrdered) as "Erwarteter Umsatz",
sum((od.priceEach - p.buyPrice) * od.quantityOrdered) as "Erzeugter Umsatz"

from products p

inner join orderdetails od on od.productCode = p.productCode
where productName like "%Porsche%" and p.productName = p.productName
group by p.productName;

# AUFGABEN SUBQUERIES
#----------------------------------------------------------------------------------------------------------

# 11. Was ist der Umsatz pro Kunde in Total und in % vom Gesamtumsatz?

select
c.customerNumber,
sum(p.amount) as "Ausgaben_pro_customer_Number",
sum(p.amount) / (select sum(amount) from payments) as "Anteil Kunde an Gesamtumsatz"

from customers c

inner join payments p on p.customerNumber = c.customerNumber
group by c.customerNumber;

# 12. Was ist der durchschnittliche Pro-Kopf-Umsatz (𝑝𝑚.𝑎𝑚𝑜𝑢𝑛𝑡/𝐴𝑛𝑧𝑎ℎ𝑙 𝑀𝐴) in den einzelnen Standorten?

select
o.city,
o.country,
count(distinct e.employeeNumber) as "MA",
profit.Profit,
profit.Profit / count(distinct e.employeeNumber) as "PKP"

from employees e
inner join offices o on o.officeCode = e.officeCode
	
inner join
		(select 
        o.city,
        sum(pm.amount) as "Profit"
        from offices o
        inner join employees e on o.officeCode = e.officeCode
		inner join customers c on c.salesRepEmployeeNumber = e.employeeNumber
		inner join payments pm on c.customerNumber = pm.customerNumber
        group by o.city) as profit on profit.city = o.city
        
group by o.city, o.country
order by MA desc;

# 13. Vergleiche den Umsatz von den einzelnen Monaten in 2003 mit den Monaten 2004 und erstelle 
# die Differenz:

select
sum(od.quantityOrdered * od.priceEach) as "Umsatz",
month(orderDate) as "Monat",
year(orderDate) as "Jahr",
u2004.umsatz,
u2004.Monat,
u2004.Jahr,
u2004.umsatz - sum(od.quantityOrdered * od.priceEach)  as "Differenz"

from orderdetails od
inner join orders o on o.orderNumber = od.orderNumber

inner join(
			select
            sum(od.quantityOrdered * od.priceEach) as "Umsatz",
			month(orderDate) as "Monat",
            year(orderDate) as "Jahr"
            from orderdetails od
			inner join orders o on o.orderNumber = od.orderNumber
            where year(orderDate) = "2004"
            group by month(orderDate), year(orderDate)) 
            as u2004 on u2004.Monat = month(orderDate)

where year(orderDate) = "2003"
group by month(orderDate), year(orderDate), u2004.umsatz, u2004.Monat, u2004.Jahr;

# 14. Welches Paar von Produkten wird häufig zusammen gekauft?

select

od1.productCode as "Item 1",
od2.productCode as "Item 2",
count(od1.orderNumber) as "zusammen gekauft"
from
orderdetails od1
inner join orderdetails od2 on od1.productCode < od2.productCode and od1.orderNumber = od2.orderNumber

group by od1.productCode, od2.productCode
order by count(od1.orderNumber) desc;

# 15. Gibt es Produkte, die wir im Dezember 2003 verkauft haben, aber nicht im Dezember 2004?

select
	jahr2003.productCode,
	jahr2003.dez2003,
    jahr2004.dez2004
from
    (select 
        od.productCode,
        count(*) as "dez2003"
    from orders o 
    inner join orderdetails od on o.orderNumber = od.orderNumber
    where orderDate like "2003-12%"
    group by od.productCode) jahr2003

left join
    (select 
        od.productCode,
        count(*) as "dez2004"
    from orders o 
    inner join orderdetails od on o.orderNumber = od.orderNumber
    where orderDate like "2004-12%"
    group by od.productCode) jahr2004
on jahr2003.productCode = jahr2004.productCode and jahr2004.productCode is null

group by productCode;

select
p2004.productCode as "Dezember 2004",
p2003.productCode as "Dezember 2003"
from orderdetails od1

inner join (select
od2.productCode, o.orderNumber from orders o
inner join orderdetails od2 on o.orderNumber = od2.orderNumber
where o.orderDate like "2004-12-%") as p2004 on od1.orderNumber = p2004.orderNumber

right join (select
od3.productCode, o2.orderNumber from orders o2
inner join orderdetails od3 on o2.orderNumber = od3.orderNumber
where o2.orderDate like "2003-12-%") as p2003 on od1.orderNumber = p2003.orderNumber;

# 16. Berechne den durchschnittlichen Wert aller Bestellungen in 2004:

select
    avg(sq.Summe) as "Durchschnittlicher Wert Bestellungen"
    
    from(
			select sum(priceEach * quantityOrdered) as "Summe"
			from orders o
            inner join orderdetails od on od.orderNumber = o.orderNumber 
            where o.orderDate like "2004%" 
            group by o.orderNumber) as sq; 

# 17. Welcher Bestellungswert von 2004 ist höher als der ausgerechnete Wert von Aufgabe 16?

select
orderNumber,
sum(priceEach * quantityOrdered) as "Bestellwert"

from orderdetails

group by orderNumber

having sum(priceEach * quantityOrdered) >
	(select
	avg(sq.Summe) as "Durchschnittlicher Wert Bestellungen"
    
    from(
			select sum(priceEach * quantityOrdered) as "Summe"
			from orders o
            inner join orderdetails od on od.orderNumber = o.orderNumber 
            where o.orderDate like "2004%" 
            group by o.orderNumber) as sq)

order by Bestellwert; 
