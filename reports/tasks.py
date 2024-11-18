from .models import Report

def generate_report_task(report_id):
    """Background task to generate a report."""
    report = Report.objects.get(id=report_id)

    # Simulate report generation logic
    # Example: Generate a CSV or PDF file (you can replace this with your logic)
    print(f"Generating report: {report.name}")

    # Mark as generated once complete
    report.is_generated = True
    report.save()
