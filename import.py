import sqlite3
import sys
from pymongo import MongoClient
import ast

#connect to mongo coll
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

pokemonColl.delete_many({})
# connect to pokemon sqlite database
conn = sqlite3.connect("/Users/andrewle/Documents/School/INFO330/INFO330-ExploringDocDBs/pokemon.sqlite")
crsr = conn.cursor()

#select all rows that need it
generalquery = crsr.execute(""" 
    SELECT
        name, pokedex_number, type1, type2, hp, attack, defense, speed, sp_attack, sp_defense, abilities
    FROM imported_pokemon_data
""")

pokemonRows = generalquery.fetchall()
pokemonCols = []
for row in pokemonRows:
    pokemon = {
        "_id": row[1],
        "name": row[0],
        "pokedex_number": int(row[1]),
        "types": [row[2]],
        "hp": int(row[4]),
        "attack": int(row[5]),
        "defense": int(row[6]),
        "speed": int(row[7]),
        "sp_attack": int(row[8]),
        "sp_defense": int(row[9]),
        "abilities": ast.literal_eval(row[10])
    }
    if row[3]:
        pokemon["types"].append(row[3])
    
    pokemonColl.insert_one(pokemon)

