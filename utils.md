def decompose_time_series(df):
    
    # calculate trend feature
    df_copy = df.copy()
    trend_co2 = calculate_moving_average(df_copy,'CO2')
    trend_peoplecount = calculate_moving_average(df_copy,'peoplecount_rgb')
    centred_ratios_co2 = df_copy['CO2'] / trend_co2
    centred_ratios_peoplecount = df_copy['peoplecount_rgb'] / trend_peoplecount
    
    # calculate seasonal feature
    # To form a rough seasonal feature (St) data estimation, apply separate 2 × 2
    # moving average to each month of the centred ratios.
    
    # calculate the seasonal feature for co2
    seasonal_co2 = centred_ratios_co2.rolling(window=2).mean().rolling(window=2).mean()
    seasonal_co2 = seasonal_co2.fillna(1)
    
    # calculate the seasonal feature for peoplecount
    seasonal_peoplecount = centred_ratios_peoplecount.rolling(window=2).mean().rolling(window=2).mean()
    seasonal_peoplecount = seasonal_peoplecount.fillna(1)
    
    # calculate the residual feature
    residual_co2 = centred_ratios_co2 / seasonal_co2
    residual_peoplecount = centred_ratios_peoplecount / seasonal_peoplecount
    
    # modified centred ratios
    modified_centred_ratios_co2 = residual_co2 * trend_co2
    modified_centred_ratios_peoplecount = residual_peoplecount * trend_peoplecount
    
    # repeat to obtain the revised seasonal feature
    seasonal_co2 = modified_centred_ratios_co2.rolling(window=2).mean().rolling(window=2).mean()
    seasonal_co2 = seasonal_co2.fillna(1)
    
    seasonal_peoplecount = modified_centred_ratios_peoplecount.rolling(window=2).mean().rolling(window=2).mean()
    seasonal_peoplecount = seasonal_peoplecount.fillna(1)
      
    seasonal_adjusted_co2 = df_copy['CO2'] / seasonal_co2
    seasonal_adjusted_peoplecount = df_copy['peoplecount_rgb'] / seasonal_peoplecount

    trend_adjusted_co2 = seasonal_adjusted_co2.rolling(window=12).mean().rolling(window=2).mean()
    trend_adjusted_peoplecount = seasonal_adjusted_peoplecount.rolling(window=12).mean().rolling(window=2).mean()
        
    new_ratios_co2 = df_copy['CO2'] / trend_adjusted_co2
    new_ratios_peoplecount = df_copy['peoplecount_rgb'] / trend_adjusted_peoplecount
    
    # Repeat Steps 3 to 5 using the new ratios and applying a 3 × 5 moving average
    # instead of a 3 × 3 moving average.