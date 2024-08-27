from flask import Blueprint, request, jsonify
from models.pet import PetModel
from services.pet_service import PetService

pet_bp = Blueprint('pet', __name__)


@pet_bp.route('/pets', methods=['POST'])
def create_pet():
    data = request.get_json()
    try:
        pet = PetModel(**data)
        created_pet = PetService.create_pet(pet.dict())
        return jsonify(created_pet), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@pet_bp.route('/pets', methods=['GET'])
def get_all_pets():
    pets = PetService.get_all_pets()
    return jsonify(pets), 200


@pet_bp.route('/pets/<pet_id>', methods=['GET'])
def get_pet_by_id(pet_id):
    pet = PetService.get_pet_by_id(pet_id)
    if pet:
        return jsonify(pet), 200
    return jsonify({"error": "Pet not found"}), 404


@pet_bp.route('/pets/<pet_id>', methods=['PUT'])
def update_pet(pet_id):
    data = request.get_json()
    try:
        pet = PetModel(**data)
        updated_pet = PetService.update_pet(pet_id, pet.dict())
        if updated_pet:
            return jsonify(updated_pet), 200
        return jsonify({"error": "Pet not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@pet_bp.route('/pets/<pet_id>', methods=['DELETE'])
def delete_pet(pet_id):
    result = PetService.delete_pet(pet_id)
    if result.deleted_count:
        return jsonify({"message": "Pet deleted"}), 200
    return jsonify({"error": "Pet not found"}), 404
