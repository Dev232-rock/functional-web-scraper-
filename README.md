# functional-web-scraper-
A. Setup and Install Dependencies
pip install requests beautifulsoup4 selenium pandas openai
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import openai
import json
import pandas as pd
import time
import logging

Example Output (Enhanced)
Extracted Reviews:
[
    "Amazing display quality!",
    "Sound could be better.",
    "Value for money.",
    "Remote is a bit slow.",
    "Sleek and modern design.",
    "Great selection of pre-installed apps.",
    "The brightness levels are excellent.",
    "WiFi connectivity issues sometimes.",
    "Customer support could be improved.",
    "Perfect for gaming with low input lag.",
    "Dolby Atmos sound is immersive.",
    "Occasional software lags when switching apps.",
    "Easy setup and user-friendly interface.",
    "Colors are vibrant and sharp.",
    "Viewing angles could be wider."
]
AI-Generated Review Summary:
Customers love the display quality, mentioning its sharp colors and brightness levels. The TV's sleek design and pre-installed apps add to its appeal. Gamers appreciate the low input lag, and the Dolby Atmos sound is a highlight. However, some users report WiFi connectivity issues, occasional software lags, and a slow remote response. Sound quality and viewing angles could be improved, and a few customers mention customer support concerns. Overall, it's considered a great value for money TV with modern features.
