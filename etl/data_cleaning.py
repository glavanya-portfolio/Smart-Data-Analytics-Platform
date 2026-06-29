import pandas as pd
def remove_duplicates(df):
    """
    Removes duplicate rows from the dataset.
    Returns cleaned dataframe and number of rows removed.
    """

    before_rows = len(df)

    df = df.drop_duplicates()

    after_rows = len(df)

    duplicates_removed = before_rows - after_rows

    return df, duplicates_removed

def remove_extra_spaces(df):
    """
    Removes leading and trailing spaces from text columns.
    """

    text_columns = df.select_dtypes(include="object").columns

    for column in text_columns:
        df[column] = df[column].str.strip()

    return df
def standardize_text(df):
    """
    Converts all text columns to Proper Case.
    """

    text_columns = df.select_dtypes(include="object").columns

    for column in text_columns:
        df[column] = df[column].str.title()

    return df

def convert_date_columns(df):
    """
    Automatically detects and converts date columns.
    """

    for column in df.columns:

        if "date" in column.lower():

            df[column] = pd.to_datetime(
                df[column],
                errors="coerce"
            )

    return df

def handle_missing_values(df):
    """
    Handles missing values based on column data type.
    """

    for column in df.columns:

        # Numeric columns
        if pd.api.types.is_numeric_dtype(df[column]):
            df[column] = df[column].fillna(df[column].median())

        # Text columns
        elif pd.api.types.is_string_dtype(df[column]) or df[column].dtype == "object":
            df[column] = df[column].fillna("Unknown")

    return df
def clean_data(df):
    """
    Complete ETL Pipeline
    """

    df, duplicates_removed = remove_duplicates(df)

    df = remove_extra_spaces(df)

    df = standardize_text(df)

    df = convert_date_columns(df)

    df = handle_missing_values(df)

    summary = {
        "Duplicate Rows Removed": duplicates_removed
    }

    return df, summary