"""Module providingFunction printing python version."""

import sys
import glob
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import utils
import std

def main(json_files_param, co2_data_param, command_param):
    """Main function."""
    # Your function logic here
    path = json_files_param
    files = list(glob.glob(path + '**/*.json', recursive=True))
    df_co2 = pd.read_csv(co2_data_param)
    df_final = utils.create_final_df(files, df_co2)
    # take only the first part of this return value
    trend_co2, *_ = std.decompose_time_series(df_final)
    df_final['trend_co2'] = trend_co2
    df_final['trend_co2'] = df_final['trend_co2'].fillna(0)
    lin_reg = LogisticRegression()
    input_columns = ['time_hours', 'trend_co2']
    target_column = 'occupancy'
    if command_param == 'train':
        lin_reg.fit(df_final[input_columns], df_final[target_column])
        utils.save_model(lin_reg, 'model.pkl')
    elif command_param == 'run':
        lin_reg = utils.load_model('model.pkl')
        predictions = lin_reg.predict(df_final[input_columns])
        accuracy = accuracy_score(df_final[target_column], predictions)
        print(accuracy)
    else:
        print('Unknown command')
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python main.py json_files co2_data train/run")
        sys.exit(1)

    JSON_FILES = sys.argv[1]
    CO2_DATA = sys.argv[2]
    COMMAND = sys.argv[3]

    main(JSON_FILES, CO2_DATA, COMMAND)
    