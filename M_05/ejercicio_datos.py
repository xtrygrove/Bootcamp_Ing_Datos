import warnings
from cryptography.utils import CryptographyDeprecationWarning
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)

from pymongo import MongoClient
import pandas as pd

# Conexión a MongoDB
client = MongoClient("mongodb+srv://admin:Bootc%40mp_2025@cluster0.ww4cl7o.mongodb.net/?retryWrites=true&w=majority")
db = client["demo_db"]
collection = db["tickets_soporte"]

# Verificar número de documentos
total = collection.count_documents({})
print(f"\nTotal de documentos en 'tickets_soporte': {total}")

if total > 0:
    # Leer los primeros 10
    cursor = collection.find().limit(100)
    df = pd.DataFrame(cursor)
    
    print("\nPrimeros 10 documentos:\n")
    print(df.head(10).to_string(index=False))