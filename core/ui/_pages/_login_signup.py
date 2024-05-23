from snowflake.snowpark import Row
from hashlib import sha256

import streamlit as st

from core.ui._pages.abc import PageABC


class LoginSignupPage(PageABC):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self._create_account_table()

	@property
	def title(self) -> str:
		return "Login / Sign-up"

	def _create_account_table(self) -> None:
		self.session.sql(
			"""
			CREATE TABLE IF NOT EXISTS ACCOUNT_TABLE(
					user VARCHAR,
					password_hash VARCHAR
			)
			"""
		).collect()

	def _create_new_user(
		self,
		username: str,
		password: str,
	) -> None:
		self.session.sql(
			f"""
			INSERT INTO ACCOUNT_TABLE VALUES('{username}', '{password}')
			"""
		).collect()

	def _log_in_user(
		self,
		username: str,
		password_hash: str,
	) -> list[Row]:
		dataframe = self.session.sql(
			f"""
			SELECT * FROM ACCOUNT_TABLE WHERE USER = '{username}' AND PASSWORD = '{password_hash}'
			"""
		).collect()
		return dataframe

	def run(self) -> None:
		st.title(self.title)

		username = st.text_input("Username")
		password = st.text_input("Password", type='string')
		password_hash = self._string_sha256(password)

		if st.button("Login"):
			result = self._log_in_user(
				username=username,
				password_hash=password_hash,
			)
			if result:
				st.success(f"Logged in as {username}")
			else:
				st.warning("Incorrect username or password")

		if st.button("Sign-up"):
			self._log_in_user(
				username=username,
				password_hash=password_hash,
			)
			st.success("You have successfully created an account")

	@staticmethod
	def _string_sha256(__string: str) -> str:
		__string = str.encode(__string)
		__string = sha256(__string)
		__string = __string.hexdigest()
		return __string
