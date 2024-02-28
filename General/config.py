from environs import Env

env = Env()
env.read_env()

SECRET_KEY = env.str("SECRET_KEY")
ALGORITHM = env.str("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = env.int("ACCESS_TOKEN_EXPIRE_MINUTES")
COOKIE_NAME = env.str("COOKIE_NAME")

host = env.str("HOST")
port = env.int("PORT")

db_host = env.str("DB_HOST")
db_port = env.int("DB_PORT")
db_username = env.str("DB_USERNAME")
db_password = env.str("DB_PASSWORD")
db_name = env.str("DB_NAME")

