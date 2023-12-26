# Limitations and Considerations

While GPT-4 with Vision (GPT-4V) represents a significant advancement in AI capabilities, it's important to understand its limitations and considerations for effective usage.

## Scope

GPT-4V is designed to interpret general images and answer questions about them. However, it is not suitable for specialized tasks like interpreting medical images or other highly specialized visual tasks. For such tasks, specialized models and algorithms are recommended.

## Performance

GPT-4V may struggle with certain types of image inputs. These include:

- Non-Latin text: The model may have difficulty interpreting text in non-Latin scripts.
- Small text: Text that is too small may not be accurately interpreted by the model.
- Rotated images: Images that are not upright may pose a challenge for the model.
- Spatial reasoning: The model may struggle with specific spatial queries about the image.

## Costs

The usage of GPT-4V is charged in tokens based on the size and detail level of the images. Larger and more detailed images will consume more tokens, which may increase the cost of using the service.

## Rate Limits

Images are processed at the token level and count towards the total tokens per minute (TPM) limit. Exceeding the TPM limit may result in throttling of the service.

## Image Processing and Deletion

After processing, images are deleted and not retained by OpenAI. This is in line with OpenAI's commitment to user privacy and data security.

For more detailed information about the capabilities, limitations, and considerations of GPT-4V, please refer to the respective markdown files in this repository. For frequently asked questions about GPT-4V, refer to the [FAQs](faqs.md) section.
