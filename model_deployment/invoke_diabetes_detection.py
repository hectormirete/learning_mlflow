import requests

payload = '[{"age":0.03807591, "sex": 0.05068012, "bmi": 0.06169621, "bp": 0.02187235, "s1": -0.0442235, "s2": -0.03482076, "s3": -0.04340085, "s4": -0.00259226, "s5": 0.01990842, "s6": -0.01764613}]'
headers = {'Content-Type': 'application/json; format=pandas-records'}
request_uri = 'http://127.0.0.1:5000/invocations'
expected_result = 151.0

if __name__ == '__main__':
    try:
        response = requests.post(url=request_uri, data=payload, headers=headers)
        print(response)
        print('Prediction:', response.content)
        print('Expected result:', expected_result)
    except Exception as exception:
        raise(exception)
