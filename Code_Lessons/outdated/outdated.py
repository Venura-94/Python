def is_valid_date(date_str, month_names):
    try:
        parts = date_str.split(' ')
        if len(parts) == 3:
            month, day, year = parts
            month = month.capitalize()
        else:
            month, day, year = parts[0].capitalize(), parts[1][:-1], parts[2]

        if month in month_names and 1 <= int(day) <= 31 and 1 <= int(year) <= 9999:
            return True
    except (ValueError, IndexError):
        pass
    return False

def main():
    month_names = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    while True:
        date_str = input("Enter a date (month day year) or (month/day/year): ")
        if is_valid_date(date_str, month_names):
            parts = date_str.split(' ')
            if len(parts) == 3:
                month, day, year = parts
                month = month_names.index(month.capitalize()) + 1
            else:
                month, day, year = parts[0].capitalize(), parts[1][:-1], parts[2]
                month = month_names.index(month.capitalize()) + 1
            formatted_date = f"{int(year):04d}-{int(month):02d}-{int(day):02d}"
            print(f"Formatted date in YYYY-MM-DD: {formatted_date}")
            break
        else:
            print("Invalid date format. Please try again.")

if __name__ == "__main__":
    main()