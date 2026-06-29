import pandas as pd
import os
import streamlit as st

# ---------------- SESSION STATE INIT ----------------
if "pdf_generated" not in st.session_state:
    st.session_state.pdf_generated = False

if "excel_generated" not in st.session_state:
    st.session_state.excel_generated = False
if "cleaned_df" not in st.session_state:
    st.session_state.cleaned_df = None


from utils.file_handler import load_data
from etl.data_quality import get_data_quality
from etl.data_cleaning import clean_data
from utils.dataset_detector import detect_dataset_type
from analytics.kpi_generator import generate_kpis
from dashboard.charts import display_charts
from database.db_operations import save_to_mysql
from reports.pdf_report import generate_pdf_report
from reports.excel_report import export_to_excel
from data.business_questions import answer_question



st.set_page_config(
    page_title="Smart Data Analytics Platform",
    page_icon="📊",
    layout="wide"
)


# ================= SIDEBAR =================
with st.sidebar:

    st.image("https://img.icons8.com/color/96/combo-chart.png", width=80)

    st.title("Smart Analytics")

    st.markdown("---")

    st.success("✅ Upload Dataset")

    st.info("""
Supported Files

• Excel (.xlsx)
""")

    st.markdown("---")

    st.subheader("Modules")
    st.write("Dataset Preview")
    st.write("Data Quality Report")
    st.write("🧹 ETL Cleaning")
    st.write("Dataset Detection")
    st.write("📈 Dashboard")
    st.write("📊 KPI Generator")
    st.write("💾 MySQL Storage")
    st.write("📄 PDF Report")
    st.write("📗 Excel Export")
    st.write("🤖 Business Questions")

st.title("📊 Smart Data Analytics Platform")

st.caption("AI Powered ETL • KPI • Dashboard • Reporting")

with st.container():
    st.divider()
    st.subheader("📁 Upload Dataset")

    uploaded_file = st.file_uploader(
        "Choose CSV or Excel File",
        type=["csv", "xlsx"]
    )

if uploaded_file is not None:

  df = load_data(uploaded_file)
    
  st.success("✅ File uploaded successfully!")

  with st.expander("📄 Dataset Preview", expanded=True):
    st.dataframe(df, use_container_width=True)

  report = get_data_quality(df)

  with st.expander("📋 Data Quality Report"):
    st.write(report)

  cleaned_df, cleaning_summary = clean_data(df)

  st.session_state.cleaned_df = cleaned_df

  with st.expander("🧹 Cleaning Summary"):
    st.write(cleaning_summary)

  with st.expander("✅ Cleaned Dataset"):
    st.dataframe(cleaned_df, use_container_width=True)

  dataset_type = detect_dataset_type(cleaned_df)

  with st.expander("📂 Dataset Detection", expanded=True):
    st.info(f"📂 Dataset Type: {dataset_type}")

  kpis = generate_kpis(cleaned_df, dataset_type)

  display_charts(cleaned_df, dataset_type)

  tab1, tab2, tab3 = st.tabs([
    "📊 KPIs",
    "📈 Dashboard",
    "📄 Reports"
])

# ---------------- TAB 1 ----------------
  with tab1:

    st.subheader("📊 Smart KPI Generator")

    if kpis:

        columns = st.columns(len(kpis))

        for column, (kpi_name, kpi_value) in zip(columns, kpis.items()):
            column.metric(kpi_name, kpi_value)

    else:
        st.warning("No KPIs could be generated.")


# ---------------- TAB 2 ----------------

  with tab2:

    st.divider()

    st.subheader("💬 Ask a Business Question")

    user_question = st.text_input(
        "Type your question...",
        key="question_box"
    )

    if user_question:
        answer = answer_question(cleaned_df, user_question)
        st.success(answer)


# ---------------- TAB 3 ----------------

  with tab3:

    st.subheader("📄 Reports")

    if st.button("💾 Save Clean Data to MySQL"):

        table_name = dataset_type.lower().replace(" ", "_")

        save_to_mysql(cleaned_df, table_name)

        st.success("Dataset saved successfully to MySQL.")

    col1, col2 = st.columns(2)

    # ================= PDF =================
    with col1:

        if st.button("Generate PDF Report"):

            os.makedirs("reports", exist_ok=True)

            file_path = os.path.join("reports", "analysis_report.pdf")

            generate_pdf_report(file_path, dataset_type, kpis)

            st.session_state.pdf_generated = True

            st.success("PDF Generated Successfully!")

        if st.session_state.pdf_generated:

            file_path = os.path.join("reports", "analysis_report.pdf")

            with open(file_path, "rb") as f:

                st.download_button(
                    label="⬇️ Download PDF",
                    data=f,
                    file_name="analysis_report.pdf",
                    mime="application/pdf"
                )

    # ================= EXCEL =================
    with col2:

        if st.button("Export Clean Data (Excel)"):

            os.makedirs("exports", exist_ok=True)

            file_path = os.path.join("exports", "clean_data.xlsx")

            export_to_excel(cleaned_df, file_path)

            st.session_state.excel_generated = True

            st.success("Excel Generated Successfully!")

        if st.session_state.excel_generated:

            file_path = os.path.join("exports", "clean_data.xlsx")

            with open(file_path, "rb") as f:

                st.download_button(
                    label="⬇️ Download Excel",
                    data=f,
                    file_name="clean_data.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )