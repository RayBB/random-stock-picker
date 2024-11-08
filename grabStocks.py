import urllib.request
import json
import re

def grab_stocks():
    # Download the NASDAQ traded symbols file
    url = 'ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqtraded.txt'
    
    try:
        # Download and decode the content
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
    except Exception as e:
        raise Exception(f"Failed to download NASDAQ symbols: {str(e)}")

    # Extract stock symbols using regex
    # Matches patterns like 'A|AAIC' and captures everything after the pipe
    pattern = r'^\w\|(\w+)'
    symbols = []
    
    for line in content.split('\n'):
        match = re.match(pattern, line)
        if match:
            symbols.append(match.group(1))
    
    # Write to JSON file
    with open('stocks.json', 'w') as f:
        json.dump(symbols, f)

if __name__ == '__main__':
    grab_stocks()
