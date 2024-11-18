from django.shortcuts import render, redirect, get_object_or_404
from .models import Report
from .forms import ReportGenerationForm
from django.http import HttpResponse
from django_q.tasks import async_task
import csv

# View list of reports
def report_list(request):
    reports = Report.objects.all()
    return render(request, 'reports/report_list.html', {'reports': reports})

# Generate a new report asynchronously
def generate_report(request):
    if request.method == 'POST':
        form = ReportGenerationForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.is_generated = False  # Mark as not generated
            report.save()
            # Trigger report generation in the background
            async_task('reports.tasks.generate_report_task', report.id)
            return redirect('report_list')
    else:
        form = ReportGenerationForm()
    return render(request, 'reports/generate_report.html', {'form': form})

# Download a specific report
def download_report(request, report_id):
    report = get_object_or_404(Report, id=report_id, is_generated=True)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{report.name}.csv"'

    writer = csv.writer(response)
    # Example data - Replace with your actual report generation logic
    writer.writerow(['Field1', 'Field2', 'Field3'])
    writer.writerow(['Data1', 'Data2', 'Data3'])

    return response
