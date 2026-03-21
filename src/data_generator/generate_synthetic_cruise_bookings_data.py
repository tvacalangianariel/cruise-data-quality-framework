import pandas as pd
import random
import numpy as np
from datetime import datetime, timedelta


def generate_data(num_bookings=10000):
    bookings = []
    passengers = []
    payments = []
    
    # -----------------------------
    # Generate bookings (no cabin_type yet)
    # -----------------------------
    for b in range(num_bookings):
        booking_id = 1000000000 + b
        ship = random.choice(["Oceanic Explorer", "Sea Voyager", "Atlantic Dream"])
        booking_date = datetime.now() - timedelta(days=random.randint(1, 365))
        sailing_date = booking_date + timedelta(days=random.randint(-10, 200))
    
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

    # -----------------------------
    # Convert to DataFrame
    # -----------------------------
    bookings_df = pd.DataFrame(bookings)

    # -----------------------------
    # Apply CONTROLLED distribution to cabin_type
    # -----------------------------
    cabin_ranges = {
        'Balcony': (0.60, 0.70),
        'Interior': (0.20, 0.30),
        'Oceanview': (0.10, 0.20),
        'Suite': (0.01, 0.05)
    }

    random_weights = {
        k: np.random.uniform(v[0], v[1]) for k, v in cabin_ranges.items()
    }

    total = sum(random_weights.values())
    normalized_weights = {k: v / total for k, v in random_weights.items()}

    bookings_df['cabin_type'] = np.random.choice(
        list(normalized_weights.keys()),
        size=len(bookings_df),
        p=list(normalized_weights.values())
    )

    # Debug distribution
    print("\nCabin Type Distribution:")
    print(bookings_df['cabin_type'].value_counts(normalize=True))
    print("Weights:", normalized_weights)

    # -----------------------------
    # Apply RANDOM missing to 'ship'
    # -----------------------------
    missing_rate = np.random.uniform(0.001, 0.10)
    num_missing = int(len(bookings_df) * missing_rate)

    missing_indices = np.random.choice(
        bookings_df.index,
        size=num_missing,
        replace=False
    )

    bookings_df.loc[missing_indices, 'ship'] = None

    print(f"\nShip missing rate: {bookings_df['ship'].isna().mean():.4f}")

    # -----------------------------
    # Save files
    # -----------------------------
    bookings_df.to_csv("../../data/bookings.csv", index=False)
    pd.DataFrame(passengers).to_csv("../../data/passengers.csv", index=False)
    pd.DataFrame(payments).to_csv("../../data/payments.csv", index=False)
    
    print("Enterprise dataset generated.")
        


#generate_data()
