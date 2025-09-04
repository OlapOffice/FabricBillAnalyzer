# 🚀 Microsoft Azure & Fabric Bill Analyzer - Enhanced Edition
## Detailed User Workflow Diagram

**Powered by [Semanticise Inc.](https://semanticise.com/)**

---

## 📋 Pre-Requisites Checklist

### ✅ **Data Preparation**
Your CSV/Excel file **MUST** contain these columns:
- `MeterCategory` - Service category (e.g., "Storage", "Azure App Service")
- `ConsumedService` - Service name (e.g., "Microsoft.Storage")
- `ResourceName` - Resource identifier
- `Cost` - Billing cost (numeric)

### ✅ **System Requirements**
- Python 3.7 or higher
- 2GB RAM minimum
- Web browser (Chrome, Firefox, Safari, Edge)
- Internet connection (for interactive charts)

---

## 🔄 Complete User Workflow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         🏁 START: Getting Your Data                           │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    📥 Step 1: Obtain Azure Billing Data                      │
│                                                                               │
│   🌐 Azure Portal → Subscription → Billing → Invoices → Download             │
│                                                                               │
│   ✅ Download detailed usage CSV file                                        │
│   ✅ Verify required columns are present                                     │
│   ✅ Check file size (max 16MB via web, unlimited via CLI)                  │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                     🚀 Step 2: Launch the Application                        │
│                                                                               │
│   Choose your method:                                                         │
│   ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐                │
│   │  🖥️ Web App      │ │  💻 Command Line │ │  🔧 Direct Run   │                │
│   │                 │ │                 │ │                 │                │
│   │ python run_app.py│ │  python cli.py   │ │  python app.py   │                │
│   │ (Recommended)   │ │  (Advanced)     │ │  (Manual)       │                │
│   └─────────────────┘ └─────────────────┘ └─────────────────┘                │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                    ┌─────────────────┬─┴─────────────────┐
                    │                 │                   │
                    ▼                 ▼                   ▼
         ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
         │   Web Interface  │ │  Command Line   │ │   Test Suite    │
         │  (Most Users)   │ │   (Advanced)    │ │  (Validation)   │
         └─────────────────┘ └─────────────────┘ └─────────────────┘
                    │                 │                   │
                    │                 ▼                   │
                    │    📊 CLI Analysis & Export         │
                    │    • Basic analysis                 │
                    │    • Combined report                │
                    │    • Excel/CSV export              │
                    │    • Batch processing              │
                    │                                     │
                    ▼                                     ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                 🌐 Step 3: Web Dashboard (http://localhost:5000)             │
│                                                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                     📁 File Management Section                       │   │
│   │                                                                     │   │
│   │   • View previously uploaded files                                  │   │
│   │   • Check file sizes and details                                   │   │
│   │   • Delete old files if needed                                     │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                       │                                       │
│                                       ▼                                       │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                      📤 Upload New File                             │   │
│   │                                                                     │   │
│   │   • Drag & drop or browse for file                                 │   │
│   │   • Automatic file validation                                      │   │
│   │   • Progress indicator                                             │   │
│   │   • Error messages for invalid files                               │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                        ✅ Step 4: File Validation                            │
│                                                                               │
│   Automatic checks performed:                                                │
│   ✅ File format validation (CSV, Excel)                                     │
│   ✅ Required columns verification                                           │
│   ✅ Data type validation (Cost column numeric)                             │
│   ✅ Empty data detection                                                    │
│                                                                               │
│   ❌ If validation fails: Error message with specific guidance               │
│   ✅ If validation passes: Ready for analysis                                │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      🔍 Step 5: Choose Analysis Method                       │
│                                                                               │
│   ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐                │
│   │  📊 Full Analysis│ │  🔍 Search Data  │ │  🎛️ Advanced    │                │
│   │                 │ │                 │ │    Filters      │                │
│   │ • Complete      │ │ • Find specific │ │                 │                │
│   │   dashboard     │ │   resources     │ │ • Multi-filter  │                │
│   │ • All charts    │ │ • Keyword search│ │ • Custom ranges │                │
│   │ • All reports   │ │ • Export results│ │ • Real-time     │                │
│   │                 │ │                 │ │   updates       │                │
│   └─────────────────┘ └─────────────────┘ └─────────────────┘                │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                 📊 Step 6: Full Analysis Dashboard                           │
│                                                                               │
│   🎯 Key Metrics Section:                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  💰 Total Cost    │  🏢 Services    │  📦 Categories  │  🔧 Resources │   │
│   │  $X,XXX.XX       │  XX services    │  XX categories  │  XX resources │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                               │
│   📈 Interactive Charts Section:                                              │
│   ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐                │
│   │ 🥧 Service Pie   │ │ 📊 Category Bar │ │ 🏆 Top Resources│                │
│   │                 │ │                 │ │                 │                │
│   │ • Hover details │ │ • Sorted by     │ │ • Highest costs │                │
│   │ • Click to zoom │ │   cost          │ │ • Clickable     │                │
│   │ • Export image  │ │ • Interactive   │ │ • Drill-down    │                │
│   └─────────────────┘ └─────────────────┘ └─────────────────┘                │
│                                                                               │
│   ┌─────────────────┐ ┌─────────────────┐                                    │
│   │ 📊 Cost Histogram│ │ ☀️ Sunburst     │                                    │
│   │                 │ │   Hierarchy     │                                    │
│   │ • Distribution  │ │                 │                                    │
│   │ • Binning       │ │ • Multi-level   │                                    │
│   │ • Statistics    │ │ • Category drill│                                    │
│   └─────────────────┘ └─────────────────┘                                    │
│                                                                               │
│   🆕 Combined Sorted Report Section:                                          │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  📋 Intelligent Sorting: Category↑ → Service↑ → Cost↓                │   │
│   │                                                                     │   │
│   │  • Groups similar services together                                │   │
│   │  • Shows highest costs first within each service                   │   │
│   │  • Ready for BillSort.csv export                                   │   │
│   │  • Preview table with first 10 rows                                │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      📤 Step 7: Export & Download Options                    │
│                                                                               │
│   Choose your export format:                                                 │
│                                                                               │
│   ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐                │
│   │ 📊 Excel Report │ │ 📄 BillSort CSV │ │ 🔍 Search Export│                │
│   │                 │ │                 │ │                 │                │
│   │ • Multi-sheet   │ │ • Combined      │ │ • Filtered data │                │
│   │ • All analyses  │ │   sorted report │ │ • Search results│                │
│   │ • Charts        │ │ • Standardized  │ │ • Custom subset │                │
│   │ • Raw data      │ │   format        │ │                 │                │
│   └─────────────────┘ └─────────────────┘ └─────────────────┘                │
│                                                                               │
│   Excel Report Contains:                                                      │
│   📋 Summary Sheet - Overview and key metrics                                │
│   🏢 By_Service Sheet - Analysis by consumed service                         │
│   📦 By_Category Sheet - Analysis by meter category                          │
│   🔧 By_Resource Sheet - Analysis by resource name                           │
│   🆕 Combined_Sorted Sheet - Intelligent sorting                             │
│   🏆 Top_Costs Sheet - Highest cost items                                    │
│   📊 Raw_Data Sheet - Original data                                          │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    🔍 Alternative Path: Search Functionality                 │
│                                                                               │
│   From main analysis page, click "Search Data":                              │
│                                                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  🔎 Global Search Features                                           │   │
│   │                                                                     │   │
│   │  • Search across all fields (Resource, Service, Category)          │   │
│   │  • Partial matching and wildcards                                  │   │
│   │  • Highlighted results                                             │   │
│   │  • Real-time search as you type                                   │   │
│   │  • Export search results                                          │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                               │
│   Example searches:                                                           │
│   • "storage" - Find all storage-related items                               │
│   • "prod" - Find production resources                                       │
│   • "microsoft.web" - Find specific services                                 │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                 🎛️ Alternative Path: Advanced Filtering                      │
│                                                                               │
│   From main analysis page, click "Advanced Filters":                         │
│                                                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  🎚️ Multi-Dimensional Filtering                                     │   │
│   │                                                                     │   │
│   │  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐       │   │
│   │  │ 📦 Category     │ │ 🏢 Service      │ │ 💰 Cost Range   │       │   │
│   │  │ Filter          │ │ Filter          │ │ Slider          │       │   │
│   │  │                 │ │                 │ │                 │       │   │
│   │  │ • Dropdown list │ │ • Dropdown list │ │ • Min/Max costs │       │   │
│   │  │ • Multi-select  │ │ • Multi-select  │ │ • Real-time     │       │   │
│   │  │ • Dynamic update│ │ • Dynamic update│ │   filtering     │       │   │
│   │  └─────────────────┘ └─────────────────┘ └─────────────────┘       │   │
│   │                                                                     │   │
│   │  ┌─────────────────────────────────────────────────────────────┐   │   │
│   │  │ 🔤 Text Search: Find specific resources by name            │   │   │
│   │  └─────────────────────────────────────────────────────────────┘   │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                               │
│   🔄 Real-time Results:                                                       │
│   • Results update as you change filters                                     │
│   • Count of filtered items shown                                            │
│   • Export filtered data available                                           │
│   • Reset all filters button                                                 │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    📊 Step 8: API Access (Advanced Users)                    │
│                                                                               │
│   For developers and automation:                                              │
│                                                                               │
│   🔌 REST API Endpoints:                                                      │
│   ├── GET /api/stats/<filename>           - Basic statistics JSON            │
│   ├── GET /api/combined_report/<filename> - 🆕 Combined sorted report        │
│   ├── GET /export_excel/<filename>        - Download Excel report            │
│   └── GET /export_combined_csv/<filename> - 🆕 Download BillSort.csv         │
│                                                                               │
│   💡 Use cases:                                                               │
│   • Automated reporting                                                       │
│   • Integration with other tools                                             │
│   • Batch processing multiple files                                          │
│   • Custom dashboard development                                             │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                     🔄 Step 9: Ongoing Analysis & Monitoring                 │
│                                                                               │
│   📅 Regular Workflow Recommendations:                                        │
│                                                                               │
│   ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐                │
│   │ 📆 Monthly       │ │ 📈 Trend        │ │ 🎯 Cost         │                │
│   │ Analysis        │ │ Analysis        │ │ Optimization    │                │
│   │                 │ │                 │ │                 │                │
│   │ • Download new  │ │ • Compare       │ │ • Identify      │                │
│   │   billing data  │ │   monthly costs │ │   top spenders  │                │
│   │ • Upload & run  │ │ • Track service │ │ • Find unused   │                │
│   │   analysis      │ │   growth        │ │   resources     │                │
│   │ • Generate      │ │ • Monitor       │ │ • Plan budget   │                │
│   │   reports       │ │   patterns      │ │   adjustments   │                │
│   └─────────────────┘ └─────────────────┘ └─────────────────┘                │
│                                                                               │
│   🔗 Integration with Microsoft Fabric Capacity Metrics:                     │
│   • Use this analyzer for: Historical cost analysis & optimization           │
│   • Use Fabric Metrics App for: Real-time performance monitoring             │
│   • Combined insights provide complete visibility                             │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                        🎯 Step 10: Results & Action Items                    │
│                                                                               │
│   📋 What You Get:                                                            │
│   ✅ Complete cost breakdown by service, category, and resource               │
│   ✅ Interactive visualizations for presentations                             │
│   ✅ BillSort.csv for standardized reporting                                 │
│   ✅ Multi-sheet Excel report for detailed analysis                          │
│   ✅ Filtered and searchable data views                                      │
│                                                                               │
│   🎯 Recommended Actions:                                                     │
│   1. 🔍 Review top cost items first                                          │
│   2. 📊 Identify cost optimization opportunities                              │
│   3. 📈 Share interactive charts with stakeholders                           │
│   4. 📅 Schedule regular monthly analysis                                     │
│   5. 🔗 Set up automated reporting if needed                                 │
│                                                                               │
│   💼 Business Value:                                                          │
│   • Transparent Azure/Fabric cost visibility                                 │
│   • Data-driven cost optimization decisions                                  │
│   • Standardized reporting across teams                                      │
│   • Historical trend analysis capabilities                                   │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           🔚 END: Successful Analysis                        │
│                                                                               │
│   🎉 Congratulations! You have successfully:                                 │
│   ✅ Analyzed your Microsoft Fabric/Azure billing data                       │
│   ✅ Generated comprehensive reports and visualizations                       │
│   ✅ Exported data in multiple formats for further use                       │
│   ✅ Gained insights into your cloud spending patterns                       │
│                                                                               │
│   🔄 Next Steps:                                                              │
│   • Save your reports for future reference                                   │
│   • Share findings with your team                                            │
│   • Plan cost optimization initiatives                                       │
│   • Schedule your next analysis                                              │
│                                                                               │
│   🆘 Need Help?                                                               │
│   📧 Contact: Semanticise Inc. Support                                       │
│   🌐 Website: https://semanticise.com/                                       │
└─────────────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════════

## 🚨 Troubleshooting Quick Reference

### Common Issues & Solutions

| Issue | Cause | Solution |
|-------|--------|----------|
| ❌ "Module not found" | Missing dependencies | Run: `pip install -r requirements.txt` |
| ❌ "Required columns missing" | Wrong CSV format | Ensure: MeterCategory, ConsumedService, ResourceName, Cost |
| ❌ Charts not loading | Browser/Internet issue | Check connection, clear cache |
| ❌ File upload fails | File too large | Use CLI for files >16MB |
| ❌ Empty results | Data format issue | Check Cost column is numeric |

### File Format Requirements

```
✅ CORRECT CSV FORMAT:
MeterCategory,ConsumedService,ResourceName,Cost
Azure Storage,Microsoft.Storage,mystorageaccount,125.50
Azure App Service,microsoft.web,mywebapp,89.75
```

```
❌ INCORRECT FORMAT:
Category,Service,Name,Price  ← Wrong column names
Storage,Storage Service,,     ← Missing values
```

### Performance Tips

- **Small files (<1MB)**: Use web interface
- **Large files (>16MB)**: Use command line interface
- **Batch processing**: Use CLI with scripts
- **Regular analysis**: Set up automated workflows

═══════════════════════════════════════════════════════════════════════════════

## 🎯 Quick Start Summary

1. **📥 Get Data**: Download Azure billing CSV from portal
2. **🚀 Launch**: Run `python run_app.py` 
3. **📤 Upload**: Drag & drop your CSV file
4. **🔍 Analyze**: Click "Analyze" button
5. **📊 Explore**: View charts and reports
6. **📤 Export**: Download Excel or BillSort.csv
7. **🔄 Repeat**: Monthly for ongoing monitoring

**🌐 Access**: http://localhost:5000

---

**Made with ❤️ by [Semanticise Inc.](https://semanticise.com/)**

*This workflow diagram provides complete guidance for users at all technical levels - from business analysts to developers - to successfully use the Microsoft Fabric Bill Analyzer Enhanced Edition.*
