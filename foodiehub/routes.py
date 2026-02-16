from flask import Blueprint, request, jsonify
from models import db, User, Restaurant, Dish, Order
from flask_jwt_extended import create_access_token, jwt_required

api = Blueprint("api", __name__)

# ---------- USER ----------

@api.route("/register", methods=["POST"])
def register():
    data = request.json

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"msg": "User exists"}), 409

    user = User(
        name=data["name"],
        email=data["email"],
        password=data["password"]
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User created"}), 201


@api.route("/login", methods=["POST"])
def login():
    data = request.json

    user = User.query.filter_by(
        email=data["email"],
        password=data["password"]
    ).first()

    if not user:
        return jsonify({"msg": "Invalid credentials"}), 401

    token = create_access_token(identity=str(user.id))

    return jsonify(access_token=token)


# ---------- RESTAURANT ----------

@api.route("/restaurants", methods=["POST"])
@jwt_required()
def add_restaurant():
    data = request.json

    restaurant = Restaurant(
        name=data["name"],
        location=data["location"]
    )

    db.session.add(restaurant)
    db.session.commit()

    return jsonify({"msg": "Restaurant added"}), 201


@api.route("/restaurants", methods=["GET"])
def get_restaurants():
    restaurants = Restaurant.query.filter_by(is_active=True).all()

    result = [
        {"id": r.id, "name": r.name, "location": r.location}
        for r in restaurants
    ]

    return jsonify(result)


# ---------- DISH ----------

@api.route("/dishes", methods=["POST"])
@jwt_required()
def add_dish():
    data = request.json

    dish = Dish(
        name=data["name"],
        price=data["price"],
        restaurant_id=data["restaurant_id"]
    )

    db.session.add(dish)
    db.session.commit()

    return jsonify({"msg": "Dish added"}), 201


# ---------- ORDER ----------

@api.route("/orders", methods=["POST"])
@jwt_required()
def place_order():
    data = request.json

    order = Order(
        user_id=data["user_id"],
        restaurant_id=data["restaurant_id"]
    )

    db.session.add(order)
    db.session.commit()

    return jsonify({"msg": "Order placed"}), 201


@api.route("/orders/<int:user_id>", methods=["GET"])
@jwt_required()
def get_orders(user_id):
    orders = Order.query.filter_by(user_id=user_id).all()

    result = [{"id": o.id, "restaurant_id": o.restaurant_id} for o in orders]

    return jsonify(result)

