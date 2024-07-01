import requests
import atexit
import json
import time
from config import proxy_credendtials as pc

product_sku = "HQ4202"  # Insert product sku here | https://www.adidas.com/us/ultraboost-1.0-shoes/HQ4202
site = "adidas"  # Demandware site (such as adidas.com) 
target_site = (
    "https://www."
    + str(site).lower()
    + ".com/api/products/"
    + str(product_sku).upper()
    + "/availability"
)
print(target_site)
timeout_retry_seconds = 180
refresh_rate_seconds = 15  # It will refresh with updated stock number every 15 seconds
total_stock = {}
loaded_sizes = {}


def start_scan():
    atexit.register(save_data)

    # Importing proxy credentials from config.py
    proxy = pc
    proxies = {"http": proxy, "https": proxy}
    r = requests.get(target_site, proxies=proxies, verify=False)
    print(r.text)

    live = False

    while True:
        text = r.text

        if "security issue" in text:  # If the IP is banned
            print("\n")
            print("=====================================")
            print("Session has been forbidden on this IP")
            print("=====================================")
            print("\n")

        elif "<title>" in text:  # If the ip is rate limited
            print("\n")
            print("=============================")
            print("Session has been rate limited")
            print("=============================")
            print("\n")
            print(text)

            time.sleep(timeout_retry_seconds)
        else:
            json_message = json.loads(text)

            if "message" in json_message:  # If the product is not found
                # Once the release is done save data and exit
                if live:
                    live = False
                    save_data()

                print("\n")
                print("The product for SKU " + product_sku + " was not found.")
                print("\n")

            elif "id" in json_message:  # If the product is found
                sku = json_message["id"]
                status = json_message["availability_status"]

                print(" ")
                print("SKU: " + sku)
                print("Availability: " + status)

                if status == "IN_STOCK":  # If the product is in stock
                    live = True
                    sizes_in_stock = ""

                    for variation in json_message["variation_list"]:
                        size = str(variation["size"])
                        stock_amount_int = variation["availability"]
                        stock_amount_string = str(stock_amount_int)

                        if stock_amount_int > 0:
                            sizes_in_stock += size + ", "

                        if size not in loaded_sizes:  # If the size is not loaded
                            print(" ")
                            print("   Size: " + size)
                            print("   Available: " + stock_amount_string)
                            print("   Status: " + variation["availability_status"])

                            loaded_sizes[size] = stock_amount_int
                            total_stock[size] = stock_amount_int
                        else:
                            previous_stock = loaded_sizes[size]

                            if previous_stock != stock_amount_int:  # If stock changed
                                if stock_amount_int > previous_stock:
                                    total_stock[size] = total_stock[size] + (
                                        stock_amount_int - previous_stock
                                    )

                                print(
                                    "====================================================="
                                )
                                print("Stock change for size " + size)
                                print("New stock: " + stock_amount_string)
                                print(
                                    "====================================================="
                                )

                                loaded_sizes[size] = stock_amount_int
                    if sizes_in_stock != "":
                        print("Available sizes: " + sizes_in_stock[:-2])
                        # Removes the last comma and space

        time.sleep(refresh_rate_seconds)  # Refreshes every 15 seconds


def save_data():
    if len(total_stock) > 0:
        with open(
            "total_stock" + "_" + str(product_sku) + ".json", "w"
        ) as total_stock_file:
            json.dump(total_stock, total_stock_file, sort_keys=True, indent=4)
        # Saves the stock numbers for each size in a json file within the same directory

        print("Saved the total stock to total_stock_" + str(product_sku) + ".json")
    else:
        print("No stock was loaded, no data saved")


if __name__ == "__main__":
    start_scan()
