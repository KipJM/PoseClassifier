def preprocess(df):
    # Normalize data
    pose_mean = df.stack().mean()
    pose_std = df.stack().std()
    df = (df - pose_mean) / pose_std
    return df
