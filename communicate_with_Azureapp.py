import requests
import json

if __name__ == "__main__":

    url = "https://perkierstudentscoreprediction.azurewebsites.net/predict"

    data_1 = {"gender": "female",
              "race_ethnicity": 'group A',
              "parental_level_of_education": "bachelor's degree",
              "lunch": 'standard',
              "test_preparation_course": 'completed',
              "reading_score": 55,
              "writing_score": 79}

    data_2 = {"gender": "male",
              "race_ethnicity": 'group E',
              "parental_level_of_education": "master's degree",
              "lunch": 'free/reduced',
              "test_preparation_course": 'completed',
              "reading_score": 15,
              "writing_score": 22}

    data_3 = {"gender": "male",
              "race_ethnicity": 'group A',
              "parental_level_of_education": "bachelor's degree",
              "lunch": 'free/reduced',
              "test_preparation_course": 'completed',
              "reading_score": 95,
              "writing_score": 92}

    # Make a POST request to the API endpoint
    try:
        response = requests.post(url, json=data_1)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            predictions = response.json()
            print("Model Predictions:", predictions)
        else:
            print("Error:", response.status_code, response.text)

    except requests.exceptions.RequestException as e:
        print("Error:", e)

    quit()


