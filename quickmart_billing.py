cart = [
    {"name": "Notebook", "category": "Stationery", "price": 40, "qty": 5},
    {"name": "Pen", "category": "Stationery", "price": 10, "qty": 11},
    {"name": "Biscuits", "category": "Snacks", "price": 25, "qty": 4},
    {"name": "Juice", "category": "Drinks", "price": 45, "qty": 3},
    {"name": "Chips", "category": "Snacks", "price": 20, "qty": 6},
]
 
 
def line_total(item):
    """Return price x qty of one item."""
    return item["price"] * item["qty"]
 
 
def subtotal(cart):
    """Return the sum of all line totals."""
    return sum(line_total(item) for item in cart)
 
 
def apply_discount(amount, percent=0):
    """Return the amount after reducing it by percent."""
    return amount - (amount * percent / 100)
 
 
def gst(amount, rate=18):
    """Return the GST on the amount."""
    return amount * rate / 100
 
 
def category_totals(cart):
    """Return a dictionary of category -> total value."""
    totals = {}
    for item in cart:
        category = item["category"]
        totals[category] = totals.get(category, 0) + line_total(item)
    return totals
 
 
def top_items(cart, n=2):
    """Return the names of the n items with the highest line total."""
    ranked = sorted(cart, key=line_total, reverse=True)
    return [item["name"] for item in ranked[:n]]
 
 
def print_bill(cart, discount_percent=0):
    """Print the bill table and the summary."""
    print(f"{'Item':<10}{'Price':>6}{'Qty':>5}{'Total':>8}")
    print("-" * 29)
    for item in cart:
        print(f"{item['name']:<10}{item['price']:>6}{item['qty']:>5}{line_total(item):>8}")
    print("-" * 29)
 
    sub = subtotal(cart)
    discounted = apply_discount(sub, discount_percent)
    discount_amount = sub - discounted
    tax = gst(discounted)
    grand = discounted + tax
 
    print(f"{'Subtotal':<21}{sub:>8.2f}")
    print(f"{f'Discount {discount_percent}%':<21}{discount_amount:>8.2f}")
    print(f"{'GST 18%':<21}{tax:>8.2f}")
    print(f"{'Grand total':<21}{grand:>8.2f}")
 
 
def main():
    print("Task 1: Line total")
    print(line_total(cart[0]))
    print()
 
    print("Task 2: Subtotal")
    print(subtotal(cart))
    print()
 
    print("Task 3: Discount")
    print(apply_discount(500))
    print(apply_discount(500, 10))
    print()
 
    print("Task 4: GST")
    print(gst(100))
    print(gst(100, 5))
    print()
 
    print("Task 5: Category totals")
    totals = category_totals(cart)
    for category in sorted(totals):
        print(f"{category:<12}{totals[category]}")
    print()
 
    print("Task 6: Top items")
    print(top_items(cart))
    print(top_items(cart, 3))
    print()
 
    print("Task 7: Bill")
    print_bill(cart, 10)
    print()
 
    print("Task 8: Tests")
    assert line_total(cart[0]) == 200
    assert apply_discount(200, 50) == 100
    assert gst(200) == 36
    assert top_items(cart, 1) == ["Notebook"]
    print("All tests passed")
 
 
if __name__ == "__main__":
    main()
 