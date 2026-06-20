from dotenv import load_dotenv
import os

load_dotenv()

print("Database Name:", os.getenv("DATABASE_NAME"))
print("Database Path:", os.getenv("DATABASE_PATH"))
print("Data Folder:", os.getenv("DATA_FOLDER"))
print("Output Folder:", os.getenv("OUTPUT_FOLDER"))
print("Log Level:", os.getenv("LOG_LEVEL"))