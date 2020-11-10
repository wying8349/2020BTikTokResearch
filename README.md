# 2020BTikTokResearch

Daily Schedule
Previously
- Did some researches (see related work)
- A failed try of scraping data from tiktok
  - based on this [tutorial](https://blog.csdn.net/u011422450/article/details/105834021)
  - Possible reasons:
    - SSL Pinning from TikTok ([refer](https://blog.csdn.net/qq_38851536/article/details/93217470))
      Yet, I still failed even if I used a rooted android simulator and applied Xposed+Justtrustme to it. 
    - TikTok forbids access from China. This is not solvable by simply using a VPN or proxy because it will scan the sim card and ban any visit from a phone that have a Chinese Sim card.
      It is still confusing because I basically ran it on an android simulator, which technically have no sim card. 
      The error however seems to be the same with the error I see when I try to use TikTok on a phone that has a Chinese Sim card. 
- Made a proposal

Nov 7, 2020
- What I did:
  1. I researched for new methods to scrap data from TikTok
  2. I found [TikTokApi](https://github.com/davidteather/TikTok-Api). 
  3. Cloned the repo and installed with pip on Windows
  
- Problems I met:
  1. Contantly recieving the error messagy: Browser object has no attribute verifyFp
     Possible Causes and solutions: refering to [this issue](https://github.com/davidteather/TikTok-Api/issues/237)
     - tried to solve with re-setting the enviroment variables and add chromium in to the path (fail)
     - tried to solve by setting it async (failed)
     

Nov 8, 2020
- What I did:
  1. Continuing with solving the no attribute verifyFp issue
     - It seems sometimes the problem happens on one system and not on another, so I tried to restart the API on a linux VM and it worked. 
  2. Wrote a script that scraps the data of 100 videos of a specific day and write it to a nice json file
  3. Setting up a git repo to record this

- Problems I met:
  1. When I use the function .trending, what is the trending am I getting? Is it really the most popular videos at that time?
  2. TikTok is good at AI recommending. What if I create an account that shows to have a high interest with TV series? Will the trending get more videos related to TV series? Should I do that?

- Things to do later:
  1. Research on .trending (se Problems today)
  2. What is attribute verifyFp?
  3. Find a way to wash and analyze the json file I get.
  4. I need to meet with professor

Nov 9, 2020
- What I did:
  1. scraps 100 videos data today. 
  not really much things done today. 
  
- Problems I meet:
  1. if i only look at the desc, there is probably not much to analyze. unlike twitter, in tiktok, these descriptions of a video are not whole sentances and made it difficult to do nlp. Probably need to download the videos and do some analysis. 
  2. the data now is really noisy. there might not be 1 TV series related tiktok in the 100 I am getting. I can manually looking at it, but I also need a way to deal with this. 

- Things to do later:
  1. Research on .trending (se Problems today)
  2. What is attribute verifyFp?
  3. Find a way to wash and analyze the json file I get.
  4. I need to meet with professor
