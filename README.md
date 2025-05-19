# Coffee Shop

## Project Overview

This project models a simple coffee ordering system with three core classes:  
- *Customer* — represents a customer with a validated name.  
- *Coffee* — represents a coffee type with validation on the name.  
- *Order* — links a customer and a coffee with a price, with validation on all inputs.

The system manages relationships between customers, coffees, and orders, allowing you to:  
- Create orders for customers and coffees  
- Track all orders of a specific coffee or customer  
- Calculate stats like average coffee price and number of orders  
- Identify the "most aficionado" customer for a particular coffee (the customer who spent the most)

## Features

- Validation of input data (e.g., customer name length, coffee name length, price range)  
- Methods to retrieve related orders and customers/coffees for analytics  
- Aggregate methods for calculating order counts and average prices  


## Installation & Setup

1. Clone the repository:  
   `git clone <repository-url>`

2. Navigate to the project directory:  
   `cd coffee_shop`

3. (Optional) Create and activate a Python virtual environment:  
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

   Install dependencies 
   pip install pytest

   Runt the tests using **pytest**


