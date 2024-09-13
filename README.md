# crypto-price-finder-to-csv
TL;DR: A simple (and free!) python script that makes use of CoinGeckoTerminal's public API to get the past 6 months of end-of-day prices for any token pool you can find on CoinGeckoTerminal. Could be good for tax info, certainly was for me :) [Legal obligation - none of this is tax advice!]

Too long, did read: 
This Python script allows you to fetch historical price data for cryptocurrency tokens from GeckoTerminal. It retrieves up to 6 months of daily price data and saves it to a CSV file in your current working directory.

## Prerequisites

Before running the script, make sure you have Python installed on your system. This script was developed using Python 3.7+ in case you have dependency issues, but you shouldn't!

Main thing is if you're a coding newbie doing this from total scratch, you'll need to install the `requests` library. You can do this by running:

```
pip install requests
```

## Usage

1. Git clone this repository `git clone https://github.com/mark-lord/crypto-price-finder-to-csv` or else download the `price-finder.py` script. If you're having trouble doing either of those things, don't worry, you can navigate directly into the file here on Github and literally copy/paste the code into a textfile and then do save-as `price-finder.py`. Side note, if you're worried about this being malware in any way, then when you go to the file here in Github, you can do the same thing of opening the code, copying and pasting it into chatGPT or Claude, and it'll tell you what it does!

2. If you haven't already, open a terminal or command prompt and navigate to the directory containing the script. I use Cursor (a VSCode fork) but anything with commandline will do. For Mac users, you can right click on the folder containing the `price-finder.py` file and select open in Terminal. Windows you can navigate to the folder, click in the address bar and type CMD to open up commandline, and for Linux... well, if you're on Linux you're probably not needing this level of info!

3. Go to whichever pool you're interested in on CoinGeckoTerminal - say you have an employer paying you a token on a WETH / UniSwapv3 pool - then copy the URL for the page, then run the price-finder.py script with the GeckoTerminal pool URL as an argument:

```
python price-finder.py https://www.geckoterminal.com/eth/pools/{tokenidentifier}
```

Replace the whole URL, curly brackets included, with the GeckoTerminal pool URL of the token you're interested in.

4. The script will fetch the pool information and up to 6 months of daily price data, then save it to a CSV file named after the token pair (e.g., "memecoin-SOL.csv").

## Output

The script will display pool information in the terminal and create a CSV file with two columns:
- Date: The date of the price data point
- Price (in USD): The closing price for that day in USD, assuming USD is still the default - was for me at time of creating the script.

## Limitations

- The script can only retrieve up to 6 months of historical data. (Sad sad)
- Price data is provided in USD.
- The accuracy and availability of data depend on GeckoTerminal's API, which they could change at any moment - like they did with the normal CoinGecko free API

## Note

This script relies on the current structure of GeckoTerminal's website and API. If you're using this script well into the future, it's possible that GeckoTerminal may have changed their API or policies, which could cause the script to stop working. Check GeckoTerminal's latest documentation or terms of service if you encounter issues, and then hand the docs to good Cursor (or Claude.AI directly, or whatever crazy service you're using that I cannot at this point in time possibly hope to fathom)

## Contributing

Feel free to fork this repository with improvements or bug fixes! I'm have clinically severe ADHD so I'm not the best person for maintaining any repos, I just occasionally make a cool thing and find I want to share it (hehe)

## License

This project is open source and available under the [Apache 2.0](LICENSE). In short and in plain English, I want anyone to just use it as you see fit - I want this to be as open as possible!

