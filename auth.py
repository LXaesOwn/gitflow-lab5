def authenticate_user(username, password):
    # Simplified authentication
    return username == 'admin' and password == 'password'
def logout_user():
    print('User logged out')
