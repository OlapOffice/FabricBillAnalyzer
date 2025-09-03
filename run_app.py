#!/usr/bin/env python3
"""
Fabric Bill Analyzer - Enhanced Flask Application Runner
Comprehensive setup and launch script with feature validation
"""

import os
import sys
import subprocess
import time
import webbrowser
import pandas as pd
from datetime import datetime

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version_info.major}.{sys.version_info.minor}")
    return True

def check_and_install_requirements():
    """Check and install required packages"""
    requirements = [
        'Flask==2.3.3',
        'pandas>=1.5.0',
        'plotly==5.17.0',
        'openpyxl>=3.0.0',
        'numpy>=1.21.0',
        'werkzeug>=2.0.0'
    ]
    
    print("📦 Checking Requirements")
    print("=" * 40)
    
    missing_packages = []
    
    for package in requirements:
        package_name = package.split('==')[0].split('>=')[0].split('<')[0]
        try:
            if package_name == 'plotly':
                import plotly
                print(f"✅ {package_name} (v{plotly.__version__})")
            elif package_name == 'pandas':
                import pandas as pd
                print(f"✅ {package_name} (v{pd.__version__})")
            elif package_name == 'Flask':
                import flask
                print(f"✅ {package_name} (v{flask.__version__})")
            elif package_name == 'openpyxl':
                import openpyxl
                print(f"✅ {package_name} (v{openpyxl.__version__})")
            elif package_name == 'numpy':
                import numpy as np
                print(f"✅ {package_name} (v{np.__version__})")
            elif package_name == 'werkzeug':
                import werkzeug
                print(f"✅ {package_name} (v{werkzeug.__version__})")
            else:
                __import__(package_name)
                print(f"✅ {package_name}")
        except ImportError:
            print(f"❌ {package_name} (not installed)")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️  Installing missing packages...")
        for package in missing_packages:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f"✅ Installed {package}")
            except subprocess.CalledProcessError:
                print(f"❌ Failed to install {package}")
                return False
    
    return True

def check_project_structure():
    """Verify project files and directories exist"""
    print("\n📁 Checking Project Structure")
    print("=" * 40)
    
    required_files = [
        'app.py',
        'analyzer.py',
        'charts.py',
        'requirements.txt',
        'templates/index.html',
        'templates/analysis.html',
        'templates/filter.html',
        'templates/search_results.html'
    ]
    
    required_dirs = [
        'templates',
        'bills',
        'reports'
    ]
    
    # Check directories
    for directory in required_dirs:
        if os.path.exists(directory):
            print(f"✅ Directory: {directory}")
        else:
            os.makedirs(directory, exist_ok=True)
            print(f"🔧 Created directory: {directory}")
    
    # Check files
    missing_files = []
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ File: {file_path}")
        else:
            print(f"❌ Missing: {file_path}")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n⚠️  Missing files: {missing_files}")
        print("Please ensure all required files are present")
        return False
    
    return True

def create_sample_data():
    """Create sample data for testing"""
    print("\n📊 Creating Sample Data")
    print("=" * 40)
    
    sample_data = {
        'MeterCategory': [
            'Azure App Service', 'Azure Cognitive Search', 'Storage', 'Storage', 
            'Azure App Service', 'Virtual Machines', 'SQL Database', 'Azure Functions',
            'Application Gateway', 'Key Vault'
        ],
        'ConsumedService': [
            'microsoft.web', 'Microsoft.Search', 'Microsoft.Storage', 'Microsoft.Storage',
            'microsoft.web', 'Microsoft.Compute', 'Microsoft.Sql', 'Microsoft.Web',
            'Microsoft.Network', 'Microsoft.KeyVault'
        ],
        'ResourceName': [
            'webapp-prod', 'search-service-main', 'storage-account-data', 'storage-blob-images',
            'function-app-api', 'vm-web-server', 'sql-db-main', 'function-app-processor',
            'app-gateway-main', 'kv-secrets-prod'
        ],
        'Cost': [125.50, 250.75, 15.25, 32.30, 85.00, 450.25, 380.90, 22.15, 95.60, 12.80],
        'ResourceGroup': [
            'rg-web-prod', 'rg-search', 'rg-storage', 'rg-storage',
            'rg-functions', 'rg-compute', 'rg-database', 'rg-functions',
            'rg-network', 'rg-security'
        ],
        'ResourceLocation': [
            'East US', 'West US', 'Central US', 'Central US', 'East US',
            'West Europe', 'East US', 'West US', 'East US', 'West US'
        ],
        'ResourceType': [
            'WebApp', 'SearchService', 'StorageAccount', 'BlobService', 'FunctionApp',
            'VirtualMachine', 'SqlDatabase', 'FunctionApp', 'ApplicationGateway', 'KeyVault'
        ],
        'MeterName': [
            'Premium Hours', 'Search Units', 'Storage GB', 'Blob Requests', 'Execution Time',
            'VM Hours', 'Database Hours', 'Execution Count', 'Gateway Hours', 'Operations'
        ]
    }
    
    df = pd.DataFrame(sample_data)
    sample_file = 'bills/sample_fabric_bill.csv'
    df.to_csv(sample_file, index=False)
    
    print(f"✅ Created: {sample_file}")
    print(f"   - {len(df)} sample records")
    print(f"   - Total cost: ${df['Cost'].sum():,.2f}")
    
    return sample_file

def run_application():
    """Launch the Flask application"""
    print("\n🚀 Starting Fabric Bill Analyzer")
    print("=" * 40)
    
    # Display startup information
    print("🌟 Semanticise Inc. Microsoft Fabric Bill Analyzer - Enhanced")
    print("📍 https://semanticise.com/")
    print("🔧 Features: Interactive Charts, Advanced Filtering, Combined Sorted Report")
    print("")
    
    # Launch info
    print("🌐 Starting web server...")
    print("📱 URL: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server")
    print("")
    
    # Wait a bit then open browser
    def open_browser():
        time.sleep(2)
        try:
            webbrowser.open('http://localhost:5000')
            print("🌍 Opened browser")
        except:
            pass
    
    import threading
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Import and run the Flask app
    try:
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"\n❌ Error starting application: {e}")

def show_features():
    """Display available features"""
    print("\n🎯 Available Features")
    print("=" * 40)
    
    features = [
        "📊 Interactive Charts (Plotly)",
        "🔍 Advanced Filtering System",
        "📑 Combined Sorted Report (NEW)",
        "🔎 Resource Search Functionality", 
        "📈 Multi-dimensional Analysis",
        "📋 Excel Export with Multiple Sheets",
        "💾 CSV Export (BillSort format)",
        "📱 Responsive Web Interface",
        "🎨 Modern Bootstrap UI",
        "⚡ Real-time Data Processing"
    ]
    
    for feature in features:
        print(f"  {feature}")

def main():
    """Main application launcher"""
    print("🚀 Fabric Bill Analyzer - Enhanced Flask Application")
    print("🏢 Powered by Semanticise Inc. - https://semanticise.com/")
    print("=" * 60)
    print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Step 1: Check Python version
    if not check_python_version():
        return
    
    # Step 2: Check and install requirements
    if not check_and_install_requirements():
        print("\n❌ Failed to install requirements. Please install manually:")
        print("pip install -r requirements.txt")
        return
    
    # Step 3: Check project structure
    if not check_project_structure():
        print("\n❌ Project structure is incomplete")
        return
    
    # Step 4: Create sample data
    sample_file = create_sample_data()
    
    # Step 5: Show features
    show_features()
    
    # Step 6: Launch application
    print(f"\n✅ All checks passed! Ready to launch.")
    input("Press Enter to start the Flask application...")
    
    run_application()

if __name__ == "__main__":
    main()
