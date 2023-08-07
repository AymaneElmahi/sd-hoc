"""Module providingFunction printing python version."""

def decompose_time_series(df_):
    """
    Decompose time series into trend, seasonal and irregular components
    :param df_: pandas dataframe
    :return: None
    """
    # Step 1: Calculate 2 × 12 moving average in the raw data
    trend_co2 = df_['co2'].rolling(window=12, center=True).mean()
    trend_occupancy = df_['peoplecount_rgb'].rolling(window=12, center=True).mean()

    # Step 2: Calculate centred ratios
    centred_ratios_co2 = df_['co2'] / trend_co2
    centred_ratios_occupancy = df_['peoplecount_rgb'] / trend_occupancy

    for _ in range(2):
        # Step 3: Calculate rough seasonal feature
        seasonal_co2 = centred_ratios_co2.rolling(window=2).mean().rolling(window=2).mean()
        seasonal_occupancy = centred_ratios_occupancy.rolling(
            window=2).mean().rolling(window=2).mean()

        # Step 4: Calculate irregular feature
        et_co2 = centred_ratios_co2 / seasonal_co2
        et_occupancy = centred_ratios_occupancy / seasonal_occupancy

        # Step 5: Modify irregular feature by multiplying with seasonal feature
        modified_et_co2 = et_co2 * seasonal_co2
        modified_et_occupancy = et_occupancy * seasonal_occupancy

        # Step 6: Update seasonal feature
        seasonal_co2 = modified_et_co2.rolling(window=2).mean().rolling(window=2).mean()
        seasonal_occupancy = modified_et_occupancy.rolling(window=2).mean().rolling(window=2).mean()

        # Step 7: Calculate preliminary seasonal adjusted series
        preliminary_seasonal_adjusted_co2 = df_['co2'] / seasonal_co2
        preliminary_seasonal_adjusted_occupancy = df_['peoplecount_rgb'] / seasonal_occupancy

        # Step 8: Estimate trend feature using weighted Henderson moving average
        trend_co2 = preliminary_seasonal_adjusted_co2.rolling(window=12,
                                                              center=True).mean()
        trend_occupancy = preliminary_seasonal_adjusted_occupancy.rolling(window=12,
                                                                          center=True).mean()

        # Step 9: Calculate new centred ratios
        centred_ratios_co2 = df_['co2'] / trend_co2
        centred_ratios_occupancy = df_['peoplecount_rgb'] / trend_occupancy

        for _ in range(2):
            # Step 10: Calculate rough seasonal feature using 3 × 5 moving average
            seasonal_co2 = centred_ratios_co2.rolling(
                window=3,center=True).mean().rolling(window=5, center=True).mean()
            seasonal_occupancy = centred_ratios_occupancy.rolling(
                window=3, center=True).mean().rolling(window=5, center=True).mean()

            # Step11:Update irregular feature using modified centred ratios and 3×5 moving average
            et_co2 = centred_ratios_co2 / seasonal_co2
            et_occupancy = centred_ratios_occupancy / seasonal_occupancy

            modified_et_co2 = et_co2 * seasonal_co2
            modified_et_occupancy = et_occupancy * seasonal_occupancy

            # Step 12: Update seasonal feature using 3 × 5 moving average
            seasonal_co2 = modified_et_co2.rolling(
                window=3, center=True).mean().rolling(window=5, center=True).mean()
            seasonal_occupancy = modified_et_occupancy.rolling(
                window=3, center=True).mean().rolling(window=5, center=True).mean()

            # Step 13: Calculate reminder feature
            reminder_feature_co2 = preliminary_seasonal_adjusted_co2 / trend_co2
            reminder_feature_occupancy = preliminary_seasonal_adjusted_occupancy / trend_occupancy
    return (trend_co2, trend_occupancy, seasonal_co2, seasonal_occupancy, reminder_feature_co2,
            reminder_feature_occupancy)
