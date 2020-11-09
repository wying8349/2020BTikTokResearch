from TikTokApi import TikTokApi
import json as json
from datetime import date

# Starts TikTokApi
api = TikTokApi()

# The Number of trending TikToks you want to be displayed
results = 100

# Returns a list of dictionaries of the trending object
trending = api.trending(results)

# Loops over every tiktok
for tiktok in trending:
    # Prints the text of the tiktok
    print(tiktok["desc"])
    

print(len(trending))

# Print the Output
today = date.today()
d = today.strftime("%b-%d-%Y")
with open("dailyRecode/TikTokData"+d+".json", "w") as fout:
    json.dump(trending, fout, indent=4, sort_keys=True)
