## Data Model



### Bookings

Primary key: booking\_id



### Passengers

Primary key: passenger\_id
Foreign key: booking\_id



### Payments

Primary key: transaction\_id
Foreign key: booking\_id, passenger\_id





### Relationship Diagram

cruise\_bookings (1) 	──── (many) passengers

cruise\_bookings (1) 	──── (many) payments

passengers (1) 		──── (many) payments

