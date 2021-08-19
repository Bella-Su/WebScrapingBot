import requests
from bs4 import BeautifulSoup
import time
import csv
import send_mail
from datetime import date

urls = ["https://finance.yahoo.com/quote/RKT?p=RKT", 
        "https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch", 
        "https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch"]
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}

today = str(date.today()) + '.csv' ## today object to return today's date as a string

csv_file = open(today, "w") ## create a csv file for writing
csv_writer = csv.writer(csv_file) ## create a object to write into the file
csv_writer.writerow(['Stock Name', 'Current Price', 'Previous Close', 'Open','Bid', 'Ask', 'Day Range', '52 week Range','Volume', 'Avg. Volume']) ## .writerow is a method

for url in urls:
    stock = []
    html_page = requests.get(url, headers=headers) ##print(html_page.content)->we can print the whole page content
    soup = BeautifulSoup(html_page.content, 'lxml') ##soup object, in the  beautifulSoup() we pass the html content and parase 


    header_info = soup.find_all("div", id="quote-header-info")[0] ## header_info is a list with only one element, so we can use[0]
    stock_tittle = header_info.find("h1").get_text()
    current_price = header_info.find("div", class_ = "My(6px) Pos(r) smartphone_Mt(6px)").find("span").get_text()

    stock.append(stock_tittle)
    stock.append(current_price)

    table_info = soup.find_all("div", class_ = "D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)")[0].find_all("tr")

    for i in range(0,8):
        value = table_info[i].find_all("td")[1].get_text()
        stock.append(value)
    
    csv_writer.writerow(stock) ## write the list into as a row into the file
    time.sleep(5)

csv_file.close()

## Call function to send the mail
send_mail.send(filename= today)
