import pandas as pd
import random
from datetime import datetime, timedelta


def generate_data(num_bookings=10000):
    bookings = []
    passengers = []
    payments = []
    
    # create bookings based on params passed
    for b in range(num_bookings):
        booking_id = 1000000000 + b
        ship = random.choice(["Oceanic Explorer", "Sea Voyager", "Atlantic Dream"])
        booking_date = datetime.now() - timedelta(days=random.randint(1, 365))
        sailing_date = booking_date + timedelta(days=random.randint(-10, 200))  # invalid cases
    
        occupants = random.randint(1, 4)
        total_fare = round(random.uniform(-500, 10000), 2)
    
        bookings.append({
            "booking_id": booking_id,
            "ship": ship,
            "booking_date": booking_date,
            "sailing_date": sailing_date,
            "occupants": occupants,
            "total_fare": total_fare
            })
    
        for p in range(occupants):
            passenger_id = booking_id * 10 + p
    
            passengers.append({
                "passenger_id": passenger_id,
                "booking_id": booking_id,
                "passenger_name": f"Guest_{passenger_id}",
                "gender": random.choice(["M", "F"]),
                "passenger_email": None if random.random() < 0.05 else f"user{p}@email.com"
            })
            
            payments.append({
                "transaction_id": passenger_id * 100,
                "booking_id": booking_id,
                "passenger_id": passenger_id,
                "payment_amount": round(random.uniform(-200, 5000), 2),
                "payment_status": random.choice(["Paid", "Pending", "Failed"])
            })

    #generate files
    pd.DataFrame(bookings).to_csv("../../data/bookings.csv", index=False)
    pd.DataFrame(passengers).to_csv("../../data/passengers.csv", index=False)
    pd.DataFrame(payments).to_csv("../../data/payments.csv", index=False)
    
    print("Enterprise dataset generated.")
        


generate_data()
