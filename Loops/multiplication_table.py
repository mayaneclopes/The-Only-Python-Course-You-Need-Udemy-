# You are developing a feature in an educational app that displays multiplication tables.
# Tasks:
# Write a function named multiplication_table that takes a single integer argument number.
# Using a for loop and range(), generate the multiplication table for number from 1 to 10.
# Return a list of strings in the following format:
# "number x i = result"
# (Example: "3 x 4 = 12")

def generate_invoice(customer_name: str = "Guest", *items: str, **charges: float) -> str:
    total = 0.0
    invoice_lines = [f"Invoice for {customer_name}:"]
 
    if items:
        invoice_lines.append("Items:")
        for item in items:
            invoice_lines.append(f"- {item}")
 
    if charges:
        invoice_lines.append("Charges:")
        for label, amount in charges.items():
            invoice_lines.append(f"{label.capitalize()}: {amount}")
            total += amount
 
    invoice_lines.append(f"Total Amount Due: {total}")
    return "\\n".join(invoice_lines)

generate_invoice("Amit", "Burger", "Fries", tax=50.0, service=20.00)
print(generate_invoice)