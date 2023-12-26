# Managing Images with GPT-4 with Vision (GPT-4V)

This document provides an overview of how to manage images when using GPT-4 with Vision (GPT-4V).

## State Management

The Chat Completions API, which GPT-4V uses, is not stateful. This means that it does not retain any information about previous requests. Therefore, every time you make a request, you need to pass the images again, even if they were used in the previous request.

## Image Processing and Deletion

Once the images are processed, they are deleted and not retained by OpenAI. This is an important aspect of OpenAI's commitment to user privacy. Therefore, if you need to refer to the results of a previous image processing request, you should store the results on your end.

## Example

Here is an example of how to manage images using the Python scripts provided in this repository:

```python
from uploading_base64_encoded_images import upload_image
from handling_multiple_image_inputs import upload_multiple_images

# Path to your image
image_path = "path_to_your_image.jpg"

# Upload a single image
upload_image(image_path)

# Paths to multiple images
image_paths = ["path_to_image1.jpg", "path_to_image2.jpg"]

# Upload multiple images
upload_multiple_images(image_paths)
```

In the above example, the `upload_image` function is used to upload a single image, and the `upload_multiple_images` function is used to upload multiple images. Note that these functions encode the images in base64 format before uploading.

Remember to replace `"path_to_your_image.jpg"`, `"path_to_image1.jpg"`, and `"path_to_image2.jpg"` with the actual paths to your images.

For more information on how to encode and upload images, refer to the [uploading_base64_encoded_images.py](uploading_base64_encoded_images.py) and [handling_multiple_image_inputs.py](handling_multiple_image_inputs.py) scripts.

## Limitations and Considerations

For detailed information about the limitations and considerations of GPT-4V, please refer to the [limitations_and_considerations.md](limitations_and_considerations.md) file in this repository.

## FAQs

For frequently asked questions about GPT-4V, refer to the [FAQs](faqs.md) section.
