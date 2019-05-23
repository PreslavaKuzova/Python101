from bs4 import BeautifulSoup
from collections import deque
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine, select
import urllib3
import requests
import re

def main():
    # create database
    engine = create_engine('sqlite:///web_crawler')
    metadata = MetaData()
    website = Table('web_crawler', metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('address', String),
        Column('server', String),
    )
    metadata.create_all(engine)
    
    connection = engine.connect()
    
    # initially get the websites from this website
    http = urllib3.PoolManager()
    url = "https://gong.bg/"
    r = requests.get(url)
    ins = website.insert().values(address = url, server = r.headers["Server"])
    connection.execute(ins)
    
    url_queue = deque([url])

    while len(url_queue):

        url = url_queue.popleft()
        print(f'Starting queue for new url: {url}')
        response = http.request('GET', url)
        soup = BeautifulSoup(response.data, features="html.parser")
        
        # extract links ending in .bg from a particular website
        # TODO add check for the beggining of the link http*://
        for link in soup.findAll('a', attrs={'href': re.compile(r"\.bg$")}):
            
            current_url = link.get('href')
            s = select([website]).where(website.c.address == current_url)
            result = connection.execute(s)

            # if the current_url is not in the queue and it is not in the database
            if current_url not in url_queue and result.first() == None:
                r = requests.get(current_url)
                
                # cannot get the server using this code?
                # print("Print",r.headers["Server"])
                
                ins = website.insert().values(address = current_url, server = r.headers["Server"])
                connection.execute(ins)
                
                url_queue.append(current_url)
                print(f'Just got new link: {current_url}')

            

            print(f'Current url_queue: {url_queue}')
    
if __name__ == "__main__":
    main()