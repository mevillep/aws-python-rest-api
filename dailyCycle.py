import json
import requests
from datetime import datetime, timedelta
import pandas as pd
import math




def getStats(event, context):
  
  # to make this mode generic
  # JSON contract
  # asset_name
  # cycle_length
  # cycle_low - [] of dates
  
  cycle_length = 60
  # Find today's date
  today = datetime.now().date()
  input_date = '2023-1-6'
  date_format = '%Y-%m-%d'
  input_date_obj = datetime.strptime(input_date, date_format)

  # Check if the input date is in future
  if input_date_obj > datetime.now():
      print("Input date cannot be in the future.")
  else:
      url = f'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30&to={input_date}'

      # Make the GET request
      response = requests.get(url)

      # Parse the JSON response
      data = response.json()

      # Check if the response is empty
      if not data:
          print("Data is empty")
      else:
          # Convert the list of prices to a DataFrame
          prices_df = pd.DataFrame(data['prices'], columns=['date', 'price'])
          prices_df['date'] = pd.to_datetime(prices_df['date'], unit='ms')
          
          # Filter the dataframe for the input date
          prices_df = prices_df[prices_df['date'].dt.date == input_date_obj.date()]
          if prices_df.empty:
              print(f"No Data found for {input_date}")
          else:
              # Find the closing price
              closing_price = prices_df['price'].iloc[-1]
              print(f'The closing price of Bitcoin on {input_date} is {closing_price} USD')


  # Add 30 days to the input date for expected midcycle low
  midcycle_low_date = input_date_obj + timedelta(days=math.floor(cycle_length/2))
    
    # Add 60 days to the input date for expected cycle low
  cycle_low_date = input_date_obj + timedelta(days=cycle_length)
  


  def daily():


        # Find the number of days that have passed since a given date object
        
        days_passed = (datetime.strptime(today.strftime("%Y-%m-%d"),date_format) - input_date_obj).days




          # Find the number of days until a given cycle low date
        days_until_cycle_low = (cycle_low_date - datetime.strptime(today.strftime("%Y-%m-%d"),date_format)).days

    

        # Find the current price of Bitcoin
        url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        response = requests.get(url)
        data = response.json()
        current_price = data['bpi']['USD']['rate_float']

        

        percent_change = ((current_price - closing_price) / closing_price) * 100

        
        
        ##  Amplitude
        
        # Make the GET request to the CoinGecko API
        url = f'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days={days_passed + 1}&to={input_date_obj}'
        response = requests.get(url)
        data = response.json()


        # Convert the list of prices to a DataFrame
        prices_df = pd.DataFrame(data['prices'], columns=['date', 'price'])

        # Find the lowest price
        lowest_price = prices_df['price'].min()


        # Find the highest price
        highest_price = prices_df['price'].max()

        
        amplitude = highest_price - lowest_price

        percent_amplitude = ((amplitude) / lowest_price ) * 100

        cycle_low_formatted = input_date_obj.strftime('%B %d, %Y')
        current_date_formatted = today.strftime('%B %d, %Y')
        cycle_low_date_formatted = cycle_low_date.strftime('%B %d, %Y')

        output = f"The cycle low happened on - {cycle_low_formatted}\n"
        output += f"The price of Bitcoin on cycle low - {int(closing_price)}\n"
        output += f"Today is - {current_date_formatted}\n"
        output += f"The price of Bitcoin today is - {current_price}\n"
        output += f"It has been - {days_passed} - days since last cycle low\n"
        output += f"Next cycle low expected date is - {cycle_low_date_formatted} - which will happen in - {days_until_cycle_low} - days\n"
        output += f"Current daily cycle is - {int(((days_passed)/cycle_length)* 100)}% complete\n"
        output += f"Current cycle High - {int(highest_price)}\n"
        output += f"Current Cycle low - {int(lowest_price)}\n"
        output += f"Current Amplitude of the cycle - {int(amplitude)} $$$\n"
        output += f"Amplitude percentage change - {int(percent_amplitude)}\n"

        print(output)




          
  daily()
  // write function to  get date
  

    