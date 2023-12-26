```python
import base64
import requests

def encode_image(image_path):
    """
    Function to encode an image to base64 format.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def upload_image(image_path):
    """
    Function to upload a base64 encoded image to GPT-4V.
    """
    encoded_image = encode_image(image_path)

    # Define the API endpoint
    url = "https://api.openai.com/v1/engines/gpt-4-vision-preview/completions"

    # Define the headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_OPENAI_API_KEY"
    }

    # Define the data
    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is in this image?", "data": {"image": {"base64": encoded_image}}}
        ]
    }

    # Make the POST request
    response = requests.post(url, headers=headers, json=data)

    # Check the status code
    if response.status_code == 200:
        # If successful, print the response
        print(response.json())
    else:
        # If unsuccessful, print the error
        print(f"Error: {response.status_code}, {response.text}")

if __name__ == "__main__":
    # Replace with the path to your image
    image_path = "path_to_your_image.jpg"
    upload_image(image_path)
```
