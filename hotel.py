import tkinter as tk
from tkinter import messagebox

# MenuItem class represents a single item on the menu
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

# Menu class contains a list of MenuItem objects
class Menu:
    def __init__(self):
        self.items = [
            MenuItem("Coffee", 2.50),
            MenuItem("Tea", 2.00),
            MenuItem("Sandwich", 5.00),
            MenuItem("Cake", 3.50),
             MenuItem("Coke", 4.50),
             MenuItem("pizza", 10.50),
             MenuItem("Burger", 9.50),
             MenuItem("Milkshake",7.50)
            # Add more items as needed
        ]

    def get_items(self):
        return self.items

# Order class manages the customer's order
class Order:
    def __init__(self):
        self.order_items = []

    def add_item(self, item):
        self.order_items.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.order_items)

    def get_order_summary(self):
        return "\n".join(str(item) for item in self.order_items)

# CafeApp class handles the graphical user interface
class CafeApp:
    GST_RATE = 0.18  # 18% GST

    def __init__(self, root):
        self.root = root
        self.root.title("DAS Restaurants ")
        self.root.geometry("400x500")
        self.menu = Menu()
        self.order = Order()

        # Display menu items
        self.menu_label = tk.Label(self.root, text="Menu", font=("Helvetica", 16, "bold"))
        self.menu_label.pack(pady=10)

        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack()

        self.create_menu_buttons()

        # Display order summary
        self.order_label = tk.Label(self.root, text="Your Order", font=("Helvetica", 16, "bold"))
        self.order_label.pack(pady=10)

        self.order_summary = tk.Text(self.root, height=10, width=40, state='disabled')
        self.order_summary.pack(pady=10)

        # Display total
        self.total_label = tk.Label(self.root, text="Total: $0.00", font=("Helvetica", 14, "bold"))
        self.total_label.pack(pady=10)

        # Display GST
        self.gst_label = tk.Label(self.root, text="GST (18%): $0.00", font=("Helvetica", 14, "bold"))
        self.gst_label.pack(pady=10)

        # Display grand total (Total + GST)
        self.grand_total_label = tk.Label(self.root, text="Grand Total: $0.00", font=("Helvetica", 16, "bold"))
        self.grand_total_label.pack(pady=10)

        # Checkout button
        self.checkout_button = tk.Button(self.root, text="Checkout", command=self.checkout, font=("Helvetica", 14, "bold"))
        self.checkout_button.pack(pady=20)

    def create_menu_buttons(self):
        for item in self.menu.get_items():
            button = tk.Button(self.menu_frame, text=str(item), width=30, command=lambda i=item: self.add_to_order(i))
            button.pack(pady=5)

    def add_to_order(self, item):
        self.order.add_item(item)
        self.update_order_summary()
        self.update_total()

    def update_order_summary(self):
        self.order_summary.config(state='normal')
        self.order_summary.delete(1.0, tk.END)
        self.order_summary.insert(tk.END, self.order.get_order_summary())
        self.order_summary.config(state='disabled')

    def update_total(self):
        total = self.order.calculate_total()
        gst = total * self.GST_RATE
        grand_total = total + gst

        self.total_label.config(text=f"Total: ${total:.2f}")
        self.gst_label.config(text=f"GST (18%): ${gst:.2f}")
        self.grand_total_label.config(text=f"Grand Total: ${grand_total:.2f}")

    def checkout(self):
        total = self.order.calculate_total()
        gst = total * self.GST_RATE
        grand_total = total + gst
        messagebox.showinfo("Checkout", f"Your total is: ${total:.2f}\nGST (18%): ${gst:.2f}\nGrand Total: ${grand_total:.2f}\nThank you for your order!")
        self.root.quit()

# Running the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CafeApp(root)
    root.mainloop()
