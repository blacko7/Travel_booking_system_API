from flask import request, jsonify
from app import app, db
from models import User, Flight, Booking
from flask_jwt_extended import create_access_token, jwt_required

# Register endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User(username=data['username'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify(message="User registered successfully"), 201

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        token = create_access_token(identity=user.id)
        return jsonify(access_token=token), 200
    return jsonify(message="Invalid credentials"), 401

# Get available flights
@app.route('/flights', methods=['GET'])
@jwt_required()
def get_flights():
    flights = Flight.query.all()
    return jsonify([flight.to_dict() for flight in flights]), 200

# Book a flight
@app.route('/bookings', methods=['POST'])
@jwt_required()
def book_flight():
    data = request.get_json()
    # Assume booking logic here
    return jsonify(message="Flight booked successfully"), 201

# Cancel a booking
@app.route('/bookings/<int:id>', methods=['DELETE'])
@jwt_required()
def cancel_booking(id):
    booking = Booking.query.get_or_404(id)
    db.session.delete(booking)
    db.session.commit()
    return jsonify(message="Booking cancelled"), 200
