import tkinter as tk
from tkinter import messagebox

class Phoenix:
    def __init__(self, root):
        self.root = root
        self.root.title("Phoenix")
        self.root.geometry("600x400")

        self.create_main_page()

    def create_main_page(self):
        # Clear the root window
        self.clear_window()

        self.panel = tk.Frame(self.root, bg="pink", padx=20, pady=20)
        self.panel.pack(fill=tk.BOTH, expand=True)

        # Create labels and buttons for the landing page
        tk.Label(self.panel, text="Welcome to Phoenix", font=("Arial", 16, "bold"), bg="pink").pack(pady=20)
        tk.Button(self.panel, text="Manager", command=self.load_manager_page, font=("Arial", 14), bg="pink").pack(pady=10, expand=True, fill="both")
        tk.Button(self.panel, text="Sales Staff", command=self.load_sales_page, font=("Arial", 14), bg="pink").pack(pady=10, expand=True, fill="both")

    def load_manager_page(self):
        # Clear the root window
        self.clear_window()

        # Create and configure manager page
        self.panel = tk.Frame(self.root, bg="pink", padx=20, pady=20)
        self.panel.pack(fill=tk.BOTH, expand=True)

        tk.Label(self.panel, text="Manager Page", font=("Arial", 16, "bold"),bg="pink").pack(pady=20)
        tk.Button(self.panel, text="Load Stock Database", command=self.setup_stock, font=("Arial", 14)).pack(pady=10, expand=True, fill="both")
        tk.Button(self.panel, text="Check Unsold Stock Levels", command=self.check_unsold_stock, font=("Arial", 14)).pack(pady=10, expand=True, fill="both")
        tk.Button(self.panel, text="Calculate Payment Due", command=self.calculate_payment, font=("Arial", 14)).pack(pady=10, expand=True, fill="both")
        tk.Button(self.panel, text="Back to Main Page", command=self.create_main_page, font=("Arial", 14)).pack(pady=10, expand=True, fill="both")

    def load_sales_page(self):
        # Clear the root window
        self.clear_window()

        # Create and configure sales staff page
        self.panel = tk.Frame(self.root, bg="pink", padx=20, pady=20)
        self.panel.pack(fill=tk.BOTH, expand=True)

        tk.Label(self.panel, text="Sales Staff Page", font=("Arial", 16, "bold"),bg="pink").pack(pady=20)
        tk.Button(self.panel, text="Sell Item(s)", command=self.sell_items, font=("Arial", 14)).pack(pady=10, expand=True, fill="both")
        tk.Button(self.panel, text="Cancel Purchase", command=self.cancel_purchase, font=("Arial", 14)).pack(pady=10, expand=True, fill="both")
        tk.Button(self.panel, text="View Sold Totals", command=self.view_sold_totals, font=("Arial", 14)).pack(pady=10, expand=True, fill="both")
        tk.Button(self.panel, text="Back to Main Page", command=self.create_main_page, font=("Arial", 14)).pack(pady=10, expand=True, fill="both")

    def setup_stock(self):
        # Functionality for setting up and loading stock database
        messagebox.showinfo("Manager Action", "Load Stock Database")

    def check_unsold_stock(self):
        # Functionality for managers to check unsold stock levels
        messagebox.showinfo("Manager Action", "Check Unsold Stock Levels")

    def calculate_payment(self):
        # Functionality for managers to calculate payment due to the band
        messagebox.showinfo("Manager Action", "Calculate Payment Due")

    def sell_items(self):
        # Functionality for sales staff to sell items
        messagebox.showinfo("Sales Staff Action", "Sell Item(s)")

    def cancel_purchase(self):
        # Functionality for sales staff to cancel a purchase
        messagebox.showinfo("Sales Staff Action", "Cancel Purchase")

    def view_sold_totals(self):
        # Functionality for sales staff to view sold totals
        messagebox.showinfo("Sales Staff Action", "View Sold Totals")

    def clear_window(self):
        # Clear all widgets in the root window
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Phoenix(root)
    root.mainloop()
