1.  SELECT * FROM customer
    WHERE gender="female";

2.  SELECT customer.first_name, customer.last_name 
    FROM customer, order  
    WHERE customer.id = order.fk_customer

3.  SELECT customer.first_name, customer.last_name, order.sum 
    FROM customer, order 
    WHERE customer.id = order.fk_customer

4. SELECT order_nr
    FROM order
    WHERE order_item.fk_order > 2


5.  SELECT customer.id, customer.first_name, MAX(customer.age)
    FROM customer 
    WHERE customer.gender="male"
    FULL OUTER
    JOIN (customer.id, customer.first_name, MAX(customer.age)
    FROM customer 
    WHERE customer.gender="female")
