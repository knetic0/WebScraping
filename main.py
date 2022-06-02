from bs4 import BeautifulSoup
import requests

while True:

    refresh = input("Press F to refresh or Press Q to quit.")

    if refresh == "F" or refresh == "f":

        url = requests.get("https://crypto.com/price")
        icerik = url.content
        soup = BeautifulSoup(icerik, "lxml")

        name = soup.find_all("td", {"class": "css-1sem0fc"})
        price = soup.find_all("div", {"class": "css-b1ilzc"})

        listeName = list()
        listePrice = list()

        for i in range(0, len(name)):
            name[i] = (name[i].text).strip("\n").strip()
            listeName.append([name[i]])

        for j in range(0, len(price)):
            price[j] = (price[j].text).strip("\n").strip()
            listePrice.append([price[j]])

        print("\tName\t\t\t", "Price")
        print("------------------------------")
        for i in range(len(listePrice)):
            print(i + 1, "-)", (','.join(listeName[i])), "~", (','.join(listePrice[i])))

    elif refresh == "Q" or refresh == "q":
        break
