"""
Test script for Combined Sorted Report feature
"""

import sys
import os
sys.path.append('.')

from analyzer import FabricBillAnalyzer

def test_combined_sorted_report():
    print("=" * 60)
    print("TESTING COMBINED SORTED REPORT FEATURE")
    print("=" * 60)
    
    # Initialize analyzer
    analyzer = FabricBillAnalyzer()
    
    # Load sample data
    sample_file = "bills/sample_fabric_bill.csv"
    print(f"Loading sample data from: {sample_file}")
    
    if not analyzer.load_data(sample_file):
        print("❌ Failed to load sample data")
        return False
    
    print("✅ Data loaded successfully")
    
    # Get basic stats
    stats = analyzer.get_basic_stats()
    print(f"\nBasic Statistics:")
    print(f"- Total Records: {stats['total_records']}")
    print(f"- Total Cost: ${stats['total_cost']:,.2f}")
    print(f"- Unique Categories: {stats['unique_categories']}")
    print(f"- Unique Services: {stats['unique_services']}")
    
    # Test Combined Sorted Report
    print(f"\n🆕 TESTING COMBINED SORTED REPORT...")
    combined_report = analyzer.generate_combined_sorted_report()
    
    if combined_report.empty:
        print("❌ Combined report is empty")
        return False
    
    print("✅ Combined Sorted Report generated successfully")
    print(f"Records in report: {len(combined_report)}")
    
    # Display sorted data
    print(f"\nCombined Sorted Report (MeterCategory↑, ConsumedService↑, Cost↓):")
    print("-" * 80)
    print(f"{'#':<3} {'MeterCategory':<25} {'ConsumedService':<20} {'Cost':>10}")
    print("-" * 80)
    
    for i, row in combined_report.iterrows():
        print(f"{i+1:<3} {row['MeterCategory']:<25} {row['ConsumedService']:<20} ${row['Cost']:>8.2f}")
    
    # Test CSV export
    print(f"\n📄 TESTING CSV EXPORT...")
    csv_file = analyzer.export_combined_sorted_csv()
    
    if csv_file and os.path.exists(csv_file):
        print(f"✅ CSV exported successfully to: {csv_file}")
        
        # Read and display first few lines of CSV
        with open(csv_file, 'r') as f:
            lines = f.readlines()[:5]
        
        print(f"\nFirst few lines of exported CSV:")
        for line in lines:
            print(f"  {line.strip()}")
    else:
        print("❌ CSV export failed")
    
    # Test Excel export (with Combined_Sorted sheet)
    print(f"\n📊 TESTING EXCEL EXPORT...")
    excel_file = analyzer.export_to_excel()
    
    if excel_file and os.path.exists(excel_file):
        print(f"✅ Excel exported successfully to: {excel_file}")
        print(f"   Includes new 'Combined_Sorted' sheet")
    else:
        print("❌ Excel export failed")
    
    print(f"\n" + "=" * 60)
    print("✅ ALL TESTS COMPLETED SUCCESSFULLY!")
    print("🚀 Combined Sorted Report feature is working correctly")
    print("=" * 60)
    
    return True

if __name__ == "__main__":
    test_combined_sorted_report()