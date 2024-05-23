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


def get_points(results_dataframe: pd.DataFrame) -> pd.DataFrame:
    results_dataframe_with_points = results_dataframe.copy()
    first_place_points = get_number_of_points_for_first_place(results_dataframe_with_points)
    results_dataframe_with_points['points'] = first_place_points / results_dataframe_with_points['rank_position']
    return results_dataframe_with_points
