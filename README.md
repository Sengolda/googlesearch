### Google Search
- A module that searches google (This is my first time making a sucessful module)
### how to install?
- Since this is very simple i will not put it on Pypi so you can install like this:
```bash
python3 -m pip install -U git+https://github.com/Sengolda/googlesearch
```

- Other way (Not recomended):
```bash
$ git clone https://github.com/Sengolda/googlesearch.git
$ cd downloads/googlesearch
$ python3 -m pip install -U .
```
- Make sure you replace "Downloads" with where your one has been saved
#### Contributing
- TO contribute just submit a pull request (There is no req) 
#### How to import?
- You can easily import by using the following:
```py
import googlesearch
# TODO: OR
from googlesearch import *
```
- Example Usage:
```py
googlesearch.search_google(term="Hello World!")
# IF YOU DID from googlesearch import * , this will not work, then you would use:
search_google(term="Hello World!")
```
