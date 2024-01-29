# import relevant libraries
from bs4 import BeautifulSoup
import requests
from constant import my_headers

# define session headers
session = requests.Session()
session.headers = my_headers


# function to extract data from a single page
def scrape_single_page(url):
    response = session.get(url, headers=my_headers)
    choco_soup = BeautifulSoup(response.text, 'html.parser')

    div_a = choco_soup.find_all("div",
                                {"class": "styles_cardWrapper__LcCPA styles_show__HUXRb styles_reviewCard__9HxJJ"})
    chocolat_data = []

    for div in div_a:
        name = div.find("span", {"class": "typography_heading-xxs__QKBS8 typography_appearance-default__AAY17"})
        no_rev = div.find("span", {"class": "typography_body-m__xgxZ_ typography_appearance-subtle__8_H2l"})
        rating = div.find("div", {"class": "styles_reviewHeader__iU9Px"})
        rev_title = div.find("h2", {"class": "typography_heading-s__f7029 typography_appearance-default__AAY17"})
        rev = div.find("p", {
            "class": "typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn"})
        rev_date = div.find("p", {
            "class": "typography_body-m__xgxZ_ typography_appearance-default__AAY17 typography_color-black__5LYEn"})
        rev_reply = div.find("p", {
            "class": "typography_body-m__xgxZ_ typography_appearance-default__AAY17 styles_message__shHhX"})

        name_text = name.text.strip() if name else None
        no_rev_text = no_rev.text.strip() if no_rev else None
        rating_text = rating.get("data-service-review-rating")
        rev_title_text = rev_title.text.strip() if rev_title else None
        rev_text = rev.text.strip() if rev else None

        rev_date_text = rev_date.text.split(":")[1].strip() if rev_date else None

        rev_reply_text = rev_reply.text.strip() if rev_reply else None

        chocolat_data.append({"Name": name_text,
                              "N_Reviews": no_rev_text,
                              "Ratings": rating_text,
                              "Title": rev_title_text,
                              "Review": rev_text,
                              "Date": rev_date_text,
                              "Reply": rev_reply_text

                              })

    return chocolat_data
