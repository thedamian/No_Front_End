# How to present at a hackathon without a front end.

This is an example to follow along with the youtube video found here:

[![Watch the video](https://img.youtube.com/vi/lCs9EriXnY8/default.jpg)](https://youtu.be/lCs9EriXnY8)

Or see the sample video LIVE at: https://no-front-end.streamlit.app/

We will be using the python StreamLit to create a simple
project included in this repo as ```index.py``` to showcase
how you could have just an API and showcase your work without learning much about front end work or libraries.

In this example we'll be using the world famous Sample API and their [Coffee list](https://sampleapis.com/api-list/coffee) API endpoint.

Definately check out the [StreamLit Cheat sheet ](https://cheat-sheet.streamlit.app/) 

How to use it locally: 

Install dependancies
```
python -m venv venv           # or create a new enviroment with anaconda
pip install requirements.txt  # which only installs streamlit and all it's requirements
```
run it: 
```
streamlit run index.py
```

Of course if you're using uv you can add uv before any of these commands. 

For example to start it once you've "uv pip install -r requirements.txt" and "uv venv" to start the virtual enviroments, then you can "uv run streamlit run index.py --server.port 5000" to get it running locally.
