import sys
import requests

def get_bitcoin_price():
    try:
        # Check if the user entered a command-line argument for the number of Bitcoins
        if len(sys.argv) != 2:
            raise ValueError("Please specify the number of Bitcoins to buy as a command-line argument.")

        # Convert the command-line argument to a float (number of Bitcoins)
        bitcoins = float(sys.argv[1])
    except (ValueError, IndexError):
        print("Error: Please provide a valid number of Bitcoins as a command-line argument.")
        sys.exit(1)

    try:
        # Make a GET request to the CoinDesk API to fetch the Bitcoin price index
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()  # Raise an error for HTTP request issues

        # Extract the current Bitcoin price from the API response JSON
        bitcoin_data = response.json()
        current_price = bitcoin_data['bpi']['USD']['rate_float']

        # Calculate the total cost in USD
        total_cost = bitcoins * current_price

        # Output the current cost of Bitcoins in USD to four decimal places with a thousands separator
        print(f"The current cost of {bitcoins} Bitcoins is ${total_cost:,.4f}")
    except requests.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        sys.exit(1)

if __name__ == "__main__":
    get_bitcoin_price()
