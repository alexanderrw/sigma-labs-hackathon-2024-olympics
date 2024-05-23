import pandas as pd
import streamlit as st


from .abc import PageABC


class LeaderboardPage(PageABC):
    @property
    def title(self) -> str:
        return "Leaderboard"

    def run(self) -> None:
        st.title("Leaderboard")

        # Dummy data to test usability
        data = {
            "Username": ["user1", "user2", "user3"],
            "Score": [300, 250, 245]
        }
        leaderboard_df = pd.DataFrame(data)
        if self.session.current_user_id:
            st.subheader("Leaderboard Section")
            st.write("Here are the top performers:")
            st.table(leaderboard_df.sort_values(by="Score", ascending=False))
        else:
            st.error("You need to be logged in to view the leaderboard.")