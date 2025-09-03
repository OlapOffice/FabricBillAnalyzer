# 🚀 Microsoft Fabric Bill Analyzer - Enhanced Edition

**Powered by [Semanticise Inc.](https://semanticise.com/)**

A comprehensive Flask web application for analyzing Microsoft Fabric billing data with interactive charts, advanced filtering, and intelligent reporting features.

![Version](https://img.shields.io/badge/version-2.0-green)
![Python](https://img.shields.io/badge/python-3.7+-blue)
![License](https://img.shields.io/badge/license-MIT-blue)

## ✨ Key Features

### 🆕 **NEW: Enhanced Features**
- **📊 Interactive Charts** - Plotly-powered visualizations with hover details
- **🔍 Advanced Filtering System** - Multi-dimensional filtering with real-time results
- **📑 Combined Sorted Report** - Intelligent data sorting (MeterCategory↑, ConsumedService↑, Cost↓)
- **💾 BillSort.csv Export** - Standardized CSV export format

### 🔧 **Core Analytics**
- **📈 Multi-dimensional Analysis** - By service, category, and resource
- **🔎 Smart Search** - Find resources, services, or categories instantly
- **📋 Excel Export** - Comprehensive reports with multiple worksheets
- **📱 Responsive Design** - Modern Bootstrap UI that works on all devices

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)
```bash
python run_app.py
```
This script will:
- Check Python version compatibility
- Install missing dependencies
- Verify project structure
- Create sample data
- Launch the web application

### Option 2: Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### Option 3: Test Suite
```bash
# Run comprehensive feature tests
python test_app.py
```

## 📁 Project Structure

```
fabric-bill-analyzer-enhanced/
├── 📄 app.py                 # Flask web application
├── 📄 analyzer.py            # Core analysis engine
├── 📄 charts.py              # Interactive chart generation
├── 📄 run_app.py             # Automated setup & launcher
├── 📄 test_app.py            # Feature test suite
├── 📄 requirements.txt       # Python dependencies
├── 📁 templates/             # HTML templates
│   ├── index.html            # Main dashboard
│   ├── analysis.html         # Analysis results
│   ├── filter.html           # Advanced filtering
│   └── search_results.html   # Search interface
├── 📁 bills/                 # Upload directory
├── 📁 reports/               # Export directory
└── 📄 README.md              # This file
```

## 📊 Data Requirements

Your CSV/Excel file must contain these columns:
- **MeterCategory** - Service category (e.g., "Storage", "Azure App Service")
- **ConsumedService** - Service name (e.g., "Microsoft.Storage")
- **ResourceName** - Resource identifier
- **Cost** - Billing cost (numeric)

### Optional Columns (Enhanced Features):
- ResourceGroup, ResourceLocation, ResourceType, MeterName

## 📥 How to Get Your Azure Billing Data

### ✅ **Azure Invoice Download Checklist**

Follow these steps to download your Azure invoice and usage data:

1. **Go to Subscription**
   - Navigate to the [Azure portal](https://portal.azure.com) and select the relevant subscription

2. **Access Billing**
   - In the subscription menu, click on **Billing** to view billing-related options

3. **Open Invoices**
   - Select **Invoices** to see a list of available billing documents

4. **Select Invoice**
   - Choose the specific invoice you want to download from the list

5. **Prepare Azure Usage File**
   - If needed, generate the detailed usage file associated with the invoice

6. **Download**
   - Click **Download** to save the invoice and usage file to your device

💡 **Pro Tip**: The detailed usage CSV file contains all the columns needed for this analyzer!

## 🔍 Microsoft Fabric Capacity Metrics

### **Enhanced Monitoring for Fabric Admins**

For **Microsoft Fabric capacity admins** looking to gain deeper visibility into their resources, Microsoft provides a comprehensive monitoring solution:

**📊 Fabric Capacity Metrics App**
- Monitor usage of compute and storage on your capacities
- Analyze utilization, processing time, and user details
- Identify overload causes and peak demand times
- Track resource consumption patterns
- Easily identify the most demanding or most popular items

**🔗 Resources:**
- **Download from AppSource**: [Microsoft Fabric Capacity Metrics](https://appsource.microsoft.com/en-us/product/power-bi/pbi_pcmm.microsoftpremiumfabricpreviewreport)
- **Installation Guide**: [Microsoft Learn - Fabric Metrics App](https://learn.microsoft.com/en-us/fabric/enterprise/metrics-app-install?tabs=1st)

**💼 Why Use Both Tools?**
- **Fabric Capacity Metrics App**: Real-time capacity monitoring and performance insights
- **This Bill Analyzer**: Historical cost analysis, billing optimization, and detailed financial reporting

Together, these tools provide complete visibility into both performance and cost aspects of your Microsoft Fabric deployment!

## 🎯 Feature Guide

### 📊 Interactive Charts
- **Service Pie Chart** - Cost distribution by service
- **Category Bar Chart** - Spending by category
- **Top Resources** - Highest cost resources
- **Cost Histogram** - Distribution analysis
- **Sunburst Chart** - Hierarchical service view

### 🔍 Advanced Filtering
- **Category & Service Filters** - Dropdown selection
- **Cost Range Sliders** - Min/Max cost filtering
- **Text Search** - Resource name matching
- **Multi-Filter Combinations** - Apply multiple filters simultaneously

### 📑 Combined Sorted Report (NEW)
Intelligent sorting algorithm:
1. **MeterCategory** (Ascending) - Groups similar services
2. **ConsumedService** (Ascending) - Sub-sorts within categories  
3. **Cost** (Descending) - Shows highest costs first

Export formats:
- **BillSort.csv** - Standardized CSV format
- **Excel Sheet** - Included in comprehensive Excel export

### 🔎 Search & Export
- **Global Search** - Find resources across all fields
- **Excel Export** - Multi-sheet workbook with all analyses
- **CSV Export** - Individual analysis downloads
- **Print Support** - Printer-friendly layouts

## 🌐 Web Interface

### Main Dashboard (`/`)
- File upload interface
- Available files management
- Feature overview

### Analysis Page (`/analyze/<filename>`)
- Interactive charts section
- Key metrics dashboard
- Multiple analysis views
- Export options

### Advanced Filtering (`/filter/<filename>`)
- Dynamic filter controls
- Real-time result updates
- Export filtered data

### Search Interface (`/search/<filename>?q=term`)
- Global search functionality
- Highlighted results
- Export search results

## 📡 API Endpoints

- **GET** `/api/stats/<filename>` - Basic statistics JSON
- **GET** `/api/combined_report/<filename>` - Combined sorted report JSON
- **GET** `/export_excel/<filename>` - Download Excel report
- **GET** `/export_combined_csv/<filename>` - Download BillSort.csv

## 🛠️ Requirements

### Python Dependencies
```
Flask==2.3.3
pandas>=1.5.0
plotly==5.17.0
openpyxl>=3.0.0
numpy>=1.21.0
werkzeug>=2.0.0
```

### System Requirements
- **Python**: 3.7 or higher
- **Memory**: 2GB RAM (for large datasets)
- **Storage**: 100MB free space
- **Browser**: Chrome, Firefox, Safari, Edge

## 🚀 Usage Examples

### Getting Started with Azure Data
1. **Download your Azure billing data** (see checklist above)
2. **Upload the CSV/Excel file** to the analyzer
3. **Click "Analyze"** to view comprehensive analysis
4. **Explore interactive charts** and metrics
5. **Export results** in Excel or CSV format

### Basic Analysis Workflow
1. Upload your Fabric billing CSV/Excel file
2. Click "Analyze" to view comprehensive analysis
3. Explore interactive charts and metrics
4. Export results in Excel or CSV format

### Advanced Filtering
1. From analysis page, click "Advanced Filters"
2. Set category, service, cost range, or text filters
3. View real-time filtered results
4. Export filtered data

### Combined Sorted Report
1. View the "Combined Sorted Report" section in analysis
2. Data is automatically sorted by: Category↑, Service↑, Cost↓
3. Click "Download BillSort.csv" for standardized export

### Integration with Fabric Capacity Metrics
1. **Use Fabric Capacity Metrics App** for real-time performance monitoring
2. **Use this Bill Analyzer** for historical cost analysis and optimization
3. **Combine insights** from both tools for complete Fabric governance

## 🔧 Configuration

### Port Configuration
Default: `http://localhost:5000`

To change port, edit `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=8080)
```

### File Size Limits
Default: 16MB

To change, edit `app.py`:
```python
MAX_CONTENT_LENGTH = 32 * 1024 * 1024  # 32MB
```

## 🆘 Troubleshooting

### Common Issues

**"Module not found" errors**
```bash
pip install -r requirements.txt
```

**"File not found" errors**
- Ensure CSV has required columns
- Check file permissions
- Verify upload directory exists

**Charts not displaying**
- Clear browser cache
- Check internet connection (for CDN resources)
- Verify Plotly.js is loading

**Performance issues with large files**
- Use filtering to reduce dataset size
- Consider processing files in chunks
- Increase system memory allocation

### Debug Mode
Run with enhanced logging:
```bash
export FLASK_DEBUG=1
python app.py
```

## 🤝 Support

For support, feature requests, or bug reports:
- 🌐 Visit: [https://semanticise.com/](https://semanticise.com/)
- 📧 Contact: Semanticise Inc. support team

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏢 About Semanticise Inc.

**Semanticise Inc.** is a leading provider of AI-powered analytics and business intelligence solutions. We specialize in transforming complex data into actionable insights.

🔗 **Learn more**: [https://semanticise.com/](https://semanticise.com/)

---

## 🎉 Version History

### v2.0 - Enhanced Edition
- ✅ Interactive Plotly charts
- ✅ Advanced filtering system  
- ✅ Combined sorted report feature
- ✅ Improved UI/UX design
- ✅ Real-time data processing
- ✅ Enhanced search functionality

### v1.0 - Initial Release
- ✅ Basic analysis features
- ✅ Excel export functionality
- ✅ Web interface
- ✅ Multi-dimensional reporting

---

**Made with ❤️ by [Semanticise Inc.](https://semanticise.com/)**