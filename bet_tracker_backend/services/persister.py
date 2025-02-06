"""Module for persisting data into Postgres SQL"""
import psycopg2
from bet_tracker_backend.models import sports_data_io

class Persister:
    def __init__(self, database: str, user: str, host: str, password: str, port: str):
        self.database = database
        self.user = user
        self.host = host
        self.password = password
        self.port = port

    
    
    def set_player_data(self, )
        
