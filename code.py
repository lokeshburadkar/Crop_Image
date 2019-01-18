from PIL import Image
 
def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    cropped_image.show()
 
 
if __name__ == '__main__':
    image = 'C:\\Users\\lokesh_pc\\Desktop\\check_image.jpg'
    crop(image, (55, 55,246,68), 'C:\\Users\\lokesh_pc\\Desktop\\cropped.jpg')
