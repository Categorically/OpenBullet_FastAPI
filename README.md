# OpenBullet_FastAPI
Test OpenBullet configs with a remote server like pythons' FastAPI module.

Using requests module is not the best, A better module might be aiohttp.

# FastAPI
```pip install fastapi```

# Uvicorn
```pip install uvicorn```

# OpenBullet2Python

Clone the repo https://github.com/Categorically/OpenBullet2Python

Files
- Root
  - OpenBullet2Python
      - TestConfig.py
  - main.py
 
# Running main.py
```uvicorn main:app --reload```

# Testing a config
Goto http://127.0.0.1:8000/docs

Config text must be base64 encoded
 
![docs](https://i.imgur.com/MM1KoaG.png)
