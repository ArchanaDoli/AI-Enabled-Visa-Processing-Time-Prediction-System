import pandas as pd
import joblib

model = joblib.load("rf_model.pkl")
model_columns = joblib.load("model_columns.pkl")

def preprocess_input(data):

    # Create empty dataframe with all model columns
    input_df = pd.DataFrame(columns=model_columns)
    input_df.loc[0] = 0

    # Set month
    input_df["Application_Month"] = data["month"]

    # Set country
    country_col = "Applicant_Country_" + data["country"]
    if country_col in input_df.columns:
        input_df[country_col] = 1

    # Set visa type
    visa_col = "Visa_Type_" + data["visa_type"]
    if visa_col in input_df.columns:
        input_df[visa_col] = 1

    # Set processing office
    office_col = "Processing_Office_" + data["office"]
    if office_col in input_df.columns:
        input_df[office_col] = 1

    return input_df


def predict_processing_time(input_data):

    processed_data = preprocess_input(input_data)
    prediction = model.predict(processed_data)

    return round(prediction[0], 2)