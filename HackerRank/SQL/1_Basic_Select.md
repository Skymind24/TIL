## Revising the Select Query 1.
Solved on 2024.07.09  
[SQl - Revising the Select Query 1.](https://www.hackerrank.com/challenges/revising-the-select-query/problem?isFullScreen=true)
> Q. Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.
The CITY table is described as follows:
    <p align="center">
    <img src="image.png" width="25%" height="25%">
    </p>

A.
```sql
select *
from city
where countrycode='USA'
           and population>100000;
```
<br>

## Revision the Seelct Query 2.
Solved on 2024.07.09  
[SQl - Revising the Select Query 2.](https://www.hackerrank.com/challenges/revising-the-select-query-2/problem?isFullScreen=true)
> Q. Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.
The CITY table is described as follows:
    <p align="center">
    <img src="image.png" width="25%" height="25%">
    </p>

A.
```sql
select name
from city
where countrycode='USA'
           and population>120000;
```
<br>

## Select All.
Solved on 2024.07.09  
[SQl - Select All.](https://www.hackerrank.com/challenges/select-all-sql/problem?isFullScreen=true)
> Q. Query all columns (attributes) for every row in the CITY table.
The CITY table is described as follows:
    <p align="center">
    <img src="image.png" width="25%" height="25%">
    </p>

A.
```sql
select *
from city;
```
<br>

## Select By ID.
Solved on 2024.07.09  
[SQl - Select By ID.](https://www.hackerrank.com/challenges/select-by-id/problem?isFullScreen=true)
> Q. Query all columns for a city in CITY with the ID 1661.
The CITY table is described as follows:
    <p align="center">
    <img src="image.png" width="25%" height="25%">
    </p>

A.
```sql
select *
from city
where id=1661;
```
<br>

## Japanese Cities' Attrbutes.
Solved on 2024.07.09  
[SQl - Japanese Cities' Attrbutes.](https://www.hackerrank.com/challenges/japanese-cities-attributes/problem?isFullScreen=true)
> Q. Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.
The CITY table is described as follows:
    <p align="center">
    <img src="image.png" width="25%" height="25%">
    </p>

A.
```sql
select *
from city
where countrycode='JPN';
```
<br>

## Japanese Cities' Names.
Solved on 2024.07.09  
[SQl - Japanese Cities' Names.](https://www.hackerrank.com/challenges/japanese-cities-name/problem?isFullScreen=true)
> Q. Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.
The CITY table is described as follows:
    <p align="center">
    <img src="image.png" width="25%" height="25%">
    </p>

A.
```sql
select name 
from city
where countrycode='JPN';
```
<br>

## Weather Observation Station 1.
Solved on 2024.07.09  
[SQl - Weather Observation Station 1.](https://www.hackerrank.com/challenges/weather-observation-station-1/problem?isFullScreen=true)
> Q. Query a list of CITY and STATE from the STATION table.
The STATION table is described as follows:
    <p align="center">
    <img src="image-1.png" width="25%" height="25%">
    </p>

A.
```sql
select city, state
from station;
```
<br>

## Weather Observation Station 3.
Solved on 2024.07.09  
[SQl - Weather Observation Station 3.](https://www.hackerrank.com/challenges/weather-observation-station-3/problem?isFullScreen=true)
> Q. Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.
The STATION table is described as follows:
    <p align="center">
    <img src="image-1.png" width="25%" height="25%">
    </p>

A.
```sql
select distinct city
from station
where id%2=0;
```
<br>

## Weather Observation Station 4.
Solved on 2024.07.09  
[SQl - Weather Observation Station 4.](https://www.hackerrank.com/challenges/weather-observation-station-4/problem?isFullScreen=true)
> Q. Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
The STATION table is described as follows:
    <p align="center">
    <img src="image-1.png" width="25%" height="25%">
    </p>
For example, if there are three records in the table with CITY values 'New York', 'New York', 'Bengalaru', there are 2 different city names: 'New York' and 'Bengalaru'. The query returns 1, because *total number of records - number of uique city names = 3 - 2 = 1*.

A. 
```sql
select
    (select count(city)
    from station)
    -
    (select count(distinct city)
    from station);
```
<br>

## Weather Observation Station 5.
Solved on 2024.07.09  
[SQl - Weather Observation Station 5.](https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true)
> Q. Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
The STATION table is described as follows:
    <p align="center">
    <img src="image-1.png" width="25%" height="25%">
    </p>
For example, CITY has four entries: DEF, ABC, PQRS and WXY.  
**Sample Output**  
    - ABC 3   
    - PQRS 4  
**Explanation**  
When ordered alphabetically, the CITY names are listed as ABC, DEF, PQRS, and WXY, with lengths  and . The longest name is PQRS, but there are  options for shortest named city. Choose ABC, because it comes first alphabetically.  
**Note**  
You can write two separate queries to get the desired output. It need not be a single query.

A.
```sql
(select city, length(city)
from station
order by length(city) desc, city asc
limit 1)

union

(select city, length(city)
from station
order by length(city), city
limit 1);
```
<br>

## Weather Observation Station 6.
Solved on 2024.07.09  
[SQl - Weather Observation Station 6.](https://www.hackerrank.com/challenges/weather-observation-station-6/problem?isFullScreen=true)
> Q. Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
The STATION table is described as follows:
    <p align="center">
    <img src="image-1.png" width="25%" height="25%">
    </p>

A.
```sql
select city
from station
where city like 'a%'
           or city like 'e%'
           or city like 'i%'
           or city like 'o%'
           or city like 'u%'; 
```
<br>

## Weather Observation Station 7.
Solved on 2024.07.09  
[SQl - Weather Observation Station 7.](https://www.hackerrank.com/challenges/weather-observation-station-7/problem?isFullScreen=true)
> Q. Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
The STATION table is described as follows:
    <p align="center">
    <img src="image-1.png" width="25%" height="25%">
    </p>

A.
```sql
select distinct city
from station
where city like '%a'
           or city like '%e'
           or city like '%i'
           or city like '%o'
           or city like '%u';
```
<br>