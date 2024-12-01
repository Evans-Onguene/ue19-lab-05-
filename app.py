import requests


def get_api():
    url = "https://v2.jokeapi.dev/joke/Any?type=single"
    try:
        # Send GET request to the API
        response = requests.get(url, timeout=5)

        # Check if the request was successful
        if response.status_code == 200:
            joke_data = response.json()
            return joke_data.get('joke', "No joke found in the response.")
        else:
            return f"Failed to retrieve the API. Status Code: {response.status_code}"

    except requests.exceptions.Timeout:
        return "Request timed out. Please try again later."

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"


if __name__ == '__main__':
    api_response = get_api()
    print(api_response)
