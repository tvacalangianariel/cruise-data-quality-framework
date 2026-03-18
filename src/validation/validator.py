import pandas as pd


def validate():
    bookings = pd.read_csv("../../data/bookings.csv")
    passengers = pd.read_csv("../../data/passengers.csv")
    payments = pd.read_csv("../../data/payments.csv")

    issues = []
    
    # 1. Orphan passengers
    #    -check if there are invalid booking(s) in bookings dataset using passengers.booking_id 
    invalid_passengers = passengers[~passengers["booking_id"].isin(bookings["booking_id"])]
    if len(invalid_passengers) > 0:
        issues.append(f"Orphan passengers: {len(invalid_passengers)}")
    
    # 2. Orphan payments
    #    -check if there are invalid/orphan passenger that made transaction in payments dataset
    invalid_payments = payments[~payments["passenger_id"].isin(passengers["passenger_id"])]
    if len(invalid_payments) > 0:
        issues.append(f"Orphan payments: {len(invalid_payments)}")
    
    # 3. Negative fare
    #    -check if there are negative fare in bookings dataset
    neg_fare = (bookings["total_fare"] < 0).sum()
    if neg_fare > 0:
        issues.append(f"Negative booking fares: {neg_fare}")
    
    # 4. Payment mismatch
    #    -check if there are mismatch in payments
    payment_sum = payments.groupby("booking_id")["payment_amount"].sum()
    merged = bookings.set_index("booking_id").join(payment_sum)
    
    mismatch = (merged["payment_amount"] > merged["total_fare"]).sum()
    if mismatch > 0:
        issues.append(f"Overpaid bookings: {mismatch}")
    
    return issues



print(validate())