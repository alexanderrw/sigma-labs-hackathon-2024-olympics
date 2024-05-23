import pandas as pd


def get_number_of_points_for_first_place(results_dataframe: pd.DataFrame) -> float:
    number_of_competitors = len(results_dataframe)
    capped_number_of_competitors = min(number_of_competitors, 8)
    total_points_available = 10 * capped_number_of_competitors

    total_multiplier = 0
    for competitor_number in range(capped_number_of_competitors):
        total_multiplier += 1 / (1 + competitor_number)

    first_place_points = total_points_available / total_multiplier
    return first_place_points


def get_available_points(results_dataframe: pd.DataFrame) -> pd.Series:
    results_dataframe_with_points = results_dataframe.copy()
    first_place_points = get_number_of_points_for_first_place(results_dataframe_with_points)
    return first_place_points / results_dataframe_with_points['rank_position']

def get_user_correct_answers(user_prediction: pd.DataFrame, event_id):
    session.sql("""
        SELECT (
            CASE WHEN SELECTIONS.SELECTION_RANKING = RESULTS.RANK_POSITION THEN 1
            ELSE 0
        )
            FROM ATHLETESELECTIONS_T AS SELECTIONS
            LEFT JOIN TOKYO_EVENTS AS RESULTS ON
                RESULTS.EVENT_ID = SELECTIONS.EVENT_ID AND
                RESULTS.ATHLETE_ID = SELECTIONS.ATHLETE_ID AND
            WHERE RESULTS.EVENT_ID = {event_id} AND SELECTIONS.USER_ID = {user_id}

         
    """)



