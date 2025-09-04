# 🚀 Quick Reference Card - Microsoft Azure & Fabric Bill Analyzer

**Powered by [Semanticise Inc.](https://semanticise.com/)**

---

## ⚡ 30-Second Quick Start

1. **📥 Download** Azure billing CSV from Azure Portal
2. **🚀 Launch** with: `python run_app.py`  
3. **🌐 Open** http://localhost:5000
4. **📤 Upload** your CSV file
5. **🔍 Click** "Analyze"
6. **📊 Explore** charts and export reports!

---

## 📋 Required CSV Columns

Your file **MUST** have these exact column names:
```
✅ MeterCategory     (e.g., "Azure Storage")
✅ ConsumedService   (e.g., "Microsoft.Storage") 
✅ ResourceName      (e.g., "mystorageaccount")
✅ Cost             (e.g., 125.50)
```

---

## 🎯 Three Ways to Use

| Method | Best For | Command |
|--------|----------|---------|
| 🖥️ **Web App** | Most users | `python run_app.py` |
| 💻 **CLI** | Automation | `python cli.py` |
| 🔧 **Direct** | Developers | `python app.py` |

---

## 📊 What You Get

### 🎨 Interactive Charts
- 🥧 Service cost pie chart
- 📊 Category bar charts  
- 🏆 Top resource rankings
- 📈 Cost distribution histograms
- ☀️ Hierarchical sunburst view

### 📑 Reports & Exports
- 📋 **Excel Report**: 7 sheets with complete analysis
- 📄 **BillSort.csv**: Smart-sorted standard format
- 🔍 **Filtered Exports**: Custom data subsets
- 📊 **Chart Exports**: High-res images for presentations

### 🆕 Enhanced Features
- 🧠 **Combined Sorted Report**: Category↑ → Service↑ → Cost↓
- 🎛️ **Advanced Filters**: Multi-dimensional filtering
- 🔍 **Global Search**: Find any resource instantly  
- 🔌 **REST API**: Automation-ready endpoints

---

## 🔍 Analysis Methods

### 📊 Full Dashboard Analysis
**When**: You want complete overview
**Steps**: Upload → Analyze → Explore all charts
**Output**: Complete interactive dashboard

### 🔍 Search & Find
**When**: Looking for specific resources  
**Steps**: Upload → Search → Enter keywords
**Output**: Filtered results with highlights

### 🎛️ Advanced Filtering  
**When**: Need precise data subsets
**Steps**: Upload → Filters → Set criteria
**Output**: Real-time filtered dashboard

---

## 📤 Export Formats

| Format | Contents | Use Case |
|--------|----------|----------|
| 📋 **Excel** | 7 sheets, all analyses | Complete reporting |
| 📄 **BillSort.csv** | Sorted standard format | Data integration |
| 🔍 **Search CSV** | Filtered results only | Targeted analysis |

---

## 🔌 API Quick Reference

For automation and integration:

```bash
# Get basic stats
GET /api/stats/filename.csv

# Get combined sorted report  
GET /api/combined_report/filename.csv

# Download exports
GET /export_excel/filename.csv
GET /export_combined_csv/filename.csv
```

---

## 🚨 Common Issues & Quick Fixes

| Problem | Quick Fix |
|---------|-----------|
| ❌ "Module not found" | `pip install -r requirements.txt` |
| ❌ "Required columns missing" | Check CSV has: MeterCategory, ConsumedService, ResourceName, Cost |
| ❌ Charts not loading | Clear browser cache, check internet |
| ❌ File upload fails | Files >16MB? Use CLI instead |
| ❌ Empty results | Cost column must be numeric |

---

## 📞 Getting Azure Data

### Azure Portal Steps:
1. **Portal** → **Subscription** → **Billing**
2. **Invoices** → **Select Invoice** → **Download**  
3. **Get detailed usage CSV** (has all required columns)

### 💡 Pro Tip:
The detailed usage file from Azure contains all the columns this analyzer needs!

---

## 🎯 Best Practices

### 📅 Regular Analysis
- **Monthly**: Download new billing data
- **Compare**: Track spending trends  
- **Act**: Optimize based on insights

### 👥 Team Sharing
- **Export** Excel reports for stakeholders
- **Share** interactive charts in presentations
- **Standardize** on BillSort.csv format

### 🔄 Integration
- **Fabric Metrics App**: Use for real-time performance
- **This Analyzer**: Use for cost analysis & optimization  
- **Combined**: Complete Fabric governance

---

## 📏 File Size Limits

- **Web Upload**: 16MB maximum
- **CLI Processing**: No limits
- **Recommendation**: Use CLI for large files (>16MB)

---

## 🆘 Need Help?

- **📖 Full Guide**: Check WORKFLOW_DIAGRAM.md  
- **🎯 Visual Flow**: Check VISUAL_FLOWCHART.md
- **📧 Support**: Contact Semanticise Inc.
- **🌐 Website**: https://semanticise.com/

---

## ✨ Key Benefits

✅ **Transparency**: Clear cost visibility across all services  
✅ **Optimization**: Identify cost-saving opportunities  
✅ **Standardization**: Consistent reporting formats  
✅ **Automation**: API-ready for automated workflows  
✅ **Integration**: Works with existing Azure tools  

---

**🎉 Ready to analyze your Azure & Fabric costs?**

**Start now**: `python run_app.py` → http://localhost:5000

---

*Made with ❤️ by [Semanticise Inc.](https://semanticise.com/)*
