from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=['GET'])
def random_cafe():
    random_row_data = Cafe.query.order_by(db.func.random()).first()
    if random_row_data:
        # Convert the model instance to a dictionary
        result = {
            "cafe": {
                "id": random_row_data.id,
                "name": random_row_data.name,
                "map_url": random_row_data.map_url,
                "img_url": random_row_data.img_url,
                "location": random_row_data.location,
                "seats": random_row_data.seats,
                "has_toilet": random_row_data.has_toilet,
                "has_wifi": random_row_data.has_wifi,
                "has_sockets": random_row_data.has_sockets,
                "can_take_calls": random_row_data.can_take_calls,
                "coffee_price": random_row_data.coffee_price
            }
        }
        print(jsonify(result))
        return jsonify(result)
    else:
        return jsonify({'error': 'No data found'})


@app.route("/all", methods=['GET'])
def all_cafes():
    all_data = Cafe.query.all()
    if all_data:
        # Convert the model instance to a dictionary
        result = [
            {
                "id": current_row.id,
                "name": current_row.name,
                "map_url": current_row.map_url,
                "img_url": current_row.img_url,
                "location": current_row.location,
                "seats": current_row.seats,
                "has_toilet": current_row.has_toilet,
                "has_wifi": current_row.has_wifi,
                "has_sockets": current_row.has_sockets,
                "can_take_calls": current_row.can_take_calls,
                "coffee_price": current_row.coffee_price
            }
            for current_row in all_data
        ]
        return jsonify({"cafes": result})
    else:
        return jsonify({'error': 'No data found'})


@app.route("/search", methods=['GET'])
def search_cafe():
    search_value = request.args.get("loc")
    if not search_value:
        return jsonify({'error': 'loc parameter is required'})

    # Perform the search using SQLAlchemy
    matching_rows_data = Cafe.query.filter_by(location=search_value).all()

    if matching_rows_data:
        # Convert the model instance to a dictionary
        result = [
            {
                "id": current_row.id,
                "name": current_row.name,
                "map_url": current_row.map_url,
                "img_url": current_row.img_url,
                "location": current_row.location,
                "seats": current_row.seats,
                "has_toilet": current_row.has_toilet,
                "has_wifi": current_row.has_wifi,
                "has_sockets": current_row.has_sockets,
                "can_take_calls": current_row.can_take_calls,
                "coffee_price": current_row.coffee_price
            }
            for current_row in matching_rows_data
        ]
        return jsonify({"cafes": result})
    else:
        return jsonify({'error': {"Not Found": "Sorry, we don't have a cafe at that location"}})


@app.route("/add", methods=['POST'])
def add_record():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'})

    new_record = Cafe(
                        name=data["name"],
                        map_url=data["map_url"],
                        img_url=data["img_url"],
                        location=data["location"],
                        seats=data["seats"],
                        has_toilet=data["has_toilet"],
                        has_wifi=data["has_wifi"],
                        has_sockets=data["has_sockets"],
                        can_take_calls=data["can_take_calls"],
                        coffee_price=data["coffee_price"]
                      )

    try:
        db.session.add(new_record)
        db.session.commit()
        return jsonify({"response": {"success": "Successfully added the new cafe."}})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)})
    finally:
        db.session.close()


@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_record(cafe_id):
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'})

    # Retrieve the existing record from the database
    existing_record = Cafe.query.get(cafe_id)

    if not existing_record:
        return jsonify({"error": {"Not Found": "Sorry a cafe with that id was not found in the database."}}), 404

    # Update the record with the new data
    for key, value in data.items():
        setattr(existing_record, key, value)

    try:
        db.session.commit()
        return jsonify({"success": "Successfully updated the price."}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)})
    finally:
        db.session.close()


@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def delete_row(cafe_id):
    # Retrieve the existing record from the database
    existing_record = Cafe.query.get(cafe_id)
    key_value = request.args.get("api_key")

    if not key_value:
        return jsonify({"error": 'api_key parameter is required'}), 400
    elif key_value != "TopSecretAPIKey":
        return jsonify({"error": "Sorry, that's not allowed. Make sure you have the correct api_key"}), 403
    elif not existing_record:
        return jsonify({"error": {"Not Found": "Sorry a cafe with that id was not found in the database."}}), 404
    else:
        try:
            db.session.delete(existing_record)
            db.session.commit()
            return jsonify({"success": "Record deleted successfully"})
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)})
        finally:
            db.session.close()


if __name__ == '__main__':
    app.run(debug=True)