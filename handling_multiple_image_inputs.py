```python
import base64
import requests

def encode_image(image_path):
    """
    Function to encode an image to base64 format.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def upload_multiple_images(image_paths):
    """
    Function to upload multiple base64 encoded images to GPT-4V.
    """
    encoded_images = [encode_image(image_path) for image_path in image_paths]

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
            {"role": "user", "content": "What is in these images?"}
        ]
    }

    # Add each image to the messages
    for encoded_image in encoded_images:
        data["messages"].append({"role": "assistant", "data": {"image": {"base64": encoded_image}}})

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
    # Replace with the paths to your images
    image_paths = ["path_to_your_image1.jpg", "path_to_your_image2.jpg"]
    upload_multiple_images(image_paths)
```
