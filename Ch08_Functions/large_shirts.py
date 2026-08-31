def make_shirt(size='large', info='i love python'):
    """Display details of the T-shirt"""
    print(f"\nT-shirt you ordered is : {size.upper()}.")
    print(f"And the message on it is: {info.title()}.")

make_shirt('xl', 'i love physics')
make_shirt(info='i love math', size='large')
make_shirt(size='small', info='i love tech')
make_shirt()