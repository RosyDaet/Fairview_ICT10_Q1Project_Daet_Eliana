from pyscript import display, document

    # The Menu item being inputted by user 
def calculate_receipt(e):
    item1 = document.getElementById('Item1')
    item2 = document.getElementById('Item2')
    item3 = document.getElementById('Item3')
    item4 = document.getElementById('Item4')

    #
    subtotal1 = float(item1.value) * item1.checked + float(item2.value) * item2.checked
    subtotal2 = float(item3.value) * item3.checked + float(item4.value) * item4.checked

    # VAT rate to 0.12 or 12% 
    tax_rate = 0.12

    #caluculation used to get subtotal 
    subtotal = subtotal1 + subtotal2

    #caluculation used to get the Vat amount of the menu item  
    vat_amount = subtotal * tax_rate

    # THe total amount of the itmes
    total_amount = subtotal + vat_amount

    display(
        f"Subtotal: ₱{subtotal:.2f}<br>"
        f"VAT: ₱{vat_amount:.2f}<br>"
        f"Total Amount: ₱{total_amount:.2f}",
        target='result'
    )


def generate_SKU(e):
    product_category = document.getElementById('Category').value
    product_name = document.getElementById('Product').value
    stock_quantity = document.getElementById('Quantity').value

    #used to get the SKU
    SKU = product_category[:3].upper() + "-" + product_name[:4].upper() + "-" + str(stock_quantity)

    #code used to display 
    display("SKU: ", generate_SKU, target='Generater')



