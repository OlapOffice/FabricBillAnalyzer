"""
Semanticise Inc. Microsoft Fabric Bill Analyzer - Enhanced CLI
Command-line interface with Combined Sorted Report feature
"""

import argparse
import os
from analyzer import FabricBillAnalyzer

def main():
    print("="*70)
    print("🚀 SEMANTICISE INC. MICROSOFT FABRIC BILL ANALYZER - ENHANCED")
    print("🌐 Visit us at: https://semanticise.com/")
    print("🆕 NEW FEATURE: Combined Sorted Report")
    print("="*70)
    
    parser = argparse.ArgumentParser(description='Analyze Microsoft Fabric billing data')
    parser.add_argument('file', nargs='?', default='bills/sample_fabric_bill.csv', 
                       help='Path to CSV billing file (default: bills/sample_fabric_bill.csv)')
    parser.add_argument('--excel', action='store_true', help='Export to Excel')
    parser.add_argument('--csv', action='store_true', help='Export Combined Sorted Report to CSV')
    parser.add_argument('--combined', action='store_true', help='Show Combined Sorted Report')
    
    args = parser.parse_args()
    
    # Check if file exists
    if not os.path.exists(args.file):
        print(f"❌ Error: File not found: {args.file}")
        print(f"💡 Make sure the file exists or use the default sample file")
        return
    
    # Initialize analyzer
    analyzer = FabricBillAnalyzer()
    
    print(f"📂 Loading data from: {args.file}")
    
    if not analyzer.load_data(args.file):
        print(f"❌ Error: Failed to load data from {args.file}")
        print(f"💡 Check that the file has required columns: MeterCategory, ConsumedService, ResourceName, Cost")
        return
    
    # Display basic statistics
    stats = analyzer.get_basic_stats()
    print(f"\n📊 BASIC STATISTICS")
    print(f"{'─'*50}")
    print(f"Total Records:      {stats['total_records']:,}")
    print(f"Total Cost:         ${stats['total_cost']:,.2f}")
    print(f"Average Cost:       ${stats['avg_cost']:,.2f}")
    print(f"Cost Range:         ${stats['min_cost']:,.2f} - ${stats['max_cost']:,.2f}")
    print(f"Unique Services:    {stats['unique_services']}")
    print(f"Unique Categories:  {stats['unique_categories']}")
    print(f"Unique Resources:   {stats['unique_resources']}")
    
    # Show top services
    print(f"\n💰 TOP SERVICES BY COST")
    print(f"{'─'*50}")
    services = analyzer.analyze_by_service()
    if not services.empty:
        for i, row in services.head(5).iterrows():
            print(f"{row['ConsumedService']:<30} ${row['Total_Cost']:>10.2f} ({row['Percentage']:4.1f}%)")
    
    # NEW FEATURE: Combined Sorted Report
    if args.combined or not any([args.excel, args.csv]):
        print(f"\n🆕 COMBINED SORTED REPORT")
        print(f"   Sort: MeterCategory↑, ConsumedService↑, Cost↓")
        print(f"{'─'*70}")
        
        combined_report = analyzer.generate_combined_sorted_report()
        if not combined_report.empty:
            print(f"{'#':<3} {'Category':<20} {'Service':<15} {'Resource':<15} {'Cost':>10}")
            print(f"{'─'*70}")
            for i, row in combined_report.head(15).iterrows():
                category = row['MeterCategory'][:19]
                service = row['ConsumedService'][:14] 
                resource = row['ResourceName'][:14]
                print(f"{i+1:<3} {category:<20} {service:<15} {resource:<15} ${row['Cost']:>8.2f}")
            
            if len(combined_report) > 15:
                print(f"... and {len(combined_report) - 15} more records")
        else:
            print("No data available for Combined Sorted Report")
    
    # Export options
    exports_done = []
    
    if args.excel:
        print(f"\n📊 EXPORTING TO EXCEL...")
        excel_file = analyzer.export_to_excel()
        if excel_file:
            exports_done.append(f"Excel: {excel_file}")
            print(f"✅ Excel report exported: {excel_file}")
            print(f"   Includes NEW 'Combined_Sorted' sheet!")
        else:
            print(f"❌ Failed to export Excel")
    
    if args.csv:
        print(f"\n📄 EXPORTING COMBINED SORTED REPORT TO CSV...")
        csv_file = analyzer.export_combined_sorted_csv()
        if csv_file:
            exports_done.append(f"BillSort CSV: {csv_file}")
            print(f"✅ CSV report exported: {csv_file}")
            print(f"   Format: MeterCategory, ConsumedService, ResourceName, Cost")
        else:
            print(f"❌ Failed to export CSV")
    
    # Summary
    print(f"\n{'='*70}")
    print(f"✅ ANALYSIS COMPLETED SUCCESSFULLY!")
    print(f"🌐 Powered by Semanticise Inc. - https://semanticise.com/")
    if exports_done:
        print(f"📁 Files exported:")
        for export in exports_done:
            print(f"   - {export}")
    else:
        print(f"💡 Use --excel or --csv flags to export reports")
        print(f"💡 Use --combined to see the full Combined Sorted Report")
    print(f"{'='*70}")

if __name__ == "__main__":
    main()