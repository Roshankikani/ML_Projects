from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model from the pickle file
with open('diamond_prcie (1).pkl', 'rb') as file:
    model = pickle.load(file)

# Render the HTML form template
@app.route('/')
def home():
    return render_template('index.html')


# Handle the form submission and make predictions
@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":

        # carat
        carat = float(request.form["carat"])

        # Cut
        cut = request.form['cut']
        if (cut == 'Ideal'):
            cut_Ideal = 1
            cut_Premium = 0
            cut_Good = 0
            cut_Very_Good = 0
            cut_Fair = 0

        elif (cut == 'Premium'):
            cut_Ideal = 0
            cut_Premium = 1
            cut_Good = 0
            cut_Very_Good = 0
            cut_Fair = 0

        elif (cut == 'Good'):
            cut_Ideal = 0
            cut_Premium = 0
            cut_Good = 1
            cut_Very_Good = 0
            cut_Fair = 0

        elif (cut == 'Very Good'):
            cut_Ideal = 0
            cut_Premium = 0
            cut_Good = 0
            cut_Very_Good = 1
            cut_Fair = 0

        elif (cut == 'Fair'):
            cut_Ideal = 0
            cut_Premium = 0
            cut_Good = 0
            cut_Very_Good = 0
            cut_Fair = 1

        color = request.form["color"]
        if (color == 'E'):
            color_D = 0
            color_E = 1
            color_F = 0
            color_G = 0
            color_H = 0
            color_I = 0
            color_J = 0

        elif (color == 'j'):
            color_D = 0
            color_E = 0
            color_F = 0
            color_G = 0
            color_H = 0
            color_I = 0
            color_J = 1

        elif (color == 'H'):
            color_D = 0
            color_E = 0
            color_F = 0
            color_G = 0
            color_H = 1
            color_I = 0
            color_J = 0

        elif (color == 'F'):
            color_D = 0
            color_E = 0
            color_F = 1
            color_G = 0
            color_H = 0
            color_I = 0
            color_J = 0

        elif (color == 'G'):
            color_D = 0
            color_E = 0
            color_F = 0
            color_G = 1
            color_H = 0
            color_I = 0
            color_J = 0

        elif (color == 'D'):
            color_D = 1
            color_E = 0
            color_F = 0
            color_G = 0
            color_H = 0
            color_I = 0
            color_J = 0

        clarity = request.form["clarity"]
        if (clarity == 'SI2'):
            clarity_I1 = 0
            clarity_IF = 0
            clarity_SI1 = 0
            clarity_SI2 = 1
            clarity_VS1 = 0
            clarity_VS2 = 0
            clarity_VVS1 = 0
            clarity_VVS2 = 0

        elif (clarity == 'SI1'):
            clarity_I1 = 0
            clarity_IF = 0
            clarity_SI1 = 1
            clarity_SI2 = 0
            clarity_VS1 = 0
            clarity_VS2 = 0
            clarity_VVS1 = 0
            clarity_VVS2 = 0

        elif (clarity == 'VS1'):
            clarity_I1 = 0
            clarity_IF = 0
            clarity_SI1 = 0
            clarity_SI2 = 0
            clarity_VS1 = 1
            clarity_VS2 = 0
            clarity_VVS1 = 0
            clarity_VVS2 = 0

        elif (clarity == 'VS2'):
            clarity_I1 = 0
            clarity_IF = 0
            clarity_SI1 = 0
            clarity_SI2 = 0
            clarity_VS1 = 0
            clarity_VS2 = 1
            clarity_VVS1 = 0
            clarity_VVS2 = 0

        elif (clarity == 'VVS2'):
            clarity_I1 = 0
            clarity_IF = 0
            clarity_SI1 = 0
            clarity_SI2 = 0
            clarity_VS1 = 0
            clarity_VS2 = 0
            clarity_VVS1 = 0
            clarity_VVS2 = 1

        elif (clarity == 'VVS1'):
            clarity_I1 = 0
            clarity_IF = 0
            clarity_SI1 = 0
            clarity_SI2 = 0
            clarity_VS1 = 0
            clarity_VS2 = 0
            clarity_VVS1 = 1
            clarity_VVS2 = 0

        elif (clarity == 'I1'):
            clarity_I1 = 1
            clarity_IF = 0
            clarity_SI1 = 0
            clarity_SI2 = 0
            clarity_VS1 = 0
            clarity_VS2 = 0
            clarity_VVS1 = 0
            clarity_VVS2 = 0

        elif (clarity == 'IF'):
            clarity_I1 = 0
            clarity_IF = 1
            clarity_SI1 = 0
            clarity_SI2 = 0
            clarity_VS1 = 0
            clarity_VS2 = 0
            clarity_VVS1 = 0
            clarity_VVS2 = 0

        depth = float(request.form["depth"])

        table = float(request.form["table"])

        x = float(request.form["x"])

        y = float(request.form["y"])

        z = float(request.form["z"])




        prediction = model.predict([[
            carat,
            cut_Ideal,
            cut_Premium,
            cut_Good,
            cut_Very_Good,
            cut_Fair,
            color_D,
            color_E,
            color_F,
            color_G,
            color_H,
            color_I,
            color_J,
            clarity_I1,
            clarity_IF,
            clarity_SI1,
            clarity_SI2,
            clarity_VS1,
            clarity_VS2,
            clarity_VVS1,
            clarity_VVS2,
            depth,
            table,
            x,
            y,
            z,
        ]])

        # Display the prediction result
        return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
