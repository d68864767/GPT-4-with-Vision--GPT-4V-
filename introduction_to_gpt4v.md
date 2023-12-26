# Introduction to GPT-4 with Vision (GPT-4V)

GPT-4 with Vision (GPT-4V) is a groundbreaking extension of OpenAI's GPT-4 model. This new feature enables the model to interpret images along with text, expanding beyond the text-only input limitation of the previous versions.

## Capability

GPT-4V can process images and answer questions about them. This new capability is available to all developers with GPT-4 access via the `gpt-4-vision-preview` model in the Chat Completions API. Please note that the Assistants API does not support image inputs yet.

## Behavior

The behavior of GPT-4V is slightly different from GPT-4 Turbo due to an automatically inserted system message. However, it is equally proficient in text tasks as GPT-4 Turbo, with the added advantage of vision capabilities.

## Limitations

Certain parameters like `message.name`, functions/tools, and `response_format` are not supported in GPT-4V. Also, a lower default `max_tokens` is set, which can be overridden if necessary.

## Getting Started

To get started with GPT-4V, refer to the [Quick Start Guide](quick_start_guide.md). This guide provides a step-by-step process on how to pass images via links or as base64 encoded directly in the request.

## Examples

This repository includes Python scripts demonstrating how to encode and upload a local image ([uploading_base64_encoded_images.py](uploading_base64_encoded_images.py)) and how to handle multiple images ([handling_multiple_image_inputs.py](handling_multiple_image_inputs.py)).

For more detailed information about the capabilities, limitations, and considerations of GPT-4V, please refer to the respective markdown files in this repository.

## FAQs

For frequently asked questions about GPT-4V, refer to the [FAQs](faqs.md) section.
