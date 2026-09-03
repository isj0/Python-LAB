def make_sandwich(*items):
    """Print the sandwich and its item details."""
    print(f"\nMaking a Sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich('cream cheese', 'pesto')
make_sandwich('cream cheese', 'sun dried tomatoes', 'cheese', 'pesto')
make_sandwich('butter', 'tomatoes', 'cucumbers')