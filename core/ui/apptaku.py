import pandas as pd
import streamlit as st



# Set up the Streamlit page
st.set_page_config(layout='wide')
st.title("Olympic Fantasy Games Paris 2024")

# Simulated database of users and their scores
users = {
    "user1": "password1",
    "user2": "password2"
}

# Dummy data to test usability
data = {
    "Username": ["user1", "user2", "user3"],
    "Score": [300, 250, 245]
}
leaderboard_df = pd.DataFrame(data)

# our logging in
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['username'] = None

menu = ["Home", "Login", "SignUp", "Leaderboard", "Fantasy Home"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Home")
    

elif choice == "Login":
    if st.session_state['logged_in']:
        st.success(f"You are logged in as {st.session_state['username']}")
    else:
        st.subheader("Login Section")
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.button("Login"):
            if username in users and users[username] == password:
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.success(f"You are logged in as {username}")
            else:
                st.error("Incorrect username or password")

elif choice == "SignUp":
    st.subheader("Sign Up Section")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type='password')
    if st.button("Sign Up"):
        users[new_user] = new_password
        st.success("You have successfully signed up!")

elif choice == "Leaderboard":
    if st.session_state['logged_in']:
        st.subheader("Leaderboard Section")
        st.write("Here are the top performers:")
        st.table(leaderboard_df.sort_values(by="Score", ascending=False))
    else:
        st.error("You need to be logged in to view the leaderboard.")

elif choice == "Fantasy Home":
    if st.session_state['logged_in']:
        st.subheader("Fantasy Home Section")
        st.write("Fantasy home details go here...")
    else:
        st.error("You need to be logged in to view the fantasy home section.")
