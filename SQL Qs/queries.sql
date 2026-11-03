--q1
select * from Students s
JOIN Enrollments e
ON s.student_id=e.student_id
WHERE grade>80
--q2
SELECT s.Name, e.grade, c.Title
FROM Students s
JOIN Enrollments e
ON s.student_id = e.student_id
JOIN Courses c
ON c.course_id = e.course_id;
--q3
--part 1
select count(Name) as Total_Students
FROM Students
--part 2
select avg(grade) as Grade_avg,c.Title
FROM Courses c 
JOIN Enrollments e 
on c.course_id=e.course_id
group by c.Title
--part 3
SELECT c.Title, COUNT(DISTINCT e.student_id) AS Total_Students
FROM Courses c
JOIN Enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.Title;

--q4

SELECT s.student_id, s.Name, AVG(e.grade) AS highest
FROM Students s
JOIN Enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id, s.Name
ORDER BY highest DESC
LIMIT 1;

--q5
select s.Name from Students s
join Enrollments e on
s.student_id=e.student_id WHERE e.grade>
(select avg(grade) from Enrollments)

--q7
--already in 1NF
--non key attributes should depend on primary key 2NF
--as an order can contain multiple products so id could be repeated so we have to get product name and order id as composite 
--key so we have to see if all other have dependency on them but customer name depends only
--on order id and product price depends only on product name so bothdoes not depends on both we make separate tables
--order(order_id(pk),customer_name),products(product name(pk),product price),order_items(order_id,product name)
--non key attributes should not depends on other non key attributes 3NF


