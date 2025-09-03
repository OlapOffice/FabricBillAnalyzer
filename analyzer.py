"""
Semanticia Inc. Microsoft Fabric Bill Analyzer - Enhanced with Combined Sorted Report

Copyright (c) 2025 Semanticise Inc.
Powered by Semanticise Inc. - https://semanticise.com/
This file contains the exact enhanced analyzer.py content from the artifact
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os
from typing import Dict, List, Tuple, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FabricBillAnalyzer:
    def __init__(self):
        """Initialize the Fabric Bill Analyzer with enhanced features."""
        self.df = None
        self.file_path = None
        self.analysis_timestamp = None
        
    def load_data(self, file_path: str) -> bool:
        """
        Load and validate billing data from CSV file.
        
        Args:
            file_path (str): Path to the CSV file
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Check if file exists
            if not os.path.exists(file_path):
                logger.error(f"File not found: {file_path}")
                return False
                
            # Load CSV with flexible separator detection
            try:
                self.df = pd.read_csv(file_path)
            except Exception as e:
                # Try with semicolon separator
                self.df = pd.read_csv(file_path, sep=';')
            
            self.file_path = file_path
            self.analysis_timestamp = datetime.now()
            
            logger.info(f"Loaded {len(self.df)} records from {file_path}")
            
            # Validate required columns
            required_columns = ['MeterCategory', 'ConsumedService', 'ResourceName', 'Cost']
            missing_columns = [col for col in required_columns if col not in self.df.columns]
            
            if missing_columns:
                logger.error(f"Missing required columns: {missing_columns}")
                logger.info(f"Available columns: {list(self.df.columns)}")
                return False
            
            # Clean and prepare data
            self._prepare_data()
            return True
            
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            return False
    
    def _prepare_data(self):
        """Prepare and clean the loaded data."""
        # Convert Cost to numeric, handling various formats
        if 'Cost' in self.df.columns:
            self.df['Cost'] = pd.to_numeric(self.df['Cost'], errors='coerce')
            self.df['Cost'] = self.df['Cost'].fillna(0)
        
        # Clean string columns
        string_columns = ['MeterCategory', 'ConsumedService', 'ResourceName']
        for col in string_columns:
            if col in self.df.columns:
                self.df[col] = self.df[col].astype(str).str.strip()
        
        # Handle date columns if present
        date_columns = ['Date', 'BillingDate', 'UsageDate']
        for col in date_columns:
            if col in self.df.columns:
                try:
                    self.df[col] = pd.to_datetime(self.df[col])
                except:
                    pass
        
        logger.info(f"Data prepared: {len(self.df)} records, ${self.df['Cost'].sum():,.2f} total cost")
    
    def get_basic_stats(self) -> Dict:
        """Generate basic statistics about the billing data."""
        if self.df is None:
            return {}
        
        stats = {
            'total_records': len(self.df),
            'total_cost': float(self.df['Cost'].sum()),
            'avg_cost': float(self.df['Cost'].mean()),
            'min_cost': float(self.df['Cost'].min()),
            'max_cost': float(self.df['Cost'].max()),
            'unique_services': self.df['ConsumedService'].nunique(),
            'unique_categories': self.df['MeterCategory'].nunique(),
            'unique_resources': self.df['ResourceName'].nunique(),
            'analysis_date': self.analysis_timestamp.strftime('%Y-%m-%d %H:%M:%S') if self.analysis_timestamp else 'N/A'
        }
        
        return stats
    
    def analyze_by_service(self) -> pd.DataFrame:
        """Analyze costs by consumed service."""
        if self.df is None:
            return pd.DataFrame()
        
        service_analysis = self.df.groupby('ConsumedService').agg({
            'Cost': ['sum', 'mean', 'count'],
            'ResourceName': 'nunique',
            'MeterCategory': lambda x: ', '.join(x.unique())
        }).round(2)
        
        # Flatten column names
        service_analysis.columns = ['Total_Cost', 'Avg_Cost', 'Usage_Count', 'Unique_Resources', 'Categories']
        service_analysis = service_analysis.sort_values('Total_Cost', ascending=False).reset_index()
        
        # Add percentage of total
        total_cost = self.df['Cost'].sum()
        service_analysis['Percentage'] = (service_analysis['Total_Cost'] / total_cost * 100).round(2)
        
        return service_analysis
    
    def analyze_by_category(self) -> pd.DataFrame:
        """Analyze costs by meter category."""
        if self.df is None:
            return pd.DataFrame()
        
        category_analysis = self.df.groupby('MeterCategory').agg({
            'Cost': ['sum', 'mean', 'count'],
            'ResourceName': 'nunique',
            'ConsumedService': lambda x: ', '.join(x.unique())
        }).round(2)
        
        # Flatten column names
        category_analysis.columns = ['Total_Cost', 'Avg_Cost', 'Usage_Count', 'Unique_Resources', 'Services']
        category_analysis = category_analysis.sort_values('Total_Cost', ascending=False).reset_index()
        
        # Add percentage of total
        total_cost = self.df['Cost'].sum()
        category_analysis['Percentage'] = (category_analysis['Total_Cost'] / total_cost * 100).round(2)
        
        return category_analysis
    
    def analyze_by_resource(self) -> pd.DataFrame:
        """Analyze costs by resource name."""
        if self.df is None:
            return pd.DataFrame()
        
        resource_analysis = self.df.groupby('ResourceName').agg({
            'Cost': ['sum', 'mean', 'count'],
            'ConsumedService': 'first',
            'MeterCategory': 'first'
        }).round(2)
        
        # Flatten column names
        resource_analysis.columns = ['Total_Cost', 'Avg_Cost', 'Usage_Count', 'Service', 'Category']
        resource_analysis = resource_analysis.sort_values('Total_Cost', ascending=False).reset_index()
        
        # Add percentage of total
        total_cost = self.df['Cost'].sum()
        resource_analysis['Percentage'] = (resource_analysis['Total_Cost'] / total_cost * 100).round(2)
        
        return resource_analysis
    
    def generate_combined_sorted_report(self) -> pd.DataFrame:
        """
        Generate the Combined Sorted Report with GROUPED costs by unique combinations.
        Groups records by MeterCategory + ConsumedService + ResourceName and sums costs.
        Sort by: MeterCategory↑, ConsumedService↑, Cost↓
        """
        if self.df is None:
            logger.error("No data loaded. Please load data first.")
            return pd.DataFrame()
        
        logger.info("Generating Combined Sorted Report with grouped costs...")
        
        # Group by MeterCategory, ConsumedService, and ResourceName, sum the costs
        grouped_df = self.df.groupby(['MeterCategory', 'ConsumedService', 'ResourceName']).agg({
            'Cost': 'sum'
        }).reset_index()
        
        # Sort by: MeterCategory (ascending), ConsumedService (ascending), Cost (descending)
        combined_report = grouped_df.sort_values(
            by=['MeterCategory', 'ConsumedService', 'Cost'],
            ascending=[True, True, False]
        ).reset_index(drop=True)
        
        # Round cost to 2 decimal places
        combined_report['Cost'] = combined_report['Cost'].round(2)
        
        logger.info(f"Combined Sorted Report generated: {len(combined_report)} grouped records from {len(self.df)} individual records")
        
        return combined_report
    
    def export_combined_sorted_csv(self, output_path: str = None) -> str:
        """
        Export the Combined Sorted Report to CSV format matching the BillSort.csv format.
        
        Args:
            output_path (str): Optional path for the output file
            
        Returns:
            str: Path to the exported file
        """
        combined_report = self.generate_combined_sorted_report()
        
        if combined_report.empty:
            logger.error("Cannot export: Combined report is empty")
            return None
        
        # Generate default filename if not provided
        if output_path is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"BillSort_{timestamp}.csv"
            output_path = os.path.join('reports', filename)
        
        # Ensure the reports directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        try:
            # Export to CSV with exact format
            combined_report.to_csv(output_path, index=False)
            logger.info(f"Combined Sorted Report exported to: {output_path}")
            return output_path
            
        except Exception as e:
            logger.error(f"Error exporting CSV: {str(e)}")
            return None
    
    def get_top_costs(self, limit: int = 10) -> pd.DataFrame:
        """Get top cost items."""
        if self.df is None:
            return pd.DataFrame()
        
        return self.df.nlargest(limit, 'Cost')[['MeterCategory', 'ConsumedService', 'ResourceName', 'Cost']]
    
    def search_resources(self, search_term: str) -> pd.DataFrame:
        """Search for resources containing the search term."""
        if self.df is None:
            return pd.DataFrame()
        
        mask = (
            self.df['ResourceName'].str.contains(search_term, case=False, na=False) |
            self.df['ConsumedService'].str.contains(search_term, case=False, na=False) |
            self.df['MeterCategory'].str.contains(search_term, case=False, na=False)
        )
        
        return self.df[mask][['MeterCategory', 'ConsumedService', 'ResourceName', 'Cost']]
    
    def export_to_excel(self, output_path: str = None) -> str:
        """
        Export comprehensive analysis to Excel file including the new Combined Sorted Report.
        
        Args:
            output_path (str): Path for the Excel file
            
        Returns:
            str: Path to the exported Excel file
        """
        if self.df is None:
            logger.error("No data to export")
            return None
        
        # Generate default filename if not provided
        if output_path is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"fabric_bill_analysis_{timestamp}.xlsx"
            output_path = os.path.join('reports', filename)
        
        # Ensure the reports directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        try:
            with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
                # Summary sheet
                summary_data = {
                    'Metric': ['Total Records', 'Total Cost', 'Average Cost', 'Unique Services', 'Unique Categories', 'Unique Resources'],
                    'Value': [
                        len(self.df),
                        f"${self.df['Cost'].sum():,.2f}",
                        f"${self.df['Cost'].mean():,.2f}",
                        self.df['ConsumedService'].nunique(),
                        self.df['MeterCategory'].nunique(),
                        self.df['ResourceName'].nunique()
                    ]
                }
                pd.DataFrame(summary_data).to_excel(writer, sheet_name='Summary', index=False)
                
                # Analysis sheets
                self.analyze_by_service().to_excel(writer, sheet_name='By_Service', index=False)
                self.analyze_by_category().to_excel(writer, sheet_name='By_Category', index=False)
                self.analyze_by_resource().to_excel(writer, sheet_name='By_Resource', index=False)
                
                # NEW: Combined Sorted Report sheet
                combined_report = self.generate_combined_sorted_report()
                combined_report.to_excel(writer, sheet_name='Combined_Sorted', index=False)
                
                # Top costs
                self.get_top_costs(20).to_excel(writer, sheet_name='Top_Costs', index=False)
                
                # Raw data
                self.df.to_excel(writer, sheet_name='Raw_Data', index=False)
            
            logger.info(f"Analysis exported to: {output_path}")
            return output_path
            
        except Exception as e:
            logger.error(f"Error exporting to Excel: {str(e)}")
            return None
    
    def generate_report_summary(self) -> str:
        """Generate a text summary of the analysis including new Combined Sorted Report info."""
        if self.df is None:
            return "No data loaded."
        
        stats = self.get_basic_stats()
        service_analysis = self.analyze_by_service()
        category_analysis = self.analyze_by_category()
        combined_report = self.generate_combined_sorted_report()
        
        summary = f"""
=== SEMANTICISE INC. MICROSOFT FABRIC BILL ANALYSIS REPORT ===\nPowered by Semanticise Inc. - https://semanticise.com/
Analysis Date: {stats['analysis_date']}
Data Source: {os.path.basename(self.file_path) if self.file_path else 'Unknown'}

OVERVIEW:
- Total Records: {stats['total_records']:,}
- Total Cost: ${stats['total_cost']:,.2f}
- Average Cost: ${stats['avg_cost']:,.2f}
- Cost Range: ${stats['min_cost']:,.2f} - ${stats['max_cost']:,.2f}

BREAKDOWN:
- Unique Services: {stats['unique_services']}
- Unique Categories: {stats['unique_categories']}
- Unique Resources: {stats['unique_resources']}

TOP 3 SERVICES BY COST:
"""
        for i, row in service_analysis.head(3).iterrows():
            summary += f"- {row['ConsumedService']}: ${row['Total_Cost']:,.2f} ({row['Percentage']:.1f}%)\n"
        
        summary += f"\nTOP 3 CATEGORIES BY COST:\n"
        for i, row in category_analysis.head(3).iterrows():
            summary += f"- {row['MeterCategory']}: ${row['Total_Cost']:,.2f} ({row['Percentage']:.1f}%)\n"
        
        # NEW: Combined Sorted Report summary
        summary += f"\nCOMBINED SORTED REPORT:\n"
        summary += f"- Records in sorted order: {len(combined_report)}\n"
        summary += f"- Sort criteria: MeterCategory↑, ConsumedService↑, Cost↓\n"
        summary += f"- Export format: BillSort.csv compatible\n"
        
        if not combined_report.empty:
            summary += f"\nTOP 3 HIGHEST COST ITEMS (from Combined Sorted Report):\n"
            top_costs = combined_report.head(3)
            for i, row in top_costs.iterrows():
                summary += f"- {row['MeterCategory']} > {row['ConsumedService']} > {row['ResourceName']}: ${row['Cost']:,.2f}\n"
        
        summary += f"\n=== END OF REPORT ==="
        
        return summary

def main():
    """Main function for command-line usage."""
    print("Semanticise Inc. Microsoft Fabric Bill Analyzer - Enhanced Version")
    print("🌐 Visit us at: https://semanticise.com/")
    print("=" * 60)
    
    analyzer = FabricBillAnalyzer()
    
    # Example usage
    sample_file = "bills/sample_fabric_bill.csv"
    
    if os.path.exists(sample_file):
        print(f"Loading sample data from {sample_file}...")
        if analyzer.load_data(sample_file):
            print("\n" + analyzer.generate_report_summary())
            
            # Generate Combined Sorted Report
            print("\nGenerating Combined Sorted Report...")
            combined_report = analyzer.generate_combined_sorted_report()
            print(f"Combined report contains {len(combined_report)} records")
            
            # Export to Excel and CSV
            excel_file = analyzer.export_to_excel()
            csv_file = analyzer.export_combined_sorted_csv()
            
            if excel_file:
                print(f"Excel report exported: {excel_file}")
            if csv_file:
                print(f"CSV report exported: {csv_file}")
                
        else:
            print("Failed to load sample data")
    else:
        print(f"Sample file not found: {sample_file}")
        print("Please provide a CSV file path as an argument or place sample data in the bills/ folder")

if __name__ == "__main__":
    main()
