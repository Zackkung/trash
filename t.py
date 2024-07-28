import requests, time, os

def gold_price_api():
    res = requests.get("https://api.chnwt.dev/thai-gold-api/latest")
    data = res.json()

    print("\nDate : "+data["response"]["date"])
    print("Update time : "+data["response"]["update_time"])
    print("Gold : buy : "+data["response"]["price"]["gold"]["buy"],"sell : "+data["response"]["price"]["gold"]["sell"])
    print("Gold bar : buy : "+data["response"]["price"]["gold_bar"]["buy"],"sell : "+data["response"]["price"]["gold_bar"]["sell"])

def weather_api():
    res = requests.get("https://ipinfo.io/loc")
    lat = res.text.split(",")[0]
    lon = res.text.split(",")[1]
    API_key = '1930e1d23b58fb12d7d9df05e5c76cdd'
    API_url = f'https://api.openweathermap.org/data/3.0/?lat={lat}&lon={lon}&appid={API_key}'
    res2 = requests.get(API_url)
    print(res2.text)

def news_api():
    os.system("cls")
    time.sleep(1)
    category_list = ["business","entertainment","general","health","science","technology","sports"]
    print("[1] Business")
    print("[2] Entertainment")
    print("[3] General")
    print("[4] Health")
    print("[5] Science")
    print("[6] Technology")
    print("[7] Sports\n")
    ca = int(input("Enter category : ")) - 1
    category = category_list[ca]
    country = input("Enter country : ")
    API_key = 'e1a398bebe804a7992c1e4dac908c728'
    API_url = f'https://newsapi.org/v2/top-headlines?{country}=de&category={category}&apiKey={API_key}'
    res = requests.get(API_url)
    data = res.json()
    #print(data["articles"])
    t=1
    print("\n")
    for i in data["articles"]:
        print(t)
        print("Author : "+i["author"])
        print("Title : "+i["title"])
        print("Description : "+str(i["description"]))
        print("Url : "+i["url"])
        print("PublishedAt : "+i["publishedAt"]+"\n")
        t+=1

def main():
    os.system("cls")
    time.sleep(1)
    print("[1] Gold price")
    print("[2] Weather")
    print("[3] News")
    print("")
    user = input("Choose an option : ")
    if user == "1":
        gold_price_api()
    elif user == "2":
        weather_api()
    elif user == "3":
        news_api()
    else:
        print(f"{user} not found")
        time.sleep(2)
        main()
#main()