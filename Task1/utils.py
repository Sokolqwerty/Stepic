def get_name(user):
    return user[0]

def sort_user_data(data):
    return sorted(data, key=get_name)