import pandas as pd
import numpy as np

def totalPoints(result_dataframe):
    if len(result_dataframe)>8:
        total_points = 8 * 10
    else:
        total_points = len(result_dataframe) * 10
    return total_points

def firstPlacePoints(result_dataframe):
    if len(result_dataframe) > 8:
        guess_number = 8
    else:
        guess_number = len(result_dataframe)
    total_points = totalPoints(result_dataframe)
    total_multiplier = 0
    for i in range(guess_number):
        total_multiplier += 1/(1+i)
    first_place_points = total_points/total_multiplier
    return first_place_points

def generatePoints(result_dataframe):
    first_place_points = firstPlacePoints(result_dataframe)
    result_dataframe['points'] = first_place_points/result_dataframe['rank_position']
    return result_dataframe