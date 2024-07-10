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