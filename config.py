from os import getenv

BOT_TOKEN = getenv("BOT_TOKEN", "5775428780:AAFUhpHCqSj2CVr4fghHM80iW3Kq-fTP-L8")
MONGO_URL = getenv("MONGO_URL", "mongodb://ud7kcz6totsvepy86bb2:d4gmTfoBbpzDmNLzItwG@n1-c2-mongodb-clevercloud-customers.services.clever-cloud.com:27017,n2-c2-mongodb-clevercloud-customers.services.clever-cloud.com:27017/b0ojwj6pcvvj30u?replicaSet=rs0")
BOT_ID = getenv("BOT_ID", "5775428780")#token first 10 digits
AI_API_KEY = getenv("AI_API_KEY", "zSCVSEhV1igLyfCR")
AI_ID = int(getenv("AI_ID", "171795"))
