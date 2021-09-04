import ast
import codecs
import numpy as np
from flask import Flask, jsonify, request
from tensorflow import keras

f = codecs.open('db.txt', 'r', "utf_8_sig")
ff = f.read()
items = ast.literal_eval(ff)


def tex_to_int(st):
    text = ":".join("{:02x}".format(ord(c)) for c in st)
    return ''.join(str(int(h, 16)) for h in text.split(':'))


def correct_data(row):
    if row[5] == 'Moscow':
        row[5] = '1'
    elif row[5] == 'Petersburg':
        row[5] = '2'

    if row[14] == 'M':
        row[14] = '0'
    elif row[14] == 'F':
        row[14] = '1'

    row[8] = items[0][row[8]]
    row[9] = items[1][row[9]]
    row[26] = items[3][row[26]]

    if row[24] == "N":
        row[24] = '-1'
    if row[13] == 'N':
        row[13] = '-1'

    row[15] = tex_to_int(row[15])
    row[16] = tex_to_int(row[16])
    row[17] = tex_to_int(row[17])
    row[18] = tex_to_int(row[18])

    return row


def prediction(test):

    x = correct_data(test)
    x = np.array(x, float)
    mean = x.mean(axis=0)
    std = x.std(axis=0)
    x -= mean
    x /= std
    x_test = np.array([x], float)
    model = keras.models.load_model('16_model_2.h5')
    pred = model.predict(x_test)
    return str(pred[0][0])


app = Flask(__name__)


@app.route('/', methods=['POST'])
def get_data():

    check = True
    POLICY_ID = request.get_json().get("POLICY_ID")
    if POLICY_ID is None:
        print("POLICY_ID")
        check = False
    POLICY_BEGIN_MONTH = request.get_json().get("POLICY_BEGIN_MONTH")
    if POLICY_BEGIN_MONTH is None:
        check = False
    POLICY_END_MONTH = request.get_json().get("POLICY_END_MONTH")
    if POLICY_END_MONTH is None:
        check = False
    POLICY_SALES_CHANNEL = request.get_json().get("POLICY_SALES_CHANNEL")
    if POLICY_SALES_CHANNEL is None:
        check = False
    POLICY_SALES_CHANNEL_GROUP = request.get_json().get("POLICY_SALES_CHANNEL_GROUP")
    if POLICY_SALES_CHANNEL_GROUP is None:
        check = False
    POLICY_BRANCH = request.get_json().get("POLICY_BRANCH")
    if POLICY_BRANCH is None:
        check = False
    POLICY_MIN_AGE = request.get_json().get("POLICY_MIN_AGE")
    if POLICY_MIN_AGE is None:
        check = False
    POLICY_MIN_DRIVING_EXPERIENCE = request.get_json().get("POLICY_MIN_DRIVING_EXPERIENCE")
    if POLICY_MIN_DRIVING_EXPERIENCE is None:
        check = False
    VEHICLE_MAKE = request.get_json().get("VEHICLE_MAKE")
    if VEHICLE_MAKE is None:
        check = False
    VEHICLE_MODEL = request.get_json().get("VEHICLE_MODEL")
    if VEHICLE_MODEL is None:
        check = False
    VEHICLE_ENGINE_POWER = request.get_json().get("VEHICLE_ENGINE_POWER")
    if VEHICLE_ENGINE_POWER is None:
        check = False
    VEHICLE_IN_CREDIT = request.get_json().get("VEHICLE_IN_CREDIT")
    if VEHICLE_IN_CREDIT  is None:
        check = False
    VEHICLE_SUM_INSURED = request.get_json().get("VEHICLE_SUM_INSURED")
    if VEHICLE_SUM_INSURED is None:
        check = False
    POLICY_INTERMEDIARY = request.get_json().get("POLICY_INTERMEDIARY")
    if POLICY_INTERMEDIARY is None:
        check = False
    INSURER_GENDER = request.get_json().get("INSURER_GENDER")
    if INSURER_GENDER is None:
        check = False
    POLICY_CLM_N = request.get_json().get("POLICY_CLM_N")
    if POLICY_CLM_N  is None:
        check = False
    POLICY_CLM_GLT_N = request.get_json().get("POLICY_CLM_GLT_N")
    if POLICY_CLM_GLT_N is None:
        check = False
    POLICY_PRV_CLM_N = request.get_json().get("POLICY_PRV_CLM_N")
    if POLICY_PRV_CLM_N is None:
        check = False
    POLICY_PRV_CLM_GLT_N = request.get_json().get("POLICY_PRV_CLM_GLT_N")
    if POLICY_PRV_CLM_GLT_N is None:
        check = False
    CLIENT_HAS_DAGO = request.get_json().get("CLIENT_HAS_DAGO")
    if CLIENT_HAS_DAGO is None:
        check = False
    CLIENT_HAS_OSAGO = request.get_json().get("CLIENT_HAS_OSAGO")
    if CLIENT_HAS_OSAGO is None:
        check = False
    POLICY_COURT_SIGN = request.get_json().get("POLICY_COURT_SIGN")
    if POLICY_COURT_SIGN  is None:
        check = False
    CLAIM_AVG_ACC_ST_PRD = request.get_json().get("CLAIM_AVG_ACC_ST_PRD")
    if CLAIM_AVG_ACC_ST_PRD is None:
        check = False
    POLICY_HAS_COMPLAINTS = request.get_json().get("POLICY_HAS_COMPLAINTS")
    if POLICY_HAS_COMPLAINTS is None:
        check = False
    POLICY_YEARS_RENEWED_N = request.get_json().get("POLICY_YEARS_RENEWED_N")
    if POLICY_YEARS_RENEWED_N is None:
        check = False
    POLICY_DEDUCT_VALUE = request.get_json().get("POLICY_DEDUCT_VALUE")
    if POLICY_DEDUCT_VALUE is None:
        check = False
    CLIENT_REGISTRATION_REGION = request.get_json().get("CLIENT_REGISTRATION_REGION")
    if CLIENT_REGISTRATION_REGION is None:
        check = False
    POLICY_PRICE_CHANGE = request.get_json().get("POLICY_PRICE_CHANGE")
    if POLICY_PRICE_CHANGE is None:
        check = False
    if check:
        arr = [POLICY_ID, POLICY_BEGIN_MONTH, POLICY_END_MONTH, POLICY_SALES_CHANNEL, POLICY_SALES_CHANNEL_GROUP,
               POLICY_BRANCH, POLICY_MIN_AGE, POLICY_MIN_DRIVING_EXPERIENCE, VEHICLE_MAKE, VEHICLE_MODEL,
               VEHICLE_ENGINE_POWER, VEHICLE_IN_CREDIT, VEHICLE_SUM_INSURED, POLICY_INTERMEDIARY, INSURER_GENDER,
               POLICY_CLM_N,POLICY_CLM_GLT_N, POLICY_PRV_CLM_N, POLICY_PRV_CLM_GLT_N, CLIENT_HAS_DAGO, CLIENT_HAS_OSAGO,
               POLICY_COURT_SIGN, CLAIM_AVG_ACC_ST_PRD, POLICY_HAS_COMPLAINTS, POLICY_YEARS_RENEWED_N,
               POLICY_DEDUCT_VALUE, CLIENT_REGISTRATION_REGION, POLICY_PRICE_CHANGE]

        res = prediction(arr)
        return jsonify({"prediction_result": res})
    else:
        return "No parameters passed"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
