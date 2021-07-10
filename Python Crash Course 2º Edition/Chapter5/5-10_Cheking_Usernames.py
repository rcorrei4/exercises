current_users = ['ana', 'bianca', 'riik', 'vic', 'thiago'] 
new_users = ['AnA', 'erick', 'igor', 'Riik', 'victoria']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f'Your username {new_user.lower()} is already in use!')
    else:
        print(f'Your username {new_user.lower()} is available!')