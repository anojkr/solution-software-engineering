import requests, sys
from bs4 import BeautifulSoup

def crawl(args):
    """
    Author : Anoj Kumar
    Email : anoj.kumar48@gmail.com

    Query1 Format: python web_crawler.py --query1 <max_page> <keyword>
    This query1 will return total no. of results fetched from page_1 to maximum page
    url format: http://www.shopping.com/products?KW=<keword>

    Query2 Format: python web_crawler.py --query2 <page_number> <keyword>
    This query2 will return total no. of result fetched from page_number specified
    url format : http://www.shopping.com/products~PG-<number>?KW=<keyword>
    """

    if '--query1'== args[0]:
        max_page = args[1]
        keyword = args[2]
        value = 0
        for page in range(1, int(max_page)+1):
            if (page <= max_page):
                host = 'http://www.shopping.com'
                url = host +'/products~PG-'+str(page)+'?KW=' + keyword
                source_code = requests.get(url)
                plain_text = source_code.text
                text = BeautifulSoup(plain_text,"html.parser")
                for t in text.find_all('div',{'class':'gridItemTop'}):
                    value +=1
                print 'Crawling page-'+str(page)+ ' done.'
                page +=1

        print 'Total no. of results for query1 is : ' + str(value)
        return value

    elif '--query2' == args[0]:
        value = 0
        host = 'http://www.shopping.com'
        url = host +'/products~PG-'+str(args[1])+'?KW=' + args[2]
        source_code = requests.get(url)
        plain_text = source_code.text
        text = BeautifulSoup(plain_text,  "html.parser")
        for t in text.find_all('div',{'class':'gridItemTop'}):
                value +=1
        print 'Total no. of results for page ' + str(args[1])+ ' is : '+ str(value)
        return value

    else:
        print 'Invalid query'

if __name__ == "__main__":
    crawl(sys.argv[1:])


