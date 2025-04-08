from PIL import Image

def resize_image_with_aspect_ratio(input_image_path, output_image_path, max_size):
    """
    Resize the image while maintaining its aspect ratio.
    
    :param input_image_path: Path to the input image
    :param output_image_path: Path to save the resized image
    :param max_size: Maximum size as a tuple (max_width, max_height)
    """
    with Image.open(input_image_path) as image:
        original_size = image.size
        image.thumbnail(max_size)
        resized_size = image.size
        image.save(output_image_path)
        print(f"Image resized from {original_size} to {resized_size} and saved to {output_image_path}")

# Example usage
input_image_path = "/Users/okazakikeita/Desktop/imageNumber/images/img.png"
output_image_path = "/Users/okazakikeita/Desktop/imageNumber/resize_image/resize_image.png"
max_size = (1000, 800)  # Example maximum size

resize_image_with_aspect_ratio(input_image_path, output_image_path, max_size)