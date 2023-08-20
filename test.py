import requests

def test_predict_endpoint():
    # URL for the local Flask app when it's run locally
    local_url = "http://localhost:5000/predict"

    # Sample input data for testing
    data = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }

    response = requests.post(local_url, json=data)
    prediction = response.json()

    # Assuming the model returns a class label as prediction
    assert prediction in ['setosa', 'versicolor', 'virginica'], f"Unexpected prediction: {prediction}"

if __name__ == "__main__":
    test_predict_endpoint()
    print("All tests passed!")
