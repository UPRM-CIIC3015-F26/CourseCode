import os
from PIL import Image
from matplotlib import pyplot as plt

# Path to the sample image in this folder (works from repo root or inside images/)
IMAGES_DIR = os.path.dirname(os.path.abspath(__file__))
SAMPLE_IMAGE = os.path.join(IMAGES_DIR, "rainbow.png")


# ==========================================
# 1. Open and display images
# ==========================================

def open_image_example(image_file):
    with Image.open(image_file) as image:
        print(f"Successfully opened image: {image.filename}")


def display_image_properties(image_file):
    with Image.open(image_file) as image:
        print(f"{image.filename}")
        print(f"Size: {image.size}")
        print(f"Format: {image.format}")


def display_image(image_file):
    with Image.open(image_file) as image:
        plt.axis("off")
        plt.imshow(image)
        plt.show()


# ==========================================
# 2. Rotate and save images
# ==========================================

def rotate_image_basic(image_file, angle=45):
    with Image.open(image_file) as image:
        rotated_image = image.rotate(angle)
        plt.axis("off")
        plt.imshow(rotated_image)
        plt.show()


def rotate_image_expand(image_file, angle=90):
    with Image.open(image_file) as image:
        rotated_image = image.rotate(angle, expand=True)
        print("Original size:", image.size)
        print("Rotated size:", rotated_image.size)
        plt.axis("off")
        plt.imshow(rotated_image)
        plt.show()


def rotate_and_save_image(image_file, angle=10):
    with Image.open(image_file) as image:
        rotated_image = image.rotate(angle, expand=True)
        saved_image_file = os.path.join(os.path.dirname(image_file), "rotated_image.png")
        rotated_image.save(saved_image_file)
        print(f"Rotated image saved as {saved_image_file}")
        return saved_image_file


# ==========================================
# 3. Crop images
# ==========================================

def crop_top_left_quarter(image_file):
    with Image.open(image_file) as image:
        width, height = image.size
        print(f"Width: {width}, Height: {height}")
        width_midpoint = int(width // 2)
        height_midpoint = int(height // 2)
        left = 0
        top = 0
        right = width_midpoint
        bottom = height_midpoint
        cropping_box = (left, top, right, bottom)
        cropped_image = image.crop(cropping_box)
        plt.axis("off")
        plt.imshow(cropped_image)
        plt.show()


def crop_image_by_pixels(image_file, pixels_to_crop):
    with Image.open(image_file) as image:
        width, height = image.size
        left = pixels_to_crop
        top = pixels_to_crop
        right = width - pixels_to_crop
        bottom = height - pixels_to_crop
        cropping_box = (left, top, right, bottom)

        try:
            cropped_image = image.crop(cropping_box)
            saved_image_file = os.path.join(
                os.path.dirname(image_file), f"cropped_{pixels_to_crop}pixels.png"
            )
            cropped_image.save(saved_image_file)
            print(f"Image cropped and saved as {saved_image_file}")
            return saved_image_file
        except Exception:
            print("Error cropping image")
            print("Check that the amount of pixels to crop is not too large")
            return None


def crop_image_by_percentage(image_file, percentage_to_crop):
    with Image.open(image_file) as image:
        width, height = image.size
        crop_percentage = percentage_to_crop / 100
        crop_amount_width = int(width * crop_percentage / 2)
        crop_amount_height = int(height * crop_percentage / 2)
        left = crop_amount_width
        top = crop_amount_height
        right = width - crop_amount_width
        bottom = height - crop_amount_height
        cropping_box = (left, top, right, bottom)

        try:
            cropped_image = image.crop(cropping_box)
            saved_image_file = os.path.join(
                os.path.dirname(image_file), f"cropped_{percentage_to_crop}percent.png"
            )
            cropped_image.save(saved_image_file)
            print(f"Image cropped and saved as {saved_image_file}")
            return saved_image_file
        except Exception:
            print("Error cropping image")
            print("Check that the percentage to crop is less than 100")
            return None


# ==========================================
# 4. Resize images
# ==========================================

def resize_image_by_factor(image_file, resize_factor):
    with Image.open(image_file) as image:
        original_width, original_height = image.size
        new_width = int(original_width * resize_factor)
        new_height = int(original_height * resize_factor)

        try:
            resized_image = image.resize((new_width, new_height))
            saved_image_file = os.path.join(
                os.path.dirname(image_file), f"resized_{new_width}x{new_height}.png"
            )
            resized_image.save(saved_image_file)
            print(f"Image resized and saved as {saved_image_file}")
            return saved_image_file
        except Exception:
            print("Error resizing image")
            print("Check that the resize factor is valid")
            return None


def resize_to_new_width(image_file, new_width):
    with Image.open(image_file) as image:
        original_width, original_height = image.size
        aspect_ratio = original_height / original_width
        new_height = int(new_width * aspect_ratio)

        try:
            resized_image = image.resize((new_width, new_height))
            saved_image_file = os.path.join(
                os.path.dirname(image_file), f"resized_{new_width}x{new_height}.png"
            )
            resized_image.save(saved_image_file)
            print(f"Image resized and saved as {saved_image_file}")
            return saved_image_file
        except Exception:
            print("Error resizing image")
            print("Check that the new width is valid")
            return None


if __name__ == "__main__":
    # Uncomment the example you want to present during class:

    # 1. Open and display images
    open_image_example(SAMPLE_IMAGE)
    display_image_properties(SAMPLE_IMAGE)
    # display_image(SAMPLE_IMAGE)

    # 2. Rotate and save images
    # rotate_image_basic(SAMPLE_IMAGE, 45)
    # rotate_image_expand(SAMPLE_IMAGE, 90)
    # rotated_file = rotate_and_save_image(SAMPLE_IMAGE, 10)
    # display_image(rotated_file)

    # 3. Crop images
    # crop_top_left_quarter(SAMPLE_IMAGE)
    # cropped_px_file = crop_image_by_pixels(SAMPLE_IMAGE, 200)
    # display_image(cropped_px_file)
    # cropped_pct_file = crop_image_by_percentage(SAMPLE_IMAGE, 50)
    # display_image(cropped_pct_file)

    # 4. Resize images
    # resized_factor_file = resize_image_by_factor(SAMPLE_IMAGE, 2)
    # display_image(resized_factor_file)
    # resized_width_file = resize_to_new_width(SAMPLE_IMAGE, 200)
    # display_image(resized_width_file)
