def make_shirt(size, info):
    """Display details of the T-shirt"""
    print(f"\nT-shirt you ordered is : {size.upper()}.")
    print(f"And the message on it is: {info.title()}.")

make_shirt('xl', 'i love physics')
make_shirt(info='i love math', size='large')