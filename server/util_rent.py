import json
import pickle
import numpy as np

__areas = None
__data_columns = None
__model = None

from scipy.special import boxcox, inv_boxcox


def get_estimated_rent(area, sq_mt, bedrooms, bathrooms):
    try:
        loc_index = __data_columns.index(area.lower())  # From a list, we can get the index by simply using .index()
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = boxcox(sq_mt, 0)
    x[1] = boxcox(bedrooms, 0)
    x[2] = boxcox(bathrooms, 0)
    if loc_index >= 0:
        x[loc_index] = 1

    return round(inv_boxcox(__model.predict([x])[0],
                            0))  # this is how we call our model. x is the input in the form of a 2D array


def get_area_names():
    return __areas


def load_saved_artifacts():  # this function takes both artifact files and saves the info into global variables
    print("loading saved artifacts...start")

    global __data_columns
    global __areas

    with open("./artifacts/columns.json", "r") as f:  # with ./ we go one folder up
        __data_columns = json.load(f)[
            "data_columns"]  # We read our json file an import the data and set our variable (list)
        __areas = __data_columns[3:]  # The locations start at index 3

    global __model  # Do not forget to define __model as a global variable

    with open("./artifacts/Madrid_rent_price.pickle", "rb") as f:  # Since is a binary model we will use rb. A
        # binary regression estimates a relationship between one or more explanatory variables and a single output binary variable
        __model = pickle.load(f)

    print("loading saved artifacts...done")


if __name__ == "__main__":
    load_saved_artifacts()
    get_area_names()
    print(get_estimated_rent("Chamartín", 119, 3, 2), "euros per month")
