import wikipediaapi
from datetime import datetime

def get_birthdays_for_date(month, day):
    wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='daily-birthdays-script/1.0 (https://github.com/srw3804/daily-birthdays)'
)

    month_name = datetime(2023, month, day).strftime('%B')
    date_title = f"{month_name}_{day}"
    
    page = wiki.page(date_title)
    if not page.exists():
        return f"<h2>Celebrity Birthdays - {month_name} {day}</h2><p>No data found.</p>"
    
    lines = page.text.splitlines()
    birthdays = []
    in_births_section = False

    for line in lines:
        if line.strip().lower() == "births":
            in_births_section = True
            continue
        if in_births_section:
            if line.strip() == "":
                continue
            if line.strip() in {"Deaths", "Holidays and observances"}:
                break
            if line.strip().startswith("*"):
                birthdays.append(line.strip()[1:].strip())

    html = f"<h2>Celebrity Birthdays - {month_name} {day}</h2>\n<ul>"
    for person in birthdays:
        html += f"<li>{person}</li>\n"
    html += "</ul>"

    return html
