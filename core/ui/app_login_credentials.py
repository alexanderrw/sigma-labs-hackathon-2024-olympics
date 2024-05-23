import hashlib 
import pandas as pd
import streamlit as st
import snowflake

## password privacy function
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False

# Adding in Snowflake steps

session = Snowflake.session


# login functions

def accountTableCreator():
	session.sql("""
    CREATE TABLE IF NOT EXISTS ACCOUNT_TABLE(
            user VARCHAR,
            password VARCHAR
    )
    """).collect()

def insertUser(username, password):
	session.sql(f"""
        INSERT INTO ACCOUNT_TABLE VALUES('{username}', '{password}')
    """).collect()

def loginAttempt(username,pw):
	data = session.sql(f"SELECT * FROM ACCOUNT_TABLE WHERE USER = '{username}' AND PASSWORD = '{pw}'").collect()
	return data

# may not be needed
def viewUsers():
	data = session.sql("SELECT * FROM ACCOUNT_TABLE").collect()
	return data


def main():
	"""Simple Login App"""

	st.title("Simple Login App")

	menu = ["Home","Login","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")

	elif choice == "Login":
		st.subheader("Login Section")

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.button("Login"):
			# if password == '12345':
			accountTableCreator()
			hashed_pswd = make_hashes(password)

			result = loginAttempt(username,check_hashes(password,hashed_pswd))
			if result != []:

				st.success("Logged In as {}".format(username))
			else:
				st.warning("Incorrect Username/Password")





	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			accountTableCreator()
			insertUser(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")



if __name__ == '__main__':
	main()