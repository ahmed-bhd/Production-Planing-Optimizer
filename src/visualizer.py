import matplotlib.pyplot as plt
import pandas as pd
import os

# --- VISUALIZATION LOGIC OVERVIEW ---
# Scenario 1 (Baseline): Uses plot_production, plot_inventory, plot_production_vs_demand
# Scenario 2 (Workforce): Uses plot_workforce, plot_overtime
# Scenario 3 (Backlog Extension): Uses plot_cost_breakdown, plot_dashboard, and standard plots

def plot_production(prod_df: pd.DataFrame, output_dir: str = "output"):
    """Baseline Production Visualization (Scenarios 1, 2, 3)"""
    plt.figure(figsize=(13, 7))
    plt.bar(prod_df['Month'], prod_df['Production'], color='skyblue')
    plt.title(f'Monthly Production Schedule ({len(prod_df)} Months)')
    save_figure(plt.gcf(), 'production_plot.png', output_dir)

def plot_inventory(inv_df: pd.DataFrame, output_dir: str = "output"):
    """Inventory levels for Scenarios 1 & 3"""
    plt.figure(figsize=(13, 7))
    plt.plot(inv_df['Month'], inv_df['Inventory'], marker='o', color='orange')
    plt.title('Monthly Inventory Levels')
    plt.grid(True)
    save_figure(plt.gcf(), 'inventory_plot.png', output_dir)

def plot_production_vs_demand(prod_df: pd.DataFrame, params: dict, output_dir: str = "output"):
    """Demand satisfaction analysis (Scenarios 1, 2, 3)"""
    num_months = len(prod_df)
    demand = params.get('demand', [])[:num_months]
    plt.figure(figsize=(13, 7))
    plt.bar(prod_df['Month'] - 0.2, prod_df['Production'], width=0.4, label='Production')
    plt.bar(prod_df['Month'] + 0.2, demand, width=0.4, label='Demand', color='red')
    plt.legend()
    save_figure(plt.gcf(), 'prod_vs_demand_plot.png', output_dir)

# --- SCENARIO 2: Workforce Dynamics ---
def plot_workforce(wf_df: pd.DataFrame, output_dir: str = "output"):
    """Workforce levels, hiring, and firing visualization"""
    plt.figure(figsize=(13, 7))
    plt.bar(wf_df['Month'], wf_df['Hiring'], color='green', alpha=0.3, label='Hiring')
    plt.bar(wf_df['Month'], -wf_df['Firing'], color='red', alpha=0.3, label='Firing')
    plt.plot(wf_df['Month'], wf_df['Total_Workers'], marker='o', color='purple', label='Total Workers')
    plt.legend()
    save_figure(plt.gcf(), 'workforce_plot.png', output_dir)

def plot_overtime(ot_df: pd.DataFrame, output_dir: str = "output"):
    """Overtime tracking for Scenario 2"""
    plt.figure(figsize=(13, 7))
    plt.bar(ot_df['Month'], ot_df['Overtime'], color='gold')
    plt.title('Overtime Hours per Month')
    save_figure(plt.gcf(), 'overtime_plot.png', output_dir)

# --- SCENARIO 3: Backlog & Comprehensive Analytics ---
def plot_cost_breakdown(cost_dict: dict, output_dir: str = "output"):
    """Donut chart for total cost composition (Scenarios 1, 2, 3)"""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(cost_dict.values(), labels=cost_dict.keys(), autopct='%1.1f%%', wedgeprops={'width': 0.5})
    ax.add_artist(plt.Circle((0,0), 0.70, fc='white'))
    plt.title("Cost Component Breakdown")
    save_figure(fig, 'cost_breakdown.png', output_dir)

def plot_dashboard(dfs_dict: dict, output_dir: str = "output"):
    """Combined 2x2 view for all performance KPIs (Scenarios 1, 2, 3)"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    dfs_dict['production'].plot(ax=axes[0,0], title="Production Trend")
    dfs_dict['inventory'].plot(ax=axes[0,1], title="Inventory/Backlog Levels")
    # ... additional subplot logic ...
    plt.tight_layout()
    save_figure(fig, 'dashboard.png', output_dir)

def save_figure(fig, filename: str, output_dir: str = "output"):
    """Standardized save utility for all scenarios."""
    if not os.path.exists(output_dir): os.makedirs(output_dir)
    fig.savefig(os.path.join(output_dir, filename), dpi=300, bbox_inches='tight')
    plt.close(fig)