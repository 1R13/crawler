 __    __    ___  ____     __  ____    ____  __    __  _        ___  ____  
|  |__|  |  /  _]|    \   /  ]|    \  /    ||  |__|  || |      /  _]|    \ 
|  |  |  | /  [_ |  o  ) /  / |  D  )|  o  ||  |  |  || |     /  [_ |  D  )
|  |  |  ||    _]|     |/  /  |    / |     ||  |  |  || |___ |    _]|    / 
|  `  '  ||   [_ |  O  /   \_ |    \ |  _  ||  `  '  ||     ||   [_ |    \ 
 \      / |     ||     \     ||  .  \|  |  | \      / |     ||     ||  .  \
  \_/\_/  |_____||_____|\____||__|\_||__|__|  \_/\_/  |_____||_____||__|\_|
                                                                              
                                                                      (WebCrawler - art by https://patorjk.com)

This is a simple tool, for website crawling.
Simple automation finds reffered urls in the source code of a given website.

The loops will be performed as follows :

  The website will be requestet via http/s and the resulting source code will be scanned line-by-line on pat-
  terns matching an HTTP format. The found strings are collected as objects and proofed of uniquenes. New ones
  are added to the found and todo2 list. After finishing the website, the URL gets removed from the todo1 list
  and added to the search list. After running the crawler on all websites from todo1, the entries from todo2
  are copied over and todo2 gets cleared. This will be done until the loop index matches the set level variable.

There are colors :
  
  At the moment there is a color code integrated :
    
    yellow  = .css or .js
    cyan    = .png, .jpg, .jpeg or .gif
    green   = .pdf
    red     = .txt

-------------------------------------------------------------------------------------------------------------

Syntax  : 

-v                    : Verbose output, printing stages and every target on finish or fail   [Default: False]
-u <https://...>      : Root URL, sets the first URL for the loop           [Default: https://www.google.com]
-r <string>           : Restrain as a string must be set to somewhat control the direction  [Default: google]
-l <integer>          : The level sets the depth on loops that whill be performed                [Default: 2]
