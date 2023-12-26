# Detail Levels in Image Understanding

GPT-4 with Vision (GPT-4V) provides the flexibility to control the level of detail in image understanding. This feature allows you to choose between low, high, or auto detail levels, affecting how the model processes images.

## Low Detail

In the low detail setting, GPT-4V uses a lower resolution and token budget for image processing. This results in faster responses but may compromise on the level of detail in the image understanding.

## High Detail

The high detail setting provides detailed crops of input images for a higher token budget. This setting is suitable for tasks that require a more detailed understanding of the image contents.

## Auto Detail

The auto detail setting allows GPT-4V to automatically decide the level of detail based on the image and the task at hand. This setting provides a balance between speed and detail in image understanding.

## Choosing the Right Detail Level

The choice of detail level depends on the specific requirements of your task. If speed is a priority and the task does not require a detailed understanding of the image, the low detail setting may be sufficient. On the other hand, if the task requires a detailed understanding of the image, the high detail setting would be more appropriate. The auto detail setting can be used when you are unsure about the level of detail required or when you want GPT-4V to automatically adjust the detail level based on the task.

Remember, the detail level affects the token budget and processing time. Therefore, it is important to choose the right detail level based on your specific requirements and constraints.

For more information on how to set the detail level in your requests, refer to the [Quick Start Guide](quick_start_guide.md).
