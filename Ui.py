import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

def fetch_amazon_details():
    url = amazon_url_entry.get()
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'}
    
    response = requests.get(url, headers=head)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find("span", attrs={'id':'productTitle'})
        price = soup.find("span", attrs={'class':'a-price-whole'})
        
        if title:
            amazon_title_label.config(text=f"Title: {title.text.strip()}")
        else:
            amazon_title_label.config(text="Title not found")
        
        if price:
            amazon_price_label.config(text=f"Price: ₹{price.text.strip()}")
        else:
            amazon_price_label.config(text="Price not found")
    else:
        messagebox.showerror("Error", f"Failed to retrieve the page. Status code: {response.status_code}")

def fetch_flipkart_details():
    url = flipkart_url_entry.get()
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'}
    
    response = requests.get(url, headers=head)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find("span", attrs={'class':'B_NuCI'})
        price = soup.find("div", attrs={'class':'_30jeq3 _16Jk6d'})
        
        if title:
            flipkart_title_label.config(text=f"Title: {title.text.strip()}")
        else:
            flipkart_title_label.config(text="Title not found")
        
        if price:
            flipkart_price_label.config(text=f"Price: ₹{price.text.strip()}")
        else:
            flipkart_price_label.config(text="Price not found")
    else:
        messagebox.showerror("Error", f"Failed to retrieve the page. Status code: {response.status_code}")

# Create the main window
root = tk.Tk()
root.title("Product Details Fetcher")

# Amazon URL input
amazon_url_label = tk.Label(root, text="Enter the Amazon Product link:")
amazon_url_label.pack(pady=5)
amazon_url_entry = tk.Entry(root, width=50)
amazon_url_entry.pack(pady=5)
fetch_amazon_button = tk.Button(root, text="Fetch Amazon Details", command=fetch_amazon_details)
fetch_amazon_button.pack(pady=5)

# Amazon product details
amazon_title_label = tk.Label(root, text="Title: ")
amazon_title_label.pack(pady=5)
amazon_price_label = tk.Label(root, text="Price: ")
amazon_price_label.pack(pady=5)

# Flipkart URL input
flipkart_url_label = tk.Label(root, text="Enter the Flipkart Product link:")
flipkart_url_label.pack(pady=5)
flipkart_url_entry = tk.Entry(root, width=50)
flipkart_url_entry.pack(pady=5)
fetch_flipkart_button = tk.Button(root, text="Fetch Flipkart Details", command=fetch_flipkart_details)
fetch_flipkart_button.pack(pady=5)

# Flipkart product details
flipkart_title_label = tk.Label(root, text="Title: ")
flipkart_title_label.pack(pady=5)
flipkart_price_label = tk.Label(root, text="Price: ")
flipkart_price_label.pack(pady=5)

# Run the main loop
root.mainloop()
