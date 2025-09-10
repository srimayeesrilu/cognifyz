from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Scraper for Quotes to Scrape
def scrape_quotes(page=1):
    url = f"http://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    data = []
    for quote in soup.find_all("div", class_="quote"):
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        data.append([text, author])

    has_next = soup.find("li", class_="next") is not None
    return ["Quote", "Author"], data, has_next


# Scraper for Hacker News
def scrape_hackernews():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    data = []
    for item in soup.select("span.titleline a")[:15]:  # updated selector
        title = item.get_text()
        link = item["href"]
        data.append([title, f'<a href="{link}" target="_blank">{link}</a>'])

    return ["Title", "Link"], data, False


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/scrape", methods=["POST"])
def scrape():
    site = request.json.get("site", "quotes")
    query = request.json.get("query", "").strip().lower()
    page = int(request.json.get("page", 1))

    headers, data, has_next = None, None, False

    if site == "quotes":
        headers, data, has_next = scrape_quotes(page)
    elif site == "hackernews":
        headers, data, has_next = scrape_hackernews()

    # Apply search filter
    if query and data:
        data = [row for row in data if any(query in str(item).lower() for item in row)]

    return jsonify({
        "headers": headers,
        "data": data,
        "has_next": has_next
    })


if __name__ == "__main__":
    app.run(debug=True)
