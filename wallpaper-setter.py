import os
import random

def set_wallpaper(image_path):
    try:
        
        # Run the wal command to set the wallpaper
        
        os.system(f"wal -i {image_path}")
        print("Wallpaper set successfully!")
    except Exception as e:
        print(f"Error setting wallpaper: {e}")

if __name__ == "__main__":
    # Replace this with the path to the directory containing images
    wallpaper_directory = "/home/versus/Downloads/Walls/new"

    # Get a list of all files with jpg or jpeg extension
    image_files = [f for f in os.listdir(wallpaper_directory) if f.lower().endswith((".jpg", ".jpeg"))]

    if image_files:
        # Select a random image file from the list
        random_image = random.choice(image_files)
        image_path = os.path.join(wallpaper_directory, random_image)

        # Call the function to set the wallpaper
        set_wallpaper(image_path)
    else:
        print("No image files found in the directory.")

