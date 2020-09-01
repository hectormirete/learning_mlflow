from mlflow import pyfunc
import pandas as pd

model_name = 'diabetes_detection'
stage = 'Production'

model = pyfunc.load_model(
    model_uri=f"models:/{model_name}/{stage}"
)

data = {"age": [0.03807591],
        "sex": [0.05068012],
        "bmi": [0.06169621],
        "bp": [0.02187235],
        "s1": [-0.0442235],
        "s2": [-0.03482076],
        "s3": [-0.04340085],
        "s4": [-0.00259226],
        "s5": [0.01990842],
        "s6": [-0.01764613]}
input_data = pd.DataFrame(data=data)

print(model.predict(input_data))