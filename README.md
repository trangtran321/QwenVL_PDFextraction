# PDF Data extraction using QWEN2.5VL
This is a short script that preliminarily extracts data from research papers in PDF format. It uses the Qwen2.5VL. 

# Dependencies:
1. Ensure that poppler utility is installed on machine. 
MacOS: https://formulae.brew.sh/formula/poppler#default 
    
    brew install poppler

Linux

    apt-get -> sudo apt-get install poppler-utils

https://poppler.freedesktop.org/ 
You can also clone from git: 

    git clone https://anongit.freedesktop.org/git/poppler/poppler.git

2. Ensure that ollama is installed and updated to latest version, then:  

    ollama pull qwen2.5vl

4. download all other dependencies from requirements.txt through pip or conda 

5. To run:
   
    python main.py --filpath <YOUR FILE PATH>

Outputs will be created in a JSON file named "extracted_data.json" for further processing. 


