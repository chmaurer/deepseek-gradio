# How to Get Started
This is a guide on how to really run the DeepSeek-R1 model for your own. You have to have an account on the azure platform and deploy the model there. At the time of writing, this is possible at an inferencing cost of 0$. 

## Setup on Azure
* In Azure AI Foundry, create an Azure AI Hub. Currently, only some us regions allow to publish the DeepSeek-R1 model.
* Go to your AI Hub, create a new project.
* When completed, select the model catalog on the left, search and select "DeepSeek-R1" and hit "Deploy". You have to provide a unique name.

## Setup your machine
* Next, open your personal terminal. Create a conda environment: conda create -n myenv python=3.11
* Activate the environment, install some more packages:
  * conda activate myenv
  * pip install gradio
  * pip install azure-ai-inference
  * pip install python-dotenv
* Create a new project in pycharm and initialise a git repo to add your sources. Select your conda env at the very right bottom of the Pycharm IDE.

## Sources and run
* Clone the repo or add at least main.py and the .env file (do it yourself, same folder as you put main in) to your project. Make sure to maintain the following variables in .env:
  * DEEPSEEK_ENDPOINT: The endpoint where your model resides, find this on Azure
  * DEEPSEEK_KEY: The key used to invoke your model, find it on Azure as well
 
* Then hit run and enjoy... Sometimes I had to wait quite long for the API to return a result, like 10sec or so.

![Screenshot](screenshot.png?raw=true "Screenshot of Chat")
