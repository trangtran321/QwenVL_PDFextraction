import tempfile
import preprocess
import extract
import argparse
import os 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script that uses Qwen2.5VL to extract text from PDF."
    )

    parser.add_argument("--filepath", required=True, type=str, help="Enter PDF filepath.")
    args = parser.parse_args()

    filepath = args.filepath
    if not os.path.exists(filepath):
        raise Exception("Invalid Input: Please ensure validity of file path and try again.")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        preprocess.convert_to_image(filepath, temp_dir)
        extract.extract_text(temp_dir)
