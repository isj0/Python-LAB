def build_profile(first, last, **user_info):
    """Build a dictionary with the details of a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info

user_profile = build_profile('John', 'Doe',
                             city='New York',
                             role='Engineer',
                             status='Level 3',
                             tenure=7)
print(user_profile)