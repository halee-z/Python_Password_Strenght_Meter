import streamlit as st
import re

# Password strength function
def password_strength(password):
    if len(password) < 8:
        return "Weak: Password is too short"
    
    if not re.search("[a-z]", password):
        return "Weak: Password must contain at least one lowercase letter"
    
    if not re.search("[A-Z]", password):
        return "Weak: Password must contain at least one uppercase letter"
    
    if not re.search("[0-9]", password):
        return "Weak: Password must contain at least one digit"
    
    if not re.search("[@#$%^&+=]", password):
        return "Weak: Password must contain at least one special character"
    
    return "Strong: Your password is strong!"

# Streamlit app interface
st.title('Password Strength Meter')
st.write("Enter a password to check its strength:")

# Password input field
password = st.text_input("Password", type="password")

# Show strength of the password
if password:
    result = password_strength(password)
    st.write(result)
