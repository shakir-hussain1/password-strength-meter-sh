import streamlit as st
import re
import random
import string

# Define common weak passwords for blacklist
common_passwords = ["password123", "123456", "qwerty", "abc123", "letmein", "password", "welcome", "admin"]

#Styling
st.markdown(
    """
<style>
.stApp{
    background-color: lightblue;
    color:black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to evaluate password strength
def evaluate_password(password):
    # Criteria 1: Length check
    if len(password) < 8:
        score = 1
        feedback = "Password is too short. It should be at least 8 characters."
        return score, feedback
    
    # Criteria 2: Uppercase and lowercase letters check
    if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
        score = 2
        feedback = "Password must contain both uppercase and lowercase letters."
        return score, feedback
    
    # Criteria 3: Digit check
    if not re.search(r'\d', password):
        score = 3
        feedback = "Password must contain at least one digit (0-9)."
        return score, feedback
    
    # Criteria 4: Special character check
    if not re.search(r'[!@#$%^&*]', password):
        score = 4
        feedback = "Password must include at least one special character: !@#$%^&*."
        return score, feedback
    
    # Criteria 5: Check if password is a common one (blacklist check)
    if password.lower() in common_passwords:
        score = 2
        feedback = "Password is too common. Please choose a unique password."
        return score, feedback

    # If all criteria are met, it's strong
    score = 5
    feedback = "Password is strong!"
    return score, feedback

# Function to suggest a strong password
def generate_strong_password():
    # Creating a strong password with 12 characters
    length = 12
    password = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=length))
    
    return password

# Streamlit app layout
def password_strength_meter():
    st.title("Password Strength Meter")
    st.write("Evaluate the strength of your password based on various security criteria.")
    
    # User input for password
    password = st.text_input("Enter your password:")
    
    if password:
        # Evaluate password strength
        score, feedback = evaluate_password(password)
        
        # Display feedback and score
        st.write(f"### Password Score: {score}")
        st.write(f"Feedback: {feedback}")
        
        if score < 5:
            st.write("### Suggestions to improve your password:")
            st.write("- Make sure your password is at least 8 characters long.")
            st.write("- Include both uppercase and lowercase letters.")
            st.write("- Add at least one digit (0-9).")
            st.write("- Use one or more special characters (e.g., !@#$%^&*).")
            st.write("- Avoid common passwords.")
        
        # If the password is strong, offer a suggestion for a new strong password.
        if score == 5:
            st.write("### Your password is strong! Great job!")
            st.write(f"Suggested strong password (for reference): **{generate_strong_password()}**")
    else:
        st.write("Please enter a password to evaluate its strength.")

# Run the app
if __name__ == "__main__":
    password_strength_meter()
