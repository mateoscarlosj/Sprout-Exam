import os

SECRET_KEY = os.getenv("SECRET_KEY", "09b1e1b7cf784b35a0d2a2a7bda5893b")
AUTH_ALGORITHM = os.getenv("AUTH_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 5000))
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://sprout:admin@db:5432/sprout")
ALLOW_ORIGINS = os.getenv("ALLOW_ORIGINS","*")