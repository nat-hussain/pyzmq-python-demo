# PYZMQ Python Multiprocessing Demo 

In this repo you will find a simple example of how to use pyzmq to communicate between threads using the multiprocessing module in Python.

We use an XSUB/XPUB socket pair to create a simple pub/sub system. The publisher sends a message to the subscriber, and the subscriber prints the message in a white screen using pygame. 

## Step-by-step to run this demo ## 

### Installation

Tested in **Python 3.11**. Following commands are for powershell in Windows 11. Create a virtual environment, and install the dependencies using the following commands:
```bash
py -3.11 -m venv venv
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Running the demo

To run the demo, execute te file in app/main.py or use the following command:
```bash
python '.\app\main.py'
```

## Utilities

### Creating your own requirements file 

```bash
pip freeze > requirements.txt
```