from datetime import datetime, timedelta

now = datetime.now()
print(f"Current Date and Time: {now}")

future_date = now + timedelta(days=10)
print(f"Date 10 Days Later: {future_date}")
