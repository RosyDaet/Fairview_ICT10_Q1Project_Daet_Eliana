
from pyscript import display, document


def calculate_receipt(e):
    # Store the button-click event passed to this function.

    # Retrieve the four menu item input elements from the HTML page.
    item1 = document.getElementById("Item1")
    item2 = document.getElementById("Item2")
    item3 = document.getElementById("Item3")
    item4 = document.getElementById("Item4")

    # Calculate the subtotal of the first two menu items.
    subtotal1 = (
        float(item1.value) * item1.checked
        + float(item2.value) * item2.checked
    )

    # Calculate the subtotal of the last two menu items.
    subtotal2 = (
        float(item3.value) * item3.checked
        + float(item4.value) * item4.checked
    )

    # Store the VAT rate as a decimal representing 12 percent.
    tax_rate = 0.12

    # Calculate the combined price of all selected menu items.
    subtotal = subtotal1 + subtotal2

    # Calculate the VAT amount based on the subtotal.
    vat_amount = subtotal * tax_rate

    # Calculate the final total including VAT.
    total_amount = subtotal + vat_amount

    # Display the receipt with line breaks and two decimal places.
    display(
    f"Subtotal: ₱{subtotal:.2f}\n"
    f"VAT (12%): ₱{vat_amount:.2f}\n"
    f"Total Amount: ₱{total_amount:.2f}",
    target="result"
)


def generate_sku(e):
    # Store the button-click event passed to this function.

    # Retrieve the product category entered on the HTML page.
    product_category = document.getElementById("Category").value.strip()

    # Retrieve the product name entered on the HTML page.
    product_name = document.getElementById("Product").value.strip()

    # Retrieve the stock quantity entered on the HTML page.
    stock_quantity = document.getElementById("Quantity").value.strip()

    # Check whether all required input fields contain values.
    if not product_category or not product_name or not stock_quantity:
        # Display an error message if an input is missing.
        display(
            "Please enter the category, product, and quantity.",
            target="Generater"
        )
        return

    try:
        # Convert the entered quantity into a whole number.
        quantity = int(stock_quantity)

        # Ensure the quantity is greater than zero.
        if quantity <= 0:
            display(
                "Quantity must be greater than zero.",
                target="Generater"
            )
            return

    except ValueError:
        # Display an error if the quantity is not a whole number.
        display(
            "Please enter a valid whole-number quantity.",
            target="Generater"
        )
        return

    # Generate the SKU using the first three category letters,
    # the first four product letters, and the stock quantity.
    sku = (
        product_category[:3].upper()
        + "-"
        + product_name[:4].upper()
        + "-"
        + str(quantity)
    )

    # Display the generated SKU string in the HTML output container.
    display(f"SKU: {sku}", target="Generater")
