import pandas as pd


def generate_kpis(df, dataset_type):

    kpis = {}

    if dataset_type == "Sales Dataset":

        sales_keywords = [
            "sales",
            "sales amount",
            "revenue",
            "amount",
            "total sales"
        ]

        sales_column = None

        for column in df.columns:

            normalized_column = (
                column.strip()
                .lower()
                .replace("_", " ")
            )

            if normalized_column in sales_keywords:
                sales_column = column
                break

        if sales_column:

            kpis["Total Sales"] = round(df[sales_column].sum(), 2)
            kpis["Total Orders"] = len(df)
            kpis["Average Order Value"] = round(df[sales_column].mean(), 2)
            kpis["Highest Sale"] = round(df[sales_column].max(), 2)
            kpis["Lowest Sale"] = round(df[sales_column].min(), 2)

    elif dataset_type == "Employee Dataset":

        kpis["Total Employees"] = len(df)
        kpis["Total Columns"] = len(df.columns)

        department_keywords = [
            "department",
            "dept"
        ]

        for column in df.columns:

            normalized_column = (
                column.strip()
                .lower()
                .replace("_", " ")
            )

            if normalized_column in department_keywords:
                kpis["Departments"] = df[column].nunique()
                break

    elif dataset_type == "Logistics Dataset":

        kpis["Total Shipments"] = len(df)
        kpis["Total Columns"] = len(df.columns)

        status_keywords = [
            "status",
            "shipment status",
            "delivery status"
        ]

        for column in df.columns:

            normalized_column = (
                column.strip()
                .lower()
                .replace("_", " ")
            )

            if normalized_column in status_keywords:

                delivered = (
                    df[column]
                    .astype(str)
                    .str.lower()
                    .str.contains("delivered")
                    .sum()
                )

                delayed = (
                    df[column]
                    .astype(str)
                    .str.lower()
                    .str.contains("delayed")
                    .sum()
                )

                kpis["Delivered"] = int(delivered)
                kpis["Delayed"] = int(delayed)

                break

    elif dataset_type == "Generic Dataset":

        kpis["Rows"] = len(df)
        kpis["Columns"] = len(df.columns)
        kpis["Missing Values"] = int(df.isna().sum().sum())
        kpis["Duplicate Rows"] = int(df.duplicated().sum())

    return kpis