# PDF Data extraction using QWEN2.5VL
This is a short script that preliminarily extracts data from research papers in PDF format. It uses the Qwen2.5VL. 

# Dependencies:
Ensure that poppler utility is installed on machine. 
MacOS:
    
    brew install poppler

Linux

    apt-get -> sudo apt-get install poppler-utils

You can also clone from git: 

    git clone https://anongit.freedesktop.org/git/poppler/poppler.git

Ensure that ollama is installed and updated to latest version, then:  

    ollama pull qwen2.5vl

Download all other dependencies from requirements.txt through pip or conda 

### To run:
     
    python main.py --filpath **YOUR_FILE_PATH**

Outputs will be created in a JSON file named "extracted_data.json" for further processing. 


