import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import openai

# Configure OpenAI API Key Replace it with Your's API
OPENAI_API_KEY = "openaiapikey"  # Mine is sk-Y5QVC-U5l4qPSqYBvBUkgrRQ0mGXPewMtrgC3sDhOpT3BlbkFJiwRGVPBSbLfPIm-O3L_P5IjFE_KLK35GkpO60GHXQA

# Function to fetch product page
def get_product_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    return response.text if response.status_code == 200 else None

# Function to parse product details
def parse_product_details(html):
    soup = BeautifulSoup(html, "html.parser")
    
    # Extract product name
    name = soup.find("span", id="productTitle")
    name = name.get_text(strip=True) if name else "N/A"

    # Extract rating
    rating = soup.select_one("span[data-asin-rating]")
    rating = rating.get_text(strip=True) if rating else "N/A"

    # Extract number of ratings
    num_ratings = soup.select_one("#acrCustomerReviewText")
    num_ratings = num_ratings.get_text(strip=True).replace(" ratings", "") if num_ratings else "N/A"

    # Extract price
    price = soup.select_one("span.a-price > span.a-offscreen")
    price = price.get_text(strip=True) if price else "N/A"

    # Extract discount
    discount = soup.select_one("span.savingsPercentage")
    discount = discount.get_text(strip=True) if discount else "N/A"

    # Extract bank offers
    offers_section = soup.find("div", id="promotions_feature_div")
    bank_offers = offers_section.get_text(strip=True) if offers_section else "N/A"

    return {
        "Product Name": name,
        "Rating": rating,
        "Number of Ratings": num_ratings,
        "Selling Price": price,
        "Total Discount": discount,
        "Bank Offers": bank_offers
    }

# Function to extract "About this item" and "Product Information"
def extract_descriptions(html):
    soup = BeautifulSoup(html, "html.parser")

    about_section = soup.find("ul", class_="a-unordered-list a-vertical a-spacing-mini")
    about_text = " | ".join([li.get_text(strip=True) for li in about_section.find_all("li")]) if about_section else "N/A"

    product_info_section = soup.find("div", id="prodDetails")
    product_info_text = product_info_section.get_text(strip=True) if product_info_section else "N/A"

    return {
        "About This Item": about_text,
        "Product Information": product_info_text
    }

# Function to extract image URLs
def extract_images(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service("chromedriver.exe")  # Replace with your chromedriver path
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    images = [img["src"] for img in soup.find_all("img") if "src" in img.attrs]
    driver.quit()
    
    return images

# Function to generate AI-powered review summary
def generate_review_summary(reviews):
    prompt_text = f"Summarize the following customer reviews for an Amazon Smart TV: {reviews}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt_text}]
    )
    
    return response["choices"][0]["message"]["content"]

# Main execution
def scrape_amazon_product(url):
    html = get_product_page(url)
    if not html:
        return "Failed to retrieve the page."

    product_details = parse_product_details(html)
    descriptions = extract_descriptions(html)
    images = extract_images(url)

    # For AI Summary, we can extract the first few customer reviews (dummy example)
    reviews = ["Great TV!", "Picture quality is amazing.", "Good value for money."]
    ai_review_summary = generate_review_summary(reviews)

    product_details.update(descriptions)
    product_details["Images"] = images
    product_details["AI Review Summary"] = ai_review_summary

    return product_details

# Example usage
product_url = "https://www.amazon.in/dp/B09G99YPQM"  # Example Smart TV product link
data = scrape_amazon_product(product_url)
print(data)


# It's Pretty Much But Make it more Handy
#Function to save data to CSV and JSON
def save_data(data, filename): 
    df = pd.DataFrame(data)

    # Save to CSV
    csv_filename = f"{filename}.csv"
    df.to_csv(csv_filename, index=False, encoding="utf-8")
    logging.info(f"Data saved to {csv_filename}")

    # Save to JSON
    json_filename = f"{filename}.json"
    with open(json_filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    logging.info(f"Data saved to {json_filename}")
