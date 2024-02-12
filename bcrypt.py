import bcrypt

# Function to hash a password
def hash_password(password):
    # Generate a salt and hash the password using bcrypt
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

# Function to verify a password
def verify_password(password, hashed_password):
    # Check if the provided password matches the hashed password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

# Example usage:
password = "securepassword"
hashed_password = hash_password(password)
print("Hashed password:", hashed_password)

# Later, when verifying the password during login:
if verify_password(password, hashed_password):
    print("Password is correct!")
else:
    print("Incorrect password!")
