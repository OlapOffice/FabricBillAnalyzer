# Microsoft Fabric Bill Analyzer - Enhanced Version 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)

> **🆕 NEW FEATURE:** Combined Sorted Report with BillSort.csv export functionality

A comprehensive tool for analyzing Microsoft Fabric billing data with advanced sorting and reporting capabilities.

![Microsoft Fabric Bill Analyzer](https://img.shields.io/badge/Microsoft%20Fabric-Bill%20Analyzer-blue?style=for-the-badge&logo=microsoft)

## ✨ Features

### 🆕 **New: Combined Sorted Report**
- **Smart Sorting**: MeterCategory↑, ConsumedService↑, Cost↓
- **BillSort.csv Export**: Direct CSV export in sorted format
- **Excel Integration**: New "Combined_Sorted" sheet in Excel reports
- **Web Interface**: Enhanced UI with dedicated export buttons
- **API Access**: RESTful endpoint for programmatic access

### 📊 **Core Analytics**
- **Multi-dimensional Analysis**: Service, Category, Resource breakdowns
- **Interactive Web Interface**: User-friendly dashboard
- **Excel Reporting**: Comprehensive multi-sheet reports
- **Search & Filter**: Find specific resources and services
- **Cost Visualization**: Top costs and percentage breakdowns

### 💻 **Multiple Interfaces**
- **Web Application**: Flask-based dashboard
- **Command Line**: Enhanced CLI with Combined Sorted Report
- **Python API**: Programmatic access for automation
- **REST API**: JSON endpoints for integration

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

```bash
# Clone the repository
git clone https://github.com/OlapOffice/FabricBillAnalyzer.git
cd FabricBillAnalyzer

# Install dependencies
pip install -r requirements.txt

# Run the web application
python app.py
```

Open your browser to: **http://localhost:5000**

### Alternative: Use the Launcher
On Windows, simply double-click `run.bat`

## 📖 Usage

### Web Interface
1. Upload your CSV billing file
2. View comprehensive analysis results
3. **NEW**: Export Combined Sorted Report as BillSort.csv
4. Export full Excel report with multiple sheets

### Command Line
```bash
# Basic analysis with Combined Sorted Report
python cli.py

# Export all formats
python cli.py --excel --csv --combined

# Specific file analysis
python cli.py data/my_fabric_bill.csv --combined
```

### Python API
```python
from analyzer import FabricBillAnalyzer

analyzer = FabricBillAnalyzer()
analyzer.load_data('bills/sample_fabric_bill.csv')

# NEW: Generate Combined Sorted Report
combined_report = analyzer.generate_combined_sorted_report()
csv_file = analyzer.export_combined_sorted_csv()
excel_file = analyzer.export_to_excel()
```

## 📋 Required CSV Format

Your input CSV must contain these columns:

| Column | Description | Example |
|--------|-------------|---------|
| `MeterCategory` | Azure service category | Azure App Service |
| `ConsumedService` | Specific Azure service | microsoft.web |
| `ResourceName` | Resource identifier | webapp-prod |
| `Cost` | Numeric cost value | 89.75 |

### Sample Data
```csv
MeterCategory,ConsumedService,ResourceName,Cost
Azure App Service,microsoft.web,webapp-prod,89.75
Azure Storage,Microsoft.Storage,stg001,125.50
Compute,Microsoft.Compute,vm-production,445.67
```

## 🆕 Combined Sorted Report

The new **Combined Sorted Report** feature provides intelligent data organization:

### Sorting Algorithm
1. **MeterCategory** (Ascending) - Groups similar services
2. **ConsumedService** (Ascending) - Sub-groups within categories  
3. **Cost** (Descending) - Highest costs first within each group

### Output Example
```csv
MeterCategory,ConsumedService,ResourceName,Cost
Azure App Service,microsoft.web,webapp-prod,89.75
Azure App Service,microsoft.web,oo100-asp,53.25
Azure Cognitive Search,Microsoft.Search,gptkb-search,238.22
Azure Storage,Microsoft.Storage,stg001,125.50
```

### Export Options
- **BillSort.csv**: Direct CSV export
- **Excel Sheet**: "Combined_Sorted" tab in Excel reports
- **Web Display**: Formatted table with sort indicators
- **JSON API**: `/api/combined_report/<filename>`

## 📁 Project Structure

```
FabricBillAnalyzer/
├── 📄 analyzer.py              # Core analysis engine with Combined Sorted Report
├── 🌐 app.py                  # Flask web application
├── 💻 cli.py                  # Command-line interface
├── 🧪 test_combined_report.py # Test scripts
├── 📋 requirements.txt        # Dependencies
├── 🚀 run.bat                # Windows launcher
├── 📁 templates/              # Web interface templates
├── 📁 bills/                 # Sample data
└── 📁 reports/              # Export folder
```

## 🔌 API Endpoints

### REST API
- `GET /` - Main dashboard
- `POST /upload` - File upload
- `GET /analyze/<filename>` - Analysis results
- `GET /export_excel/<filename>` - Excel export
- `GET /export_combined_csv/<filename>` - 🆕 BillSort CSV export
- `GET /api/stats/<filename>` - Basic statistics (JSON)
- `GET /api/combined_report/<filename>` - 🆕 Combined Sorted Report (JSON)

## 🧪 Testing

### Run Tests
```bash
# Test the new Combined Sorted Report feature
python test_combined_report.py

# Expected output:
# ✅ Data loaded successfully
# ✅ Combined Sorted Report generated successfully  
# ✅ CSV exported successfully
# ✅ Excel exported successfully
```

### Sample Data
The repository includes sample data (`bills/sample_fabric_bill.csv`) with 10 records totaling $2,180.37 for testing.

## 📊 Excel Report Sheets

| Sheet Name | Description |
|------------|-------------|
| Summary | Key metrics and totals |
| By_Service | Analysis grouped by service |
| By_Category | Analysis grouped by category |
| By_Resource | Analysis grouped by resource |
| **Combined_Sorted** | 🆕 **NEW**: Intelligently sorted data |
| Top_Costs | Highest cost items |
| Raw_Data | Original uploaded data |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆕 What's New in This Version

### Enhanced Features
- ✅ **Combined Sorted Report** - Intelligent data sorting and organization
- ✅ **BillSort.csv Export** - Direct CSV export in sorted format
- ✅ **Enhanced Excel Reports** - New "Combined_Sorted" sheet
- ✅ **Improved Web Interface** - New export buttons and displays
- ✅ **Extended CLI** - Command-line access to new features
- ✅ **Comprehensive Testing** - Test scripts and validation

### Backward Compatibility
- ✅ All existing functionality preserved
- ✅ Same CSV input requirements
- ✅ Same API endpoints (with additions)
- ✅ No breaking changes

## 🚀 Getting Started with Your Data

1. **Prepare your CSV** with the required columns
2. **Upload via web interface** or use CLI
3. **Analyze your costs** across services and categories
4. **Export Combined Sorted Report** for organized cost analysis
5. **Generate comprehensive Excel reports** for detailed insights

## 🎯 Use Cases

- **Cost Optimization**: Identify highest cost resources and services
- **Budget Planning**: Understand spending patterns across categories
- **Resource Management**: Track resource utilization and costs
- **Financial Reporting**: Generate formatted reports for stakeholders
- **Data Analysis**: Export structured data for further analysis

## 📞 Support

- 📧 **Issues**: Use GitHub Issues for bug reports and feature requests
- 📖 **Documentation**: Check the `USAGE_GUIDE.md` for detailed instructions
- 💡 **Examples**: See sample data and test scripts in the repository

---

**🎊 Ready to analyze your Microsoft Fabric billing data with intelligent sorting!**

[![Made with ❤️ by OLAP Office](https://img.shields.io/badge/Made%20with%20❤️%20by-OLAP%20Office-red)](https://github.com/OlapOffice)