
## Data Model



### Bookings

Primary key: booking_id



### Passengers

Primary key: passenger_id
Foreign key: booking_id



### Payments

Primary key: transaction_id
Foreign key: booking_id, passenger_id

