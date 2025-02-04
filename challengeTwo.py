import requests
from bs4 import BeautifulSoup
import pandas as pd
from rich import print

# https://www.vea.com.ar/bebidas


def getAllProduct(url):
    # url='https://www.mercadolibre.com.ar/ofertas?page=1'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0"
    }
    list_products = []
    for i in range(1, 20):
        pagination = f"{url}?page={i}"

        response = requests.get(pagination, headers=headers, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        products = soup.find_all("div", class_="poly-card")

        if products and len(products) != 0:
            for product in products:
                try:
                    divImage = product.find(
                        "img", class_="poly-component__picture"
                    ).attrs.get("data-src")
                except:
                    divImage = ""
                contentInfo = product.find("div", class_="poly-card__content")
                try:
                    title = contentInfo.find("a").text
                except:
                    title = ""
                try:
                    seller = contentInfo.find(
                        "span", class_="poly-component__seller"
                    ).text.split(" ")[1]
                except:
                    seller = ""
                try:
                    price_before = contentInfo.find(
                        "span", class_="andes-money-amount__fraction"
                    ).text.strip('"')
                except:
                    price_before = ""
                try:
                    price_now = (
                        contentInfo.find("span", class_="andes-money-amount")
                        .find("span", class_="andes-money-amount__fraction")
                        .text
                    )
                except:
                    price_now = ""
                try:
                    percentage = contentInfo.find(
                        "span", class_="andes-money-amount__discount"
                    ).text.split("%")[0]
                except:
                    percentage = ""

                print(
                    f"img: {divImage} title: {title} seller: {seller} price before:{price_before} percentage: {percentage} price now: {price_now}"
                )

                list_products.append(
                    {
                        "title": title,
                        "image": divImage,
                        "price_before": price_before,
                        "percentage_discount": percentage,
                        "price_now": price_now,
                        "seller": seller,
                    }
                )

    return list_products


# Main
if __name__ == "__main__":
    url = "https://www.mercadolibre.com.ar/ofertas"

    products = getAllProduct(url)

    if len(products) != 0:
        df = pd.DataFrame(products)
        df.to_excel("offerproductsallpage.xlsx", index=False, engine="openpyxl")
        print("Datos importados a offerproducts.xlsx")
    else:
        print("No se ha cargado nada")
