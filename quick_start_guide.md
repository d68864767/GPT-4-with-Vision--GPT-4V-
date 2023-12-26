# Quick Start Guide

This guide provides a step-by-step process on how to utilize the image processing capabilities of GPT-4 with Vision (GPT-4V).

## Image Inputs

Images can be passed to GPT-4V via links or as base64 encoded directly in the request. They can be included in user, system, and assistant messages (except the first system message).

## General Questions

GPT-4V excels at answering general questions about the contents of an image. However, it may struggle with specific spatial queries.

## Uploading Base64 Encoded Images

Images stored locally can be passed in base64 encoded format. Refer to the Python script [uploading_base64_encoded_images.py](uploading_base64_encoded_images.py) in this repository for an example of how to encode and upload a local image.

## Handling Multiple Image Inputs

The API can process multiple images, using all to answer a given question. A Python script example [handling_multiple_image_inputs.py](handling_multiple_image_inputs.py) is provided in this repository to demonstrate handling multiple images.

## Detail Levels in Image Understanding

You can choose between low, high, or auto detail levels, affecting how the model processes images.

- **Low Detail**: Uses a lower resolution and token budget for faster responses.
- **High Detail**: Provides detailed crops of input images for a higher token budget.

## Managing Images

The Chat Completions API is not stateful; images need to be passed with each request. After processing, images are deleted and not retained by OpenAI.

## Limitations and Considerations

For detailed information about the limitations and considerations of GPT-4V, please refer to the [limitations_and_considerations.md](limitations_and_considerations.md) file in this repository.

## FAQs

For frequently asked questions about GPT-4V, refer to the [FAQs](faqs.md) section.

GPT-4 with Vision represents a significant advancement in AI capabilities, merging visual and textual understanding in a single model. Start integrating and experimenting with this powerful feature in your applications today.
