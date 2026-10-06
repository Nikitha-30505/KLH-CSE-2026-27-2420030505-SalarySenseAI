from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)


# ==================================================
# FILE PATHS
# ==================================================

MODEL_PATH = "models/best_model.pkl"
DATA_PATH = "../datasets/salary_data.csv"


# ==================================================
# LOAD TRAINED MODEL
# ==================================================

model_data = joblib.load(MODEL_PATH)

model = model_data["model"]
encoders = model_data["encoders"]
features = model_data["features"]


# ==================================================
# LOAD DATASET
# ==================================================

df = pd.read_csv(DATA_PATH)


# ==================================================
# OPTIONS FOR PREDICTION FORM
# ==================================================

options = {
    "Gender": sorted(
        df["Gender"].dropna().unique().tolist()
    ),

    "Education_Level": sorted(
        df["Education_Level"].dropna().unique().tolist()
    ),

    "Job_Title": sorted(
        df["Job_Title"].dropna().unique().tolist()
    ),

    "Industry": sorted(
        df["Industry"].dropna().unique().tolist()
    ),

    "Location": sorted(
        df["Location"].dropna().unique().tolist()
    ),

    "Company_Size": sorted(
        df["Company_Size"].dropna().unique().tolist()
    )
}


# ==================================================
# HOME PAGE
# ==================================================

@app.route("/")
def home():
    return render_template("index.html")


# ==================================================
# PREDICTION PAGE
# ==================================================

@app.route("/predict", methods=["GET", "POST"])
def predict():

    # ----------------------------------------------
    # OPEN PREDICTION PAGE
    # ----------------------------------------------

    if request.method == "GET":

        return render_template(
            "predict.html",
            options=options
        )


    # ----------------------------------------------
    # GET FORM DATA
    # ----------------------------------------------

    try:

        age = float(request.form["Age"])

        experience = float(
            request.form["Years_of_Experience"]
        )

        gender = request.form["Gender"]

        education = request.form[
            "Education_Level"
        ]

        job_title = request.form[
            "Job_Title"
        ]

        industry = request.form[
            "Industry"
        ]

        location = request.form[
            "Location"
        ]

        company_size = request.form[
            "Company_Size"
        ]


        # ------------------------------------------
        # CREATE INPUT DATAFRAME
        # ------------------------------------------

        input_data = pd.DataFrame([{

            "Age": age,

            "Gender": gender,

            "Education_Level": education,

            "Job_Title": job_title,

            "Years_of_Experience": experience,

            "Industry": industry,

            "Location": location,

            "Company_Size": company_size

        }])


        # ------------------------------------------
        # CATEGORICAL COLUMNS
        # ------------------------------------------

        categorical_columns = [

            "Gender",

            "Education_Level",

            "Job_Title",

            "Industry",

            "Location",

            "Company_Size"

        ]


        # ------------------------------------------
        # ENCODE CATEGORICAL VALUES
        # ------------------------------------------

        for column in categorical_columns:

            encoder = encoders[column]

            value = input_data[column].iloc[0]


            if value not in encoder.classes_:

                return render_template(
                    "predict.html",
                    options=options,
                    error=(
                        "Selected "
                        + column
                        + " value is not available "
                        "in the trained model."
                    )
                )


            input_data[column] = encoder.transform(
                input_data[column]
            )


        # ------------------------------------------
        # KEEP SAME FEATURE ORDER
        # ------------------------------------------

        input_data = input_data[features]


        # ------------------------------------------
        # MAKE SALARY PREDICTION
        # ------------------------------------------

        prediction = model.predict(
            input_data
        )


        salary = round(
            float(prediction[0]),
            2
        )


        # ------------------------------------------
        # SHOW RESULT
        # ------------------------------------------

        return render_template(

            "result.html",

            salary=salary,

            age=age,

            experience=experience,

            gender=gender,

            education=education,

            job_title=job_title,

            industry=industry,

            location=location,

            company_size=company_size

        )


    # ----------------------------------------------
    # ERROR HANDLING
    # ----------------------------------------------

    except Exception as e:

        return render_template(

            "predict.html",

            options=options,

            error="Prediction error: " + str(e)

        )


# ==================================================
# DASHBOARD
# ==================================================

@app.route("/dashboard")
def dashboard():

    employee_count = len(df)

    average_salary = round(
        df["Salary"].mean(),
        2
    )

    maximum_salary = round(
        df["Salary"].max(),
        2
    )

    minimum_salary = round(
        df["Salary"].min(),
        2
    )


    return render_template(

        "dashboard.html",

        employee_count=employee_count,

        average_salary=average_salary,

        maximum_salary=maximum_salary,

        minimum_salary=minimum_salary

    )


# ==================================================
# ABOUT PAGE
# ==================================================

@app.route("/about")
def about():

    return render_template(
        "about.html"
    )


# ==================================================
# RUN APPLICATION
# ==================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )