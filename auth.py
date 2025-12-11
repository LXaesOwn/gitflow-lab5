def authenticate_user(username, password):
    # Fixed: Add password hashing
    import hashlib
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    stored_hash = '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'  # 'password' hash
    return username == 'admin' and hashed_password == stored_hash
