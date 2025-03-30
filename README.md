📺 Amazon India Smart TV Scraper

This project is a functional web scraper designed to extract detailed product information from Amazon India Smart TV listings. The scraper fetches product details, descriptions, images, and reviews and uses AI (OpenAI API) to generate a summary of customer reviews.
✨ Features

    Extract Product Details: Name, Rating, Number of Ratings, Price, Discount, and Bank Offers.

    Scrape Descriptions: "About This Item" and "Product Information" sections.

    Download Images: All product images, including the "From the Manufacturer" section.

    AI-Generated Review Summary: Automatically summarizes customer feedback using OpenAI.

    CSV & JSON Output: Saves structured data in both CSV and JSON formats.

🛠 Tech Stack
Technology	Purpose
Python	Core scripting language
Requests	Fetches web page content
BeautifulSoup	Parses static HTML content
Selenium	Handles dynamic content
Pandas	Structures and processes data
OpenAI API	Generates AI-powered review summaries
🚀 Installation & Setup
1️⃣ Install Dependencies
Make sure you have Python installed (>=3.7), then install the required libraries:
pip install requests beautifulsoup4 selenium pandas openai

2️⃣ Setup ChromeDriver for Selenium
Download ChromeDriver that matches your Chrome version from here.
Place it in the project directory.

📜 Usage
Run the Scraper
python scraper.py
Expected Output

CSV Output (amazon_smart_tv_data.csv):
Product Name, Rating, Number of Ratings, Price, Discount, AI Review Summary
Samsung 4K TV, 4.5, 10,000+, ₹45,999, 20%, "Great sound and picture"

JSON Output (amazon_smart_tv_data.json):

    [
      {
        "Product Name": "Samsung 55-inch 4K Smart TV",
        "Rating": "4.5",
        "Number of Ratings": "10,000+",
        "Price": "₹45,999",
        "Discount": "20%",
        "AI Review Summary": "Customers love the display quality and sound clarity...",
      }
    ]

🤖 AI-Generated Review Summary

Customers love the display quality, mentioning its sharp colors and brightness levels. The TV's sleek design and pre-installed apps add to its appeal. Gamers appreciate the low input lag, and the Dolby Atmos sound is a highlight. However, some users report WiFi connectivity issues, occasional software lags, and a slow remote response. Sound quality and viewing angles could be improved, and a few customers mention customer support concerns. Overall, it's considered a great value for money TV with modern features.


Feel free to fork this repo, submit pull requests, or raise issues. Contributions are always welcome!

🏆 Author
👤 DEV DUBEY
📧 devdubey2002@gmail.com

🌟 If you like this project, don't forget to star ⭐ it on GitHub!
