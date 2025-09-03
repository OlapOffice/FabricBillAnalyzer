"""
Interactive Charts and Visualizations for Microsoft Fabric Bill Analyzer
Provides Plotly-based interactive charts for data visualization
"""

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import pandas as pd
import json

# Set default template for consistent styling
pio.templates.default = "plotly_white"

class FabricChartGenerator:
    def __init__(self, analyzer):
        """Initialize chart generator with analyzer instance."""
        self.analyzer = analyzer
        self.df = analyzer.df
        
    def generate_cost_by_service_pie(self) -> str:
        """Generate pie chart for cost distribution by service."""
        if self.df is None or self.df.empty:
            return ""
            
        service_data = self.df.groupby('ConsumedService')['Cost'].sum().reset_index()
        service_data = service_data.sort_values('Cost', ascending=False).head(10)
        
        fig = px.pie(
            service_data, 
            values='Cost', 
            names='ConsumedService',
            title='Cost Distribution by Service (Top 10)',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(
            showlegend=True,
            height=500,
            title_x=0.5
        )
        
        return fig.to_html(include_plotlyjs='cdn', div_id="service_pie_chart")
    
    def generate_cost_by_category_bar(self) -> str:
        """Generate bar chart for cost by category."""
        if self.df is None or self.df.empty:
            return ""
            
        category_data = self.df.groupby('MeterCategory').agg({
            'Cost': ['sum', 'count']
        }).reset_index()
        
        category_data.columns = ['MeterCategory', 'Total_Cost', 'Usage_Count']
        category_data = category_data.sort_values('Total_Cost', ascending=True)
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            y=category_data['MeterCategory'],
            x=category_data['Total_Cost'],
            orientation='h',
            name='Cost ($)',
            marker_color='rgb(55, 83, 109)',
            text=[f'${x:,.0f}' for x in category_data['Total_Cost']],
            textposition='auto'
        ))
        
        fig.update_layout(
            title='Cost Analysis by Category',
            xaxis_title='Cost ($)',
            yaxis_title='Meter Category',
            height=max(400, len(category_data) * 30),
            title_x=0.5
        )
        
        return fig.to_html(include_plotlyjs='cdn', div_id="category_bar_chart")
    
    def generate_top_resources_chart(self) -> str:
        """Generate horizontal bar chart for top cost resources."""
        if self.df is None or self.df.empty:
            return ""
            
        top_resources = self.df.nlargest(15, 'Cost')
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            y=top_resources['ResourceName'],
            x=top_resources['Cost'],
            orientation='h',
            marker_color='rgb(26, 118, 255)',
            text=[f'${x:,.2f}' for x in top_resources['Cost']],
            textposition='auto',
            hovertemplate='<b>%{y}</b><br>Cost: $%{x:,.2f}<br>Service: %{customdata[0]}<br>Category: %{customdata[1]}<extra></extra>',
            customdata=list(zip(top_resources['ConsumedService'], top_resources['MeterCategory']))
        ))
        
        fig.update_layout(
            title='Top 15 Resources by Cost',
            xaxis_title='Cost ($)',
            yaxis_title='Resource Name',
            height=600,
            title_x=0.5
        )
        
        return fig.to_html(include_plotlyjs='cdn', div_id="top_resources_chart")
    
    def generate_cost_distribution_histogram(self) -> str:
        """Generate histogram showing cost distribution."""
        if self.df is None or self.df.empty:
            return ""
            
        fig = px.histogram(
            self.df, 
            x='Cost', 
            nbins=30,
            title='Cost Distribution Histogram',
            labels={'Cost': 'Cost ($)', 'count': 'Number of Records'},
            color_discrete_sequence=['rgb(55, 83, 109)']
        )
        
        fig.update_layout(
            title_x=0.5,
            height=400
        )
        
        return fig.to_html(include_plotlyjs='cdn', div_id="cost_histogram")
    
    def generate_service_category_sunburst(self) -> str:
        """Generate sunburst chart showing category -> service -> resource hierarchy."""
        if self.df is None or self.df.empty:
            return ""
            
        # Create hierarchical data
        hierarchy_data = []
        
        # Group by category and service
        for category in self.df['MeterCategory'].unique():
            cat_data = self.df[self.df['MeterCategory'] == category]
            cat_cost = cat_data['Cost'].sum()
            
            hierarchy_data.append({
                'ids': category,
                'labels': category,
                'parents': '',
                'values': cat_cost
            })
            
            for service in cat_data['ConsumedService'].unique():
                service_data = cat_data[cat_data['ConsumedService'] == service]
                service_cost = service_data['Cost'].sum()
                
                hierarchy_data.append({
                    'ids': f"{category} - {service}",
                    'labels': service,
                    'parents': category,
                    'values': service_cost
                })
        
        df_hierarchy = pd.DataFrame(hierarchy_data)
        
        fig = go.Figure(go.Sunburst(
            ids=df_hierarchy['ids'],
            labels=df_hierarchy['labels'],
            parents=df_hierarchy['parents'],
            values=df_hierarchy['values'],
            branchvalues="total",
        ))
        
        fig.update_layout(
            title='Service Hierarchy by Category',
            title_x=0.5,
            height=500
        )
        
        return fig.to_html(include_plotlyjs='cdn', div_id="sunburst_chart")
    
    def generate_combined_dashboard(self) -> dict:
        """Generate all charts for the dashboard."""
        return {
            'service_pie': self.generate_cost_by_service_pie(),
            'category_bar': self.generate_cost_by_category_bar(),
            'top_resources': self.generate_top_resources_chart(),
            'cost_histogram': self.generate_cost_distribution_histogram(),
            'sunburst': self.generate_service_category_sunburst()
        }

def create_charts(analyzer):
    """Create chart generator instance and return charts."""
    chart_gen = FabricChartGenerator(analyzer)
    return chart_gen.generate_combined_dashboard()
