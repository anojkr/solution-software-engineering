Author : Anoj Kumar
Email : anoj.kumar48@gmail.com

Git clone and setup python environment

Step 1. git clone https://github.com/anojkr/solution-software-engineering.git

Step 2. cd solution-software-engineering

Step 3. pip install virtualenv

Step 4. virtualenv venv

Step 5. source venv/bin/activate

Step 7. pip install -r requirements.txt


TASK 1

Run HashCode Task

python hash_code/hash_solution.py

Expected output =

     {

     680131659347 //hashcode of string "leepadg"

     lawnmower    //dehash of code 930846109532517

      }


TASK 2

Run Query 1

 python web_crawler.py --query1 max_page keyword

 eg. python web_crawler.py --query1 5 bag

 //This query return total no. of result from page 1 to max_page with provided keyword as argument

Run Query 2

 python web_crawler.py --query2 page_number keyword

 eg. python web_crawler.py --query2 5 bag

 //This query return total no. of result fetched on specific page number with provided page_number and keyword