# Microsoft Fabric Bill Analyzer - Enhanced Version
## Quick Start Guide

### 🆕 NEW FEATURE: Combined Sorted Report
This enhanced version includes the Combined Sorted Report feature that generates BillSort.csv with specific sorting: **MeterCategory↑, ConsumedService↑, Cost↓**

---

## Quick Start (3 Steps)

### 1. Install Dependencies
```bash
cd fabric-bill-analyzer-enhanced
pip install -r requirements.txt
```

### 2. Run Web Interface
```bash
python app.py
# OR
run.bat
```
Open: http://localhost:5000

### 3. Test with Sample Data
Upload `bills/sample_fabric_bill.csv` or use the CLI:
```bash
python cli.py --combined --csv --excel
```

---

## New Features Added

### ✅ Combined Sorted Report
- **Method**: `generate_combined_sorted_report()`
- **Sorting**: MeterCategory↑, ConsumedService↑, Cost↓
- **Output**: DataFrame with exact BillSort.csv format

### ✅ BillSort.csv Export
- **Method**: `export_combined_sorted_csv()`
- **Format**: MeterCategory,ConsumedService,ResourceName,Cost
- **Web Export**: New "Export BillSort CSV" button
- **CLI Export**: `python cli.py --csv`

### ✅ Enhanced Excel Export
- **New Sheet**: "Combined_Sorted" 
- **All Sheets**: Summary, By_Service, By_Category, By_Resource, **Combined_Sorted**, Top_Costs, Raw_Data

### ✅ Web UI Enhancements
- New feature highlights with "NEW" badges
- Combined Sorted Report display in analysis page
- Dedicated export buttons
- API endpoint: `/api/combined_report/<filename>`

---

## Usage Examples

### Command Line Interface
```bash
# Basic analysis with Combined Sorted Report
python cli.py

# With specific file
python cli.py data/my_fabric_bill.csv --combined

# Export all formats
python cli.py --excel --csv --combined

# Just show the Combined Sorted Report
python cli.py --combined
```

### Python API
```python
from analyzer import FabricBillAnalyzer

analyzer = FabricBillAnalyzer()
analyzer.load_data('bills/sample_fabric_bill.csv')

# NEW: Generate Combined Sorted Report
combined_report = analyzer.generate_combined_sorted_report()
print(f"Generated {len(combined_report)} sorted records")

# NEW: Export BillSort.csv
csv_file = analyzer.export_combined_sorted_csv()
print(f"BillSort.csv exported to: {csv_file}")

# Enhanced Excel export
excel_file = analyzer.export_to_excel()
print(f"Excel with Combined_Sorted sheet: {excel_file}")
```

### Web Interface
1. Go to http://localhost:5000
2. Upload your CSV file
3. Click "Analyze"
4. View the **Combined Sorted Report** section (NEW)
5. Export using "Export BillSort CSV" button (NEW)

---

## Sample Data Testing

The included sample data (`bills/sample_fabric_bill.csv`) demonstrates the sorting:

**Original Order:**
```
Azure App Service,microsoft.web,oo100-asp,53.25
Azure Cognitive Search,Microsoft.Search,gptkb-kjfebpvfuinfi,238.22
Azure Storage,Microsoft.Storage,stg001,125.50
...
```

**After Combined Sorted Report (MeterCategory↑, ConsumedService↑, Cost↓):**
```
Azure App Service,microsoft.web,webapp-prod,89.75
Azure App Service,microsoft.web,oo100-asp,53.25
Azure Cognitive Search,Microsoft.Search,gptkb-kjfebpvfuinfi,238.22
Azure Cognitive Search,Microsoft.Search,search-service-02,156.88
Azure Storage,Microsoft.Storage,stg001,125.50
Azure Storage,Microsoft.Storage,blobstorage,67.33
Bandwidth,Microsoft.Network,outbound-transfer,45.20
Bandwidth,Microsoft.Network,cdn-transfer,23.15
Compute,Microsoft.Compute,vm-production,445.67
Compute,Microsoft.Compute,vm-staging,178.32
```

**Total: $2,180.37 across 10 records**

---

## File Structure
```
fabric-bill-analyzer-enhanced/
├── 📄 analyzer.py              # Enhanced analyzer with Combined Sorted Report
├── 🌐 app.py                  # Flask web application
├── 💻 cli.py                  # Enhanced command-line interface
├── 🧪 test_combined_report.py # Test script
├── 📋 requirements.txt        # Dependencies
├── 🚀 run.bat                # Windows launcher
├── 📖 README.md              # Documentation
├── 📖 USAGE_GUIDE.md         # This guide
├── 📁 templates/
│   ├── index.html            # Main dashboard
│   └── analysis.html         # Results page with Combined Sorted Report
├── 📁 bills/                 # Upload folder
│   └── sample_fabric_bill.csv # Sample data
└── 📁 reports/              # Export folder (auto-created)
```

---

## API Endpoints

### New Endpoint
- `GET /api/combined_report/<filename>` - Returns Combined Sorted Report as JSON

### All Endpoints
- `GET /` - Main dashboard
- `POST /upload` - File upload
- `GET /analyze/<filename>` - Analysis results  
- `GET /export_excel/<filename>` - Excel export
- `GET /export_combined_csv/<filename>` - 🆕 BillSort CSV export
- `GET /api/stats/<filename>` - Basic statistics
- `GET /api/combined_report/<filename>` - 🆕 Combined Sorted Report JSON

---

## Testing the New Feature

### Quick Test
```bash
# Test with sample data
python test_combined_report.py

# Expected output:
# ✅ Data loaded successfully
# ✅ Combined Sorted Report generated successfully  
# ✅ CSV exported successfully
# ✅ Excel exported successfully
# ✅ ALL TESTS COMPLETED SUCCESSFULLY!
```

### Manual Verification
1. **Check Sorting**: Categories should be alphabetical, services within categories alphabetical, costs within services descending
2. **Check CSV Format**: Should match exactly: `MeterCategory,ConsumedService,ResourceName,Cost`
3. **Check Excel**: Should have new "Combined_Sorted" sheet
4. **Check Web UI**: Should show Combined Sorted Report section with NEW badge

---

## Required CSV Format

Your input CSV must have these exact columns:
- `MeterCategory` - Azure service category
- `ConsumedService` - Specific Azure service  
- `ResourceName` - Resource identifier
- `Cost` - Numeric cost value

**Example:**
```csv
MeterCategory,ConsumedService,ResourceName,Cost
Azure App Service,microsoft.web,webapp-prod,89.75
Azure Storage,Microsoft.Storage,stg001,125.50
```

---

## Troubleshooting

### Common Issues
1. **"Missing required columns"** - Check your CSV has: MeterCategory, ConsumedService, ResourceName, Cost
2. **"File not found"** - Ensure file path is correct
3. **"Empty Combined report"** - Check that Cost column has numeric values
4. **Web server won't start** - Ensure Flask is installed: `pip install flask`

### Getting Help
- Check the sample data format in `bills/sample_fabric_bill.csv`
- Run the test script: `python test_combined_report.py`
- Use CLI for detailed error messages: `python cli.py your_file.csv`

---

## What's Changed from Original Version

### ✅ New Features
- Combined Sorted Report generation
- BillSort.csv export functionality  
- Enhanced Excel export with Combined_Sorted sheet
- New web UI elements and API endpoints
- Improved CLI with Combined Sorted Report display

### ✅ Preserved Features
- All original analysis functionality
- Same CSV input format requirements
- Same web interface (enhanced)
- Same Excel structure (with additional sheet)
- Backward compatibility maintained

---

## Ready for LinkedIn Sharing ✅

This enhanced version now includes the requested **Combined Sorted Report** feature with:
- ✅ Exact sorting: MeterCategory↑, ConsumedService↑, Cost↓  
- ✅ BillSort.csv export format
- ✅ Excel integration with Combined_Sorted sheet
- ✅ Web interface enhancements
- ✅ Full testing and documentation
- ✅ Sample data and working examples

The Microsoft Fabric Bill Analyzer is now complete with the Combined Sorted Report feature as requested!