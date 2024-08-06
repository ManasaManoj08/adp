import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk  

def fetch_cheapest_price():
    # Get the product URLs from the user
    url1 = url1_entry.get()
    url2 = url2_entry.get()
    url3 = url3_entry.get()

    if not url1 or not url2 or not url3:
        messagebox.showerror("Error", "Please enter all three product URLs.")
        return

    try:
        # Replace 'your_data_file.json' with the actual path to your JSON data file
        with open('trail2.0.py', encoding='utf8') as f:
            price_data = f.read()

        if price_data:
            json_price_data = json.loads(price_data)
            price = []

            for d in json_price_data:
                if d['amazon_url'] == url1 or d['myntra_url'] == url1 or d['flipkart_url'] == url1:
                    price.append({'name': d['name'], 'price': d['amazon_price'], 'url': d['amazon_url']})
                elif d['amazon_url'] == url2 or d['myntra_url'] == url2 or d['flipkart_url'] == url2:
                    price.append({'name': d['name'], 'price': d['myntra_price'], 'url': d['myntra_url']})
                elif d['amazon_url'] == url3 or d['myntra_url'] == url3 or d['flipkart_url'] == url3:
                    price.append({'name': d['name'], 'price': d['flipkart_price'], 'url': d['flipkart_url']})

            minPricedItem = min(price, key=lambda x: float(x['price']))
            store_name = ''
            if 'amazon' in minPricedItem['url'].lower():
                store_name = 'Amazon'
            elif 'myntra' in minPricedItem['url'].lower():
                store_name = 'Myntra'
            elif 'flipkart' in minPricedItem['url'].lower():
                store_name = 'Flipkart'
            result_label.config(text='Cheapest Price: Rs. {} at {}'.format(minPricedItem['price'], store_name))
            price = []

    except Exception as e:
        messagebox.showerror("Error", "An error occurred while fetching data: {}".format(str(e)))

# Create the main window
root = tk.Tk()
root.geometry('830x400')
root.title("Price Comparison Tool")

background_image = Image.open("/home/sanchia/Desktop/sanchia/adp/arrangement-black-friday-shopping-carts-with-copy-space.jpg")
background_photo = ImageTk.PhotoImage(background_image)

background_label = ttk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


heading = ttk.Label(root, text="ENTER URL TO COMPARE PRICES", font="Tisa 30 bold")
heading.place(x=60, y=20)


# Create and configure the URL entry fields
url1_label = ttk.Label(root, text="Enter Product URL 1:")
url1_label.pack()
url1_label.place(x=350, y=90)
url1_entry = ttk.Entry(root, width=50)
url1_entry.pack()
url1_entry.place(x=200, y=120)

url2_label = ttk.Label(root, text="Enter Product URL 2:")
url2_label.pack()
url2_label.place(x=350, y=150)
url2_entry = ttk.Entry(root, width=50)
url2_entry.pack()
url2_entry.place(x=200, y=180)

url3_label = ttk.Label(root, text="Enter Product URL 3:")
url3_label.pack()
url3_label.place(x=350, y=210)
url3_entry = ttk.Entry(root, width=50)
url3_entry.pack()
url3_entry.place(x=200, y=240)

# Create and configure the fetch button
fetch_button = ttk.Button(root, text="Fetch Cheapest Price", command=fetch_cheapest_price)
fetch_button.pack()
fetch_button.place(x=350, y=290)

# Create and configure the result label
result_label = ttk.Label(root, text="")
result_label.pack()
result_label.place(x=300, y=320)

# Run the Tkinter main loop
root.mainloop()