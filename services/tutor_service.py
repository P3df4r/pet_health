from flask_pymongo import PyMongo
from bson.objectid import ObjectId

mongo = PyMongo()


class TutorService:
    @staticmethod
    def create_tutor(data):
        tutor_id = mongo.db.pets.insert_one(data).inserted_id
        created_tutor = mongo.db.pets.find_one({"_id": ObjectId(tutor_id)})
        created_tutor['_id'] = str(created_pet['_id'])
        return created_tutor

    @staticmethod
    def get_all_pets_from_tutor():
        pets = mongo.db.pets.find()
        return [PetService.convert_object_id(pet) for pet in pets]

    @staticmethod
    def get_pet_by_id(pet_id):
        pet = mongo.db.pets.find_one({"_id": ObjectId(pet_id)})
        return PetService.convert_object_id(pet)

    @staticmethod
    def update_pet(pet_id, data):
        mongo.db.pets.update_one({"_id": ObjectId(pet_id)}, {"$set": data})
        updated_pet = mongo.db.pets.find_one({"_id": ObjectId(pet_id)})
        if updated_pet:
            updated_pet['_id'] = str(updated_pet['_id'])
        return updated_pet

    @staticmethod
    def delete_pet(pet_id):
        return mongo.db.pets.delete_one({"_id": ObjectId(pet_id)})

    @staticmethod
    def convert_object_id(document):
        if document and '_id' in document:
            document['_id'] = str(document['_id'])
        return document
    

    