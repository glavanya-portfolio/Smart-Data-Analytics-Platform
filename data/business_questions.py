def answer_question(df, question):
    question = question.lower()

    numeric_cols = df.select_dtypes(include=['int64','float64']).columns
    text_cols = df.select_dtypes(include=['object']).columns

    # TOTAL / SUM type
    if "total" in question or "sum" in question:
        for col in numeric_cols:
            if col.lower() in question:
                return f"Total {col}: {df[col].sum()}"

    # AVERAGE type
    if "average" in question or "mean" in question:
        for col in numeric_cols:
            if col.lower() in question:
                return f"Average {col}: {df[col].mean()}"

    # MAX / HIGHEST
    if "highest" in question or "max" in question:
        for col in numeric_cols:
            if col.lower() in question:
                max_row = df.loc[df[col].idxmax()]
                return f"Highest {col} is {max_row[col]}"

    # MIN / LOWEST
    if "lowest" in question or "min" in question:
        for col in numeric_cols:
            if col.lower() in question:
                min_row = df.loc[df[col].idxmin()]
                return f"Lowest {col} is {min_row[col]}"

    # TOP CATEGORY (text columns)
    if "top" in question or "most" in question:
        for col in text_cols:
            if col.lower() in question:
                return df[col].value_counts().head(1).to_string()

    return "Sorry, I cannot understand this question with current dataset."