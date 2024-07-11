# stocknumbers

This python script will scrape through adidas.com or any website that uses demandware, and check the stock and available sizes of any SKU available on the website. This script is generally for live releases of new products, but will still function for regularly available products on the sites.

Uses Python3

Steps to run:

1. pip install requirements.txt
2. On line 7, insert the SKU of the product you would like to check stock on, or a product that is scheduled to release on the website soon. Ex: "HQ4202" from https://www.adidas.com/us/ultraboost-1.0-shoes/HQ4202.html
3. On line 8, insert the demandware site you would like to scrape. Ex: "adidas"
4. In config.py, it is highly recommended that you use a proxy to protect your IP address from being banned on the site. If a proxy is not used, it's likely that your IP will be banned almost immediately.
4. Run the script.
5. The script will continue to run until it is manually stopped via keyboard interrupt (input: control+c), as it was designed to monitor live releases on the website over an extended period of time.
6. Once the script is stopped, if it detected that stock was loaded for the product SKU that was provided, it will create json file within the same directory with the stock numbers of each size of the product SKU that was being monitored. If no stock was loaded or available, it will not create the json file, as there's no information it would need to add.

Preview:

<img width="1624" alt="Screenshot 2024-07-01 at 4 29 42 PM" src="https://github.com/dev-jujucollins/stocknumbers/assets/83800421/6c8bce36-8cf5-4ac2-9f02-cf14e84da665">

<img width="828" alt="Screenshot 2024-07-01 at 4 34 30 PM" src="https://github.com/dev-jujucollins/stocknumbers/assets/83800421/32e7b59e-20c9-4808-9dae-afd6e8ef59ee">

<img width="430" alt="Screenshot 2024-07-01 at 4 31 25 PM" src="https://github.com/dev-jujucollins/stocknumbers/assets/83800421/80ce1e13-8f66-48e0-a5b1-2ec920a2289c">

<img width="928" alt="Screenshot 2024-07-01 at 4 33 21 PM" src="https://github.com/dev-jujucollins/stocknumbers/assets/83800421/5053fb15-5e65-48a3-8a38-5378a02fddcd">
