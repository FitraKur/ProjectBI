select a.order_id , b.customer_id , b.customer_city , a.order_purchase_timestamp  
	from tb_order a, tb_customer b
	where a.customer_id = b.customer_id 
	and lower(a.order_status) not like '%canceled%'; 