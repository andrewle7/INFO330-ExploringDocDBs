import sqlite3
import sys
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

#function to find pokemon by name
def finding_name(pokemonname):
    return pokemonColl.find_one({"name": pokemonname})

#function to find pokemon with more than x attack
def finding_atk(attack):
    return pokemonColl.find({"attack": {"$gt": attack}})

#function to find pokemon who have certain abilities
def finding_ability(ability):
    return pokemonColl.find({"abilities": ability})

#query to find pokemon for pikachu
def pikachu():
    pikachu = finding_name("Pikachu")
    print(pikachu)

#function that finds pokemon with attack >150
def attack150():
    attacks = finding_atk(150)
    for poke in attacks:
        print(poke)

#function that finds pokemon with overgrow ability
def overgrowabil():
    overgrow = finding_ability("Overgrow")
    for poke in overgrow:
        print(poke)

def main():
    pikachu()
    attack150()
    overgrowabil()

main()






