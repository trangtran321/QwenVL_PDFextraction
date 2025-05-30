from pdf2image import convert_from_path 

def convert_to_image(filepath, directory):
    #convert all pdf pages into images in temporary folder
    images = convert_from_path(filepath, output_folder=directory, fmt="jpeg")