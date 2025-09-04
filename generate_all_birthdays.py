import os
from datetime import datetime
from birthday_scraper import get_birthdays_for_date  # use your existing function

output_dir = "birthdays"
os.makedirs(output_dir, exist_ok=True)

for month in range(1, 13):
    for day in range(1, 32):
        try:
            date_obj = datetime(2023, month, day)  # Leap year handled below
            month_str = date_obj.strftime('%B').lower()
            day_str = date_obj.strftime('%d').lstrip('0')
            filename = f"{month_str}-{day_str}.html"

            filename = f"{month_str}-{day_str}.html"
            filepath = os.path.join(output_dir, filename)

            # Run your scraper function for this date
            content = get_birthdays_for_date(month, day)

            # Save the result to an HTML file
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

        except ValueError:
            continue  # skip invalid dates (e.g., Feb 30)
