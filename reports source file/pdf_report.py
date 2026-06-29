from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(file_path, dataset_type, kpis):

    doc = SimpleDocTemplate(file_path)

    styles = getSampleStyleSheet()

    content = []

    # Title
    title = Paragraph("Smart Data Analytics Report", styles["Title"])
    content.append(title)
    content.append(Spacer(1, 12))

    # Dataset Type
    dataset_info = Paragraph(
        f"<b>Dataset Type:</b> {dataset_type}",
        styles["Normal"]
    )
    content.append(dataset_info)
    content.append(Spacer(1, 12))

    # KPIs Section
    kpi_title = Paragraph("Key Performance Indicators", styles["Heading2"])
    content.append(kpi_title)
    content.append(Spacer(1, 10))

    # Add KPIs
    for key, value in kpis.items():

        line = Paragraph(f"<b>{key}:</b> {value}", styles["Normal"])
        content.append(line)
        content.append(Spacer(1, 8))

    doc.build(content)