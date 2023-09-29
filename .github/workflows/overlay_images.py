from PIL import Image

def overlay_images(background_path, overlay_path, output_path):
    # Open the background and overlay images
    background = Image.open(background_path)
    overlay = Image.open(overlay_path)

    # Resize overlay to fit the background (if needed)
    overlay = overlay.resize(background.size, Image.ANTIALIAS)

    # Overlay the images
    combined = Image.alpha_composite(background.convert('RGBA'), overlay.convert('RGBA'))

    # Save the combined image
    combined.save(output_path, 'PNG')

if __name__ == '__main__':
    background_image_path = 'background.png'
    snake_image_path = 'snake.png'
    combined_image_path = 'combined.png'

    overlay_images(background_image_path, snake_image_path, combined_image_path)
