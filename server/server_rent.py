from flask import Flask, request, jsonify
import util_rent

app = Flask(__name__)


@app.route("/get_area_names")  # We need two routines: One for the locations(in util file)
def get_area_names():  # this will return all the locations
    response = jsonify({"Areas": util_rent.get_area_names()})  # Returning a response that contain the locations
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route("/predict_home_rent", methods=["POST"])  # We need two routines: One for the locations(in util file)
def predict_home_rent():
    sq_mt = float(request.form["sq_mt"])
    area = str(request.form["area"])
    bedrooms = float(request.form["bedrooms"])
    bathrooms = float(request.form["bathrooms"])

    response = jsonify({"estimated_rent": util_rent.get_estimated_rent(area, sq_mt, bedrooms, bathrooms)})

    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util_rent.load_saved_artifacts()
    app.run()
