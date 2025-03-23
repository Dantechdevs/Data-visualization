import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Market Analysis Data
market_data = pd.DataFrame({
    'Company': ['Competitor 1', 'Competitor 2', 'Competitor 3', 'Our Company'],
    'Market Share (%)': [25, 20, 15, 18],
    'Annual Growth (%)': [12, 8, -2, 10],
    'Profit Margin (%)': [22, 15, 10, 20],
    'Debt to Equity Ratio': [1.5, 2.0, 2.5, 1.8],
    'Return on Equity (%)': [18, 12, 8, 15]
})

# IoT Adoption Data
iot_data = pd.DataFrame({
    'Year': [2023, 2024, 2025],
    'Predictive Maintenance (%)': [40, 55, 70],
    'Remote Diagnostics (%)': [30, 45, 65],
    'Subscription Adoption (%)': [25, 40, 55]
})

# ROI Projection Data
roi_data = pd.DataFrame({
    'Year': [2023, 2024, 2025, 2026, 2027],
    'Investment ($M)': [400, 420, 450, 470, 400],
    'Expected ROI (%)': [10, 15, 22, 30, 40]
})

# 1. Market Analysis Radar Chart
def create_market_radar():
    fig = px.line_polar(market_data, r='Market Share (%)', theta='Company',
                      line_close=True, title='Market Share Distribution')
    fig.update_traces(fill='toself')
    return fig

# 2. Financial Health Comparison
def create_financial_comparison():
    fig = make_subplots(rows=1, cols=3, subplot_titles=('Profit Margin', 'Debt/Equity', 'ROE'))
    
    metrics = ['Profit Margin (%)', 'Debt to Equity Ratio', 'Return on Equity (%)']
    colors = ['#2E91A5', '#E15F99', '#1CA71C']
    
    for i, metric in enumerate(metrics):
        fig.add_trace(go.Bar(
            x=market_data['Company'],
            y=market_data[metric],
            name=metric,
            marker_color=colors[i]
        ), row=1, col=i+1)
        
    fig.update_layout(height=400, showlegend=False)
    return fig

# 3. IoT Adoption Trends
def create_iot_trends():
    fig = px.line(iot_data, x='Year', y=iot_data.columns[1:],
                title='IoT Feature Adoption Trends',
                labels={'value': 'Adoption Rate (%)'},
                markers=True)
    fig.update_layout(hovermode='x unified')
    return fig

# 4. ROI Projection Analysis
def create_roi_analysis():
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(go.Bar(
        x=roi_data['Year'],
        y=roi_data['Investment ($M)'],
        name='Investment',
        marker_color='#636EFA'
    ), secondary_y=False)
    
    fig.add_trace(go.Scatter(
        x=roi_data['Year'],
        y=roi_data['Expected ROI (%)'],
        name='ROI Projection',
        mode='lines+markers',
        line=dict(color='#FF6692')
    ), secondary_y=True)
    
    fig.update_layout(
        title='IoT Investment vs ROI Projection',
        yaxis_title='Investment ($M)',
        yaxis2_title='ROI (%)'
    )
    return fig

# Display all visualizations
create_market_radar().show()
create_financial_comparison().show()
create_iot_trends().show()
create_roi_analysis().show()
