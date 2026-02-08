import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.conn = pyodbc.connect(
            f"DRIVER={{SQL Server}};"
            f"SERVER={os.getenv('DB_SERVER')};"
            f"DATABASE={os.getenv('DB_DATABASE')};"
            f"UID={os.getenv('DB_USERNAME')};"
            f"PWD={os.getenv('DB_PASSWORD')}"
        )
        self.cursor = self.conn.cursor()

    def insert(self, qr_code):
        self.cursor.execute(
            "INSERT INTO Production (QrCode) VALUES (?)",
            qr_code
        )
        self.conn.commit()
