from hashlib import sha256
from typing import Optional

import streamlit as st

from .abc import PageABC


class LoginSignupPage(PageABC):
	@property
	def title(self) -> str:
		return "Login / Sign-up"

	def _create_new_user(
		self,
		username: str,
		password_hash: str,
	) -> None:
		self.session.snowpark_session.sql(
			f"""
			INSERT INTO USERS_T(username, password_hash) VALUES('{username}', '{password_hash}')
			"""
		).collect()

	def _log_in_user(
		self,
		username: str,
		password_hash: str,
	) -> Optional[int]:
		current_user = self.session.snowpark_session.sql(
			f"""
			SELECT user_id FROM USERS_T WHERE username = '{username}' AND password_hash = '{password_hash}'
			QUALIFY row_number() OVER (
				ORDER BY lastupdated_timestamp DESC
			) = 1
			"""
		).collect()
		if not current_user:
			return None
		current_user_id = current_user[0][0]
		return current_user_id

	def run(self) -> None:
		st.title(self.title)

		def is_logged_in() -> bool:
			return bool(self.session.current_user_id)

		username = st.text_input(label="Username")
		password = st.text_input(
			label="Password",
			type="password",
		)
		password_hash = self._string_sha256(password)

		login_button = st.button(
			label="Login",
			disabled=is_logged_in(),
		)
		sign_up_button = st.button(
			label="Sign-up",
			disabled=is_logged_in(),
		)
		sign_out_button = st.button(
			label="Sign out",
			disabled=(not is_logged_in())
		)

		if login_button:
			user_id = self._log_in_user(
				username=username,
				password_hash=password_hash,
			)
			if user_id:
				st.success(f"Logged in as {username}")
				self.session.current_user_id = user_id
			else:
				st.warning("Incorrect username or password")

		if sign_up_button:
			self._create_new_user(
				username=username,
				password_hash=password_hash,
			)
			st.success("You have successfully created an account")

		if sign_out_button:
			self.session.current_user_id = None
			st.success("You have signed out")

	@staticmethod
	def _string_sha256(__string: str) -> str:
		__string = str.encode(__string)
		__string = sha256(__string)
		__string = __string.hexdigest()
		return __string
