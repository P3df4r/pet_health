from flask import Blueprint, request, jsonify
from models.vet import VetModelModel
from services.pet_service import PetService

vet_bp = Blueprint('vet', __name__)

@vet_bp.route('/pets', methods=['POST'])

@vet_bp.route('/pets', methods=['GET'])
def get_all_pets():
    pets = PetService.get_all_pets()
    return jsonify(pets), 200


@vet_bp.route('/pets/<pet_id>', methods=['GET'])
def get_pet_by_id(pet_id):
    pet = PetService.get_pet_by_id(pet_id)
    if pet:
        return jsonify(pet), 200
    return jsonify({"error": "Pet not found"}), 404


@vet_bp.route('/pets/<pet_id>', methods=['PUT'])
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

