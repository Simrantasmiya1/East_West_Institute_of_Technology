from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import PageBreak
from reportlab.platypus import Image
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.platypus import HRFlowable
from reportlab.platypus import KeepTogether
from reportlab.platypus import FrameBreak
from reportlab.platypus import Indenter
from reportlab.platypus import XPreformatted
from reportlab.platypus import Flowable
from reportlab.platypus import PageTemplate
from reportlab.platypus import BaseDocTemplate
from reportlab.platypus import Frame
from reportlab.platypus import NextPageTemplate
from reportlab.platypus import FrameBreak
from reportlab.platypus import Spacer
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate

def generate_career_report(data, filename="AI_Career_Report.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    elements = []

    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    normal_style = styles["Normal"]

    elements.append(Paragraph("AI Career Analysis Report", title_style))
    elements.append(Spacer(1, 0.5 * inch))

    elements.append(Paragraph(f"Best Fit Branch: {data['best_branch']}", normal_style))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph("Suitability Ranking:", styles["Heading2"]))
    for branch, score in data["ranking"].items():
        elements.append(Paragraph(f"{branch} → {score}%", normal_style))

    elements.append(Spacer(1, 0.3 * inch))
    elements.append(Paragraph("Future Career Roles:", styles["Heading2"]))
    for role in data["careers"]:
        elements.append(Paragraph(f"• {role}", normal_style))

    elements.append(Spacer(1, 0.3 * inch))
    elements.append(Paragraph("4-Year Success Roadmap:", styles["Heading2"]))
    for year, content in data["roadmap"].items():
        elements.append(Paragraph(f"{year}: {content}", normal_style))

    elements.append(Spacer(1, 0.3 * inch))
    elements.append(Paragraph(f"Confidence Score: {data['confidence']}%", styles["Heading2"]))

    doc.build(elements)

    return filename
