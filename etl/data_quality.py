def get_data_quality(df):
    report = {
        "Rows": int(df.shape[0]),
        "Columns": int(df.shape[1]),
        "Duplicate Rows": int(df.duplicated().sum()),
        "Missing Values": int(df.isnull().sum().sum())
    }

    return report