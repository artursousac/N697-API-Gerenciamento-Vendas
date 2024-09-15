from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

uri = f"mongodb+srv://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASS")}@cluster0.brp8cuh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

db = client.GerenciamentoDeEventos

collection_Organizadores = db["Organizadores"]

collection_Participantes = db["Participantes"]

