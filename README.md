# stocknumbers

This python script will scrape through adidas.com or any website that uses demandware, and check the stock and available sizes of any SKU available on the website.

Uses Python3

Steps to run:

1. pip install requirements.txt
2. On line 7, insert the SKU of the product you would like to check stock on, or a product that is scheduled to release on the website soon. Ex: "B75806" from https://www.adidas.com/us/samba-og-shoes/B75806.html
3. On line 8, insert the demandware site you would like to scrape. Ex: "adidas"
4. Run the script.
5. The script will continue to run until it is manually closed via key input: control+c, as it was designed to monitor live releases on the website over an extended period of time.
6. Once the script is stopped, if it detected that stock was loaded for the product SKU that was provided, it will create json file within the same directory with the stock numbers of each size of the product SKU that was being monitored. If no stock was loaded or available, it will not create the json file, as there's no information it would need to add.
