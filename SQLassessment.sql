SELECT Inv."Id" as "Invoice ID",
	   Inv."BillingDate" as "Billing Date",
	   Cus."Name" as "Customer Name",
	   CASE WHEN Cus."ReferredBy" IS NOT NULL
	   		THEN CusRef."Name"
			ELSE 'No One' 
	   END as "Reffered By" 
FROM public."Invoices" as Inv
LEFT JOIN public."Customers" as Cus ON Inv."CustomerId" = Cus."Id"
LEFT JOIN public."Customers" as CusRef ON Cus."ReferredBy" = CusRef."Id"
ORDER BY Inv."BillingDate";