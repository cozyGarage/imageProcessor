from PIL import Image, ImageFilter, ImageEnhance
import os

def process_image(input_folder, output_folder, width=1280, height=800, sharpen_strength=2.0, contrast_factor=1.2):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            try:
                image_path = os.path.join(input_folder, filename)
                image = Image.open(image_path)
                
                # Resize the image
                image = image.resize((width, height))
                
                # Apply sharpen filter
                sharpened_image = image.filter(ImageFilter.SHARPEN)
                
                # Adjust contrast
                enhanced_image = ImageEnhance.Contrast(sharpened_image).enhance(contrast_factor)
                
                # Create a modified filename
                modified_filename = f"modified_{filename}"
                output_path = os.path.join(output_folder, modified_filename)
                
                # Save the modified image
                enhanced_image.save(output_path)
            except Exception as e:
                print(f"Error processing {filename}: {e}")
        else:
            print(f"Skipping {filename}, not an image file.")

if __name__ == "__main__":
    input_folder = "./imgs"
    output_folder = "./editedImgs"
    
    process_image(input_folder, output_folder)
