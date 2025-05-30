import base64
from io import BytesIO
import os, re, json, codecs
from PIL import Image
from langchain_ollama import OllamaLLM

def convert_to_base64(pil_image):
    """
    Convert PIL images to Base64 encoded strings

    :param pil_image: PIL image
    :return: Re-sized Base64 string
    """

    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")  # You can change the format if needed
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

def inference(image_path, prompt, sys_prompt="You are a helpful assistant.", max_new_tokens=4096, return_input=False):
    image = Image.open(image_path)
    image_obj = convert_to_base64(image)

    llm = OllamaLLM(model="qwen2.5vl:latest", num_predict=16384, temperature=0.1)
    llm_with_img_context = llm.bind(images=[image_obj])
    
    message = f"""{sys_prompt}\n{prompt}"""
    response = llm_with_img_context.invoke(message)
    return response
    
def extract_text(dir_path: str):

    prompt = '''1. Extract all text from the image. Include equations and ensure you are extracting the entire text from all collumns. There may be text between many figures in the image, you must extract that text as well.
    2. Describe in detail any image, workflow, chart, graph for figure above a 'Fig.' caption. 
    3. Extract all contents from a table, keeping the structure of the table intact. 
    Output a response in JSON format with these keys: {"text": str, "figures":[{"fig": int, "caption": str, "description": str, "image": PIL image}], "tables":[{"table_no": int, "caption": str, "data": [][]}}
    For figures, also output a PIL formatted image of the figure you found.
    '''
    responses = []
    for file in os.listdir(dir_path):
        filepath = os.path.join(dir_path, file)
        if os.path.isfile(filepath):
            id = re.split(r'\.', file)[0]
            id = re.split(r'-', id)[-1]
            response = inference(filepath, prompt)
            output = response.replace('```', '')
            output = output.replace('json', '')
            output = output.replace(r'\n', '')
            output = output.replace(r'\t', '')
            output = output.replace('\\', '')
            responses.append({"page":id, "response": json.loads(output)})
        
    with open("extracted_data.json", 'wb') as f:
         json.dump(responses, codecs.getwriter('utf-8')(f), indent=2)
