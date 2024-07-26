## Type of Triangle.
Solved on 2024.07.10  
[SQl - Type of Triangle.](https://www.hackerrank.com/challenges/what-type-of-triangle/problem?isFullScreen=true)
> Q. Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:  
    - Equilateral: It's a triangle with  sides of equal length.  
    - Isosceles: It's a triangle with  sides of equal length.  
    - Scalene: It's a triangle with  sides of differing lengths.  
    - Not A Triangle: The given values of A, B, and C don't form a triangle.  
The TRIANGLES table is described as follows:
    <p align="center">
    <img src="figure/triangle_table.png" width="25%" height="25%">
    </p>
Each row in the table denotes the lengths of each of a triangle's three sides.

A.
```sql
alter table triangles add column tri_type varchar(32);

update triangles
set tri_type= if (a+b<=c or a+c<=b or b+c<=a, 'Not A Triangle',
                if (a=b and b=c and c=a, 'Equilateral',
                    if ((a=b and a!=c) or (b=c and c!=a) or (c=a and a!=b), 'Isosceles', 'Scalene')));
                                    
select tri_type
from triangles;
```
<br>

## The PADS.
Solved on 2024.07.26  
[SQl - The PADS.](https://www.hackerrank.com/challenges/the-pads/problem?isFullScreen=true)
> Q. Generate the following two result sets:  
Query 1. Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first letter of each profession as a parenthetical (i.e.: enclosed in parentheses).  
`For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).`  
Query 2. Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order, and output them in the following format:  
`There are a total of [occupation_count] [occupation]s.`  
where [occupation_count] is the number of occurrences of an occupation in OCCUPATIONS and [occupation] is the lowercase occupation name. If more than one Occupation has the same [occupation_count], they should be ordered alphabetically.  
The OCCUPATIONS table is described as follows:
    <p align="center">
    <img src="figure/occupation_table.png" width="25%" height="25%">
    </p>
Occupation will only contain one of the following values: Doctor, Professor, Singer or Actor.

**Sample Output**
```
Ashely(P)
Christeen(P)
Jane(A)
Jenny(D)
Julia(A)
Ketty(P)
Maria(A)
Meera(S)
Priya(S)
Samantha(D)
There are a total of 2 doctors.
There are a total of 2 singers.
There are a total of 3 actors.
There are a total of 3 professors.
```
**Explanation**
```
The results of the first query are formatted to the problem description's specifications.
The results of the second query are ascendingly ordered first by number of names corresponding to each profession (2, 2, 3, 3), and then alphabetically by profession.
```

A.
```sql
select concat(name, "(", mid(occupation, 1, 1), ")")
from occupations
order by name asc;

select concat("There are a total of ", count(occupation), " ", lcase(occupation), "s.") count
from occupations
group by occupation
order by count asc, occupation asc;
```
<br>
