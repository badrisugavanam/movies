# Movies Trailer
A movie trailer website project

#Quick Start 
- Install python 2.7.9 from this [website](https://www.python.org/downloads/release/python-279/) and follow instructions specific to your platform
- Clone the repo: `git clone https://github.com/badrisugavanam/movies.git`
- Install the third party python API https://github.com/celiao/tmdbsimple for accessing https://www.themoviedb.org 
    - pip install tmdbsimple   
- Install another third party python API https://github.com/doganaydin/themoviedb for accessing https://www.themoviedb.org poster images for a specific movie 
    - clone the repo @ https://github.com/doganaydin/themoviedb and navigate to the directory of the cloned repo and do the following below 
    - pip install requests fuzzywuzzy
    - sudo python setup.py install

#Important Request API Key  
  - Follow the steps mentioned in API Key subsection @ https://github.com/celiao/tmdbsimple
  - Replace YOUR_API_KEY with your API Key in entertainment_center.py

#What's included 
```

movies/
│   ├── entertainment_center.py   -- File that need to be executed
│   ├── fresh_tomatoes.py
└── └── media.py
```
