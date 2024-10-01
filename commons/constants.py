from Database.db import DATABASE_URL

SECRET_KEY="4567890-09876543456789098765434567890uytrtghjk09876789"

''' these are jwt constant and can be use again and again so 
make all these in separate file and can be use when need like 
signing_key
algorithm'''

SIMPLE_JWT={
    "SIGNING_KEY": SECRET_KEY,
    "ALGORITHM":"HS256"
}
JWT_EXPIRATION_DELTA_MINUTES=360

''' Database Constants '''

DATABASE_URL = "postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"

API_VERSION="v1"
