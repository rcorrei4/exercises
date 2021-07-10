def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einsten',
                              location='princeton',
                              field='physics')

my_profile = build_profile('ricardo', 'santos',
                            age='16', weight='58',
                            location='São Paulo')

print(user_profile)
print(my_profile)