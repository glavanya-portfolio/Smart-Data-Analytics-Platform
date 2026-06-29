import streamlit as st
import plotly.express as px


def display_charts(df, dataset_type):

    st.subheader("📈 Interactive Dashboard")

    if dataset_type == "Sales Dataset":
        display_sales_charts(df)

    elif dataset_type == "Employee Dataset":
        display_employee_charts(df)

    elif dataset_type == "Logistics Dataset":
        display_logistics_charts(df)

    else:
        display_generic_charts(df)


# ================= SALES =================

def display_sales_charts(df):

    sales_columns = [
        "sales",
        "sales amount",
        "revenue",
        "amount",
        "total sales"
    ]

    category_columns = [
        "category",
        "product category"
    ]

    sales_col = None
    category_col = None

    for col in df.columns:

        name = col.strip().lower().replace("_", " ")

        if name in sales_columns:
            sales_col = col

        if name in category_columns:
            category_col = col

    if sales_col and category_col:

        chart_data = (
            df.groupby(category_col)[sales_col]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            chart_data,
            x=category_col,
            y=sales_col,
            title="Sales by Category"
        )

        st.plotly_chart(fig, use_container_width=True)

        return

    st.info("No suitable columns found for Sales chart.")


# ================= EMPLOYEE =================

def display_employee_charts(df):

    department_columns = [
        "department",
        "dept"
    ]

    department_col = None

    for col in df.columns:

        name = col.strip().lower().replace("_", " ")

        if name in department_columns:
            department_col = col

    if department_col:

        chart_data = (
            df[department_col]
            .value_counts()
            .reset_index()
        )

        chart_data.columns = [
            department_col,
            "Employees"
        ]

        fig = px.pie(
            chart_data,
            names=department_col,
            values="Employees",
            title="Employees by Department"
        )

        st.plotly_chart(fig, use_container_width=True)

        return

    st.info("No suitable columns found for Employee chart.")


# ================= LOGISTICS =================

def display_logistics_charts(df):

    status_columns = [
        "status",
        "shipment status",
        "delivery status"
    ]

    status_col = None

    for col in df.columns:

        name = col.strip().lower().replace("_", " ")

        if name in status_columns:
            status_col = col

    if status_col:

        chart_data = (
            df[status_col]
            .value_counts()
            .reset_index()
        )

        chart_data.columns = [
            status_col,
            "Count"
        ]

        fig = px.pie(
            chart_data,
            names=status_col,
            values="Count",
            title="Shipment Status"
        )

        st.plotly_chart(fig, use_container_width=True)

        return

    st.info("No suitable columns found for Logistics chart.")


# ================= GENERIC =================

def display_generic_charts(df):

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        st.info("No numeric columns available for visualization.")
        return

    fig = px.histogram(
        numeric_df,
        title="Numeric Data Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)