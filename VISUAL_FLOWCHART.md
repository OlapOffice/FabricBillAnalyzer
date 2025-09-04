# 📊 Visual Flowchart: Microsoft Fabric Bill Analyzer Workflow

```mermaid
flowchart TD
    A[🏁 START: User has Azure billing data] --> B[📥 Obtain Azure billing CSV]
    
    B --> C{📋 Data Format Check}
    C -->|✅ Valid| D[🚀 Choose Launch Method]
    C -->|❌ Invalid| E[❌ Fix data format<br/>Required: MeterCategory, ConsumedService, ResourceName, Cost]
    E --> B
    
    D --> F[🖥️ Web App<br/>python run_app.py]
    D --> G[💻 CLI<br/>python cli.py]
    D --> H[🔧 Direct<br/>python app.py]
    
    F --> I[🌐 Web Dashboard<br/>http://localhost:5000]
    G --> J[📊 CLI Analysis & Export]
    H --> I
    
    I --> K[📤 Upload File]
    K --> L{✅ File Validation}
    L -->|❌ Fail| M[❌ Show error message<br/>Check format & columns]
    L -->|✅ Pass| N[🔍 Choose Analysis Type]
    M --> K
    
    N --> O[📊 Full Analysis]
    N --> P[🔍 Search Data]  
    N --> Q[🎛️ Advanced Filters]
    
    O --> R[📈 Interactive Dashboard]
    P --> S[🔎 Search Results]
    Q --> T[🎚️ Filtered Results]
    
    R --> U[📊 View Charts & Metrics]
    S --> U
    T --> U
    
    U --> V{📤 Export Choice}
    V --> W[📋 Excel Report<br/>Multi-sheet workbook]
    V --> X[📄 BillSort CSV<br/>Combined sorted report]  
    V --> Y[🔍 Search/Filter Export<br/>Custom subset]
    
    W --> Z[💼 Business Analysis]
    X --> Z
    Y --> Z
    
    Z --> AA{🔄 Continue Analysis?}
    AA -->|Yes| B
    AA -->|No| BB[🎯 END: Successful Analysis<br/>✅ Reports generated<br/>✅ Insights gained<br/>✅ Actions planned]
    
    J --> CC[📊 CLI Results]
    CC --> DD{📤 CLI Export?}
    DD -->|Yes| EE[📋 Export files]
    DD -->|No| FF[📺 View results]
    EE --> AA
    FF --> AA
    
    style A fill:#e1f5fe
    style BB fill:#c8e6c9
    style R fill:#fff3e0
    style U fill:#f3e5f5
    style Z fill:#e8f5e8
```

## 🎯 Decision Points Explained

### 📥 Data Preparation Decision Point
- **Input**: Azure billing data in various formats
- **Validation**: Check for required columns
- **Action**: Fix format if invalid, proceed if valid

### 🚀 Launch Method Decision Point  
- **Web App (Recommended)**: Best for most users, full featured
- **CLI (Advanced)**: Best for automation, batch processing
- **Direct Run**: Manual setup, for developers

### 🔍 Analysis Type Decision Point
- **Full Analysis**: Complete dashboard with all features
- **Search**: Find specific resources or services
- **Advanced Filters**: Multi-dimensional filtering

### 📤 Export Decision Point
- **Excel Report**: Comprehensive multi-sheet analysis
- **BillSort CSV**: Standardized sorted format  
- **Custom Export**: Filtered or searched results

## 🔄 User Journey Paths

### 👤 Business Analyst Path
```
Data → Web App → Upload → Full Analysis → Excel Export → Business Decisions
```

### 👩‍💻 Developer Path  
```
Data → CLI → Automated Analysis → API Integration → Ongoing Monitoring
```

### 🔍 Investigation Path
```
Data → Web App → Search/Filter → Targeted Analysis → Custom Export → Action Items
```

### 📊 Executive Path
```
Data → Web App → Quick Analysis → Interactive Charts → Presentation Export
```

## 🎨 Feature Interaction Map

```
┌─────────────────────────────────────────────────────────────┐
│                    Core Features                            │
│                                                             │
│  📊 Interactive Charts ←→ 📤 Export Functions               │
│         ↕                        ↕                         │
│  🔍 Search & Filter ←→ 📋 Combined Sorted Report            │
│         ↕                        ↕                         │
│  🎛️ Advanced Filters ←→ 💾 Multi-format Export            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 📱 Responsive Design Flow

The application adapts to different screen sizes:

- **🖥️ Desktop**: Full dashboard with all charts visible
- **📱 Tablet**: Stacked charts, touch-friendly controls  
- **📱 Mobile**: Single-column layout, swipe navigation

---

This visual flowchart complements the detailed workflow diagram to provide users with both high-level flow understanding and detailed step-by-step guidance.
