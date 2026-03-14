def transform_data(df):

    print("Transforming data...")

    top_skills = df["skill_abr"].value_counts().head(10)

    return top_skills