def receipt_formatter(name, quantity, price):
    if quantity <= 0:
        return "Invalid quantity."

    if price < 0:
        return "Invalid price."

    subtotal = quantity * price
    tax = subtotal * 0.075
    total = subtotal + tax

    return f"""Customer: {name}
Subtotal: {subtotal:.2f}
Tax: {tax:.2f}
Total: {total:.2f}"""

# :.2f = display a number with 2 decimal places.
# An f-string allows us to put variables inside the string using {}.
# """ This is called a multiline string.

print(receipt_formatter("Chioma", 5, 50))
print()
print(receipt_formatter("Adesua", 5, 500))


