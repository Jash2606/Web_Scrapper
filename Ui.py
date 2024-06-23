import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

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
root.geometry("600x400")

# Apply some styles
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12), padding=10)
style.configure("TEntry", font=("Helvetica", 12), padding=10)
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TFrame", background="#f5f5f5")

main_frame = ttk.Frame(root, style="TFrame")
main_frame.pack(fill="both", expand=True)

# Amazon URL input
amazon_url_label = ttk.Label(main_frame, text="Enter the Amazon Product link:")
amazon_url_label.pack(pady=10)
amazon_url_entry = ttk.Entry(main_frame, width=50)
amazon_url_entry.pack(pady=5)
fetch_amazon_button = ttk.Button(main_frame, text="Fetch Amazon Details", command=fetch_amazon_details)
fetch_amazon_button.pack(pady=10)

# Amazon product details
amazon_title_label = ttk.Label(main_frame, text="Title: ")
amazon_title_label.pack(pady=5)
amazon_price_label = ttk.Label(main_frame, text="Price: ")
amazon_price_label.pack(pady=5)

# Flipkart URL input
flipkart_url_label = ttk.Label(main_frame, text="Enter the Flipkart Product link:")
flipkart_url_label.pack(pady=10)
flipkart_url_entry = ttk.Entry(main_frame, width=50)
flipkart_url_entry.pack(pady=5)
fetch_flipkart_button = ttk.Button(main_frame, text="Fetch Flipkart Details", command=fetch_flipkart_details)
fetch_flipkart_button.pack(pady=10)

# Flipkart product details
flipkart_title_label = ttk.Label(main_frame, text="Title: ")
flipkart_title_label.pack(pady=5)
flipkart_price_label = ttk.Label(main_frame, text="Price: ")
flipkart_price_label.pack(pady=5)

# Run the main loop
root.mainloop()
