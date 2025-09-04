"""
Semanticise Inc. Microsoft Azure & Fabric Bill Analyzer - Enhanced Flask Web Application
Web interface with Combined Sorted Report feature
"""

from flask import Flask, render_template, request, redirect, url_for, flash, send_file, jsonify
import os
import pandas as pd
from werkzeug.utils import secure_filename
from analyzer import FabricBillAnalyzer
from charts import create_charts
import tempfile
import json
import logging

app = Flask(__name__)
app.secret_key = 'fabric_bill_analyzer_secret_key_2024'

# Configuration
UPLOAD_FOLDER = 'bills'
ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'xls'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('reports', exist_ok=True)

def allowed_file(filename):
    """Check if file has allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Main dashboard page."""
    # List available files
    files = []
    if os.path.exists(UPLOAD_FOLDER):
        for f in os.listdir(UPLOAD_FOLDER):
            if allowed_file(f):
                file_path = os.path.join(UPLOAD_FOLDER, f)
                file_size = os.path.getsize(file_path)
                files.append({
                    'name': f,
                    'size': f"{file_size / 1024:.1f} KB",
                    'path': file_path
                })
    
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload."""
    if 'file' not in request.files:
        flash('No file selected', 'error')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No file selected', 'error')
        return redirect(url_for('index'))
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        flash(f'File {filename} uploaded successfully!', 'success')
        return redirect(url_for('analyze_file', filename=filename))
    else:
        flash('Invalid file type. Please upload CSV or Excel files only.', 'error')
        return redirect(url_for('index'))

@app.route('/analyze/<filename>')
def analyze_file(filename):
    """Analyze uploaded file and display results."""
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    if not os.path.exists(file_path):
        flash('File not found', 'error')
        return redirect(url_for('index'))
    
    # Initialize analyzer and load data
    analyzer = FabricBillAnalyzer()
    
    if not analyzer.load_data(file_path):
        flash('Error loading file. Please check the file format.', 'error')
        return redirect(url_for('index'))
    
    # Generate all analyses
    try:
        basic_stats = analyzer.get_basic_stats()
        service_analysis = analyzer.analyze_by_service()
        category_analysis = analyzer.analyze_by_category()
        resource_analysis = analyzer.analyze_by_resource()
        combined_report = analyzer.generate_combined_sorted_report()  # NEW FEATURE
        top_costs = analyzer.get_top_costs(10)
        
        # NEW: Generate interactive charts
        charts = create_charts(analyzer)
        
        # Convert DataFrames to dictionaries for template rendering
        analyses = {
            'basic_stats': basic_stats,
            'services': service_analysis.to_dict('records') if not service_analysis.empty else [],
            'categories': category_analysis.to_dict('records') if not category_analysis.empty else [],
            'resources': resource_analysis.to_dict('records') if not resource_analysis.empty else [],
            'combined_report': combined_report.to_dict('records') if not combined_report.empty else [],  # NEW
            'top_costs': top_costs.to_dict('records') if not top_costs.empty else [],
            'charts': charts  # NEW: Interactive charts
        }
        
        # Generate summary report
        summary = analyzer.generate_report_summary()
        
        return render_template('analysis.html', 
                               filename=filename, 
                               analyses=analyses, 
                               summary=summary)
        
    except Exception as e:
        flash(f'Error during analysis: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/export_excel/<filename>')
def export_excel(filename):
    """Export analysis to Excel file."""
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    if not os.path.exists(file_path):
        flash('File not found', 'error')
        return redirect(url_for('index'))
    
    analyzer = FabricBillAnalyzer()
    if not analyzer.load_data(file_path):
        flash('Error loading file for export', 'error')
        return redirect(url_for('index'))
    
    try:
        excel_path = analyzer.export_to_excel()
        if excel_path and os.path.exists(excel_path):
            return send_file(excel_path, as_attachment=True, download_name=f"fabric_analysis_{filename}.xlsx")
        else:
            flash('Error generating Excel export', 'error')
            return redirect(url_for('analyze_file', filename=filename))
            
    except Exception as e:
        flash(f'Export error: {str(e)}', 'error')
        return redirect(url_for('analyze_file', filename=filename))

@app.route('/export_combined_csv/<filename>')
def export_combined_csv(filename):
    """Export Combined Sorted Report to CSV file - NEW FEATURE."""
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    if not os.path.exists(file_path):
        flash('File not found', 'error')
        return redirect(url_for('index'))
    
    analyzer = FabricBillAnalyzer()
    if not analyzer.load_data(file_path):
        flash('Error loading file for export', 'error')
        return redirect(url_for('index'))
    
    try:
        csv_path = analyzer.export_combined_sorted_csv()
        if csv_path and os.path.exists(csv_path):
            return send_file(csv_path, as_attachment=True, download_name=f"BillSort_{filename}")
        else:
            flash('Error generating CSV export', 'error')
            return redirect(url_for('analyze_file', filename=filename))
            
    except Exception as e:
        flash(f'CSV Export error: {str(e)}', 'error')
        return redirect(url_for('analyze_file', filename=filename))

@app.route('/api/stats/<filename>')
def api_stats(filename):
    """API endpoint for basic statistics."""
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404
    
    analyzer = FabricBillAnalyzer()
    if not analyzer.load_data(file_path):
        return jsonify({'error': 'Error loading file'}), 500
    
    return jsonify(analyzer.get_basic_stats())

@app.route('/api/combined_report/<filename>')
def api_combined_report(filename):
    """API endpoint for Combined Sorted Report - NEW FEATURE."""
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404
    
    analyzer = FabricBillAnalyzer()
    if not analyzer.load_data(file_path):
        return jsonify({'error': 'Error loading file'}), 500
    
    combined_report = analyzer.generate_combined_sorted_report()
    return jsonify({
        'data': combined_report.to_dict('records'),
        'total_records': len(combined_report),
        'total_cost': float(combined_report['Cost'].sum()) if not combined_report.empty else 0
    })

@app.route('/filter/<filename>')
def filter_data(filename):
    """Advanced filtering interface - NEW FEATURE."""
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    if not os.path.exists(file_path):
        flash('File not found', 'error')
        return redirect(url_for('index'))
    
    analyzer = FabricBillAnalyzer()
    if not analyzer.load_data(file_path):
        flash('Error loading file', 'error')
        return redirect(url_for('index'))
    
    # Get filter parameters from request
    category_filter = request.args.get('category', '')
    service_filter = request.args.get('service', '')
    min_cost = request.args.get('min_cost', '')
    max_cost = request.args.get('max_cost', '')
    resource_filter = request.args.get('resource', '')
    
    # Convert cost filters to float if provided
    min_cost_value = None
    max_cost_value = None
    
    if min_cost and min_cost.strip():
        try:
            min_cost_value = float(min_cost)
        except ValueError:
            min_cost_value = None
    
    if max_cost and max_cost.strip():
        try:
            max_cost_value = float(max_cost)
        except ValueError:
            max_cost_value = None
    
    # Apply filters
    filtered_df = analyzer.df.copy()
    
    if category_filter:
        filtered_df = filtered_df[filtered_df['MeterCategory'].str.contains(category_filter, case=False, na=False)]
    
    if service_filter:
        filtered_df = filtered_df[filtered_df['ConsumedService'].str.contains(service_filter, case=False, na=False)]
    
    if resource_filter:
        filtered_df = filtered_df[filtered_df['ResourceName'].str.contains(resource_filter, case=False, na=False)]
    
    if min_cost_value is not None:
        # Ensure Cost column is numeric
        filtered_df = filtered_df[pd.to_numeric(filtered_df['Cost'], errors='coerce') >= min_cost_value]
    
    if max_cost_value is not None:
        # Ensure Cost column is numeric
        filtered_df = filtered_df[pd.to_numeric(filtered_df['Cost'], errors='coerce') <= max_cost_value]
    
    # Get unique values for filter dropdowns (from original data)
    filter_options = {
        'categories': sorted([cat for cat in analyzer.df['MeterCategory'].unique() if pd.notna(cat)]),
        'services': sorted([svc for svc in analyzer.df['ConsumedService'].unique() if pd.notna(svc)]),
        'cost_range': {
            'min': float(analyzer.df['Cost'].min()),
            'max': float(analyzer.df['Cost'].max())
        }
    }
    
    # Calculate filtered statistics
    filtered_stats = {
        'total_records': len(filtered_df),
        'total_cost': float(filtered_df['Cost'].sum()) if not filtered_df.empty else 0.0,
        'avg_cost': float(filtered_df['Cost'].mean()) if not filtered_df.empty else 0.0,
        'unique_services': filtered_df['ConsumedService'].nunique() if not filtered_df.empty else 0,
        'unique_categories': filtered_df['MeterCategory'].nunique() if not filtered_df.empty else 0
    }
    
    # Convert to records for template
    filtered_records = filtered_df.to_dict('records') if not filtered_df.empty else []
    
    return render_template('filter.html', 
                          filename=filename,
                          filtered_data=filtered_records,
                          filtered_stats=filtered_stats,
                          filter_options=filter_options,
                          applied_filters={
                              'category': category_filter,
                              'service': service_filter,
                              'min_cost': min_cost_value,
                              'max_cost': max_cost_value,
                              'resource': resource_filter
                          })

@app.route('/search/<filename>')
def search_resources(filename):
    """Search for resources."""
    search_term = request.args.get('q', '')
    
    if not search_term:
        flash('Please provide a search term', 'error')
        return redirect(url_for('analyze_file', filename=filename))
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    if not os.path.exists(file_path):
        flash('File not found', 'error')
        return redirect(url_for('index'))
    
    analyzer = FabricBillAnalyzer()
    if not analyzer.load_data(file_path):
        flash('Error loading file', 'error')
        return redirect(url_for('index'))
    
    try:
        search_results = analyzer.search_resources(search_term)
        results = search_results.to_dict('records') if not search_results.empty else []
        
        return render_template('search_results.html', 
                               filename=filename, 
                               search_term=search_term, 
                               results=results)
        
    except Exception as e:
        flash(f'Search error: {str(e)}', 'error')
        return redirect(url_for('analyze_file', filename=filename))

@app.route('/delete/<filename>')
def delete_file(filename):
    """Delete uploaded file."""
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            flash(f'File {filename} deleted successfully', 'success')
        else:
            flash('File not found', 'error')
    except Exception as e:
        flash(f'Error deleting file: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.errorhandler(413)
def too_large(e):
    """Handle file too large error."""
    flash("File is too large. Maximum size is 16MB.", 'error')
    return redirect(url_for('index')), 413

@app.errorhandler(404)
def not_found(e):
    """Handle page not found."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    """Handle internal server error."""
    return render_template('500.html'), 500

if __name__ == '__main__':
    print("Starting Semanticise Inc. Microsoft Azure & Fabric Bill Analyzer - Enhanced Version")
    print("=" * 70)
    print("🚀 NEW FEATURE: Combined Sorted Report")
    print("   - Sort by: MeterCategory↑, ConsumedService↑, Cost↓")
    print("   - Export to BillSort.csv format")
    print("   - Available in both web interface and Excel export")
    print("=" * 70)
    print("🌐 Powered by Semanticise Inc. - https://semanticise.com/")
    print("🌍 Open your browser and go to: http://localhost:5000")
    print("⏹️  To stop the server, press Ctrl+C")
    print("=" * 70)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
