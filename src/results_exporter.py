import pandas as pd
import pulp
import os

# --- REPORTING LOGIC OVERVIEW ---
# Scenario 1 (Baseline): Uses build_production_df, build_inventory_df, build_summary_df
# Scenario 2 (Workforce): Adds usage of 'Workers' variables in compute_kpis
# Scenario 3 (Backlog Extension): Adds usage of 'Backlog' variables in build_summary_df/kpis

def build_production_df(solution: dict, params: dict) -> pd.DataFrame:
    """Production data (Scenarios 1, 2, & 3)"""
    data = []
    num_months = params['months']
    for t in range(num_months):
        # Scenario 1, 2, 3: Extract production variable
        val = solution.get(f"Prod_P1_{t}", 0) 
        data.append({"Month": t + 1, "Production": val})
    return pd.DataFrame(data)

def build_inventory_df(solution: dict, params: dict) -> pd.DataFrame:
    """Inventory data (Scenarios 1 & 3 - Scenario 2 typically ignores inv)"""
    data = []
    num_months = params['months']
    for t in range(num_months):
        val = solution.get(f"Inv_P1_{t}", 0)
        data.append({"Month": t + 1, "Inventory": val})
    return pd.DataFrame(data)

def build_summary_df(solution: dict, params: dict, model: pulp.LpProblem) -> pd.DataFrame:
    """Total cost summary (Scenarios 1, 2, & 3)"""
    total_cost = pulp.value(model.objective)
    num_months = params['months']
    avg_prod = sum([solution.get(f"Prod_P1_{t}", 0) for t in range(num_months)]) / num_months
    
    # Scenario 3 specific: Includes Backlog in summary if applicable
    summary_data = {
        "Metric": ["Total Cost", "Average Monthly Production", "Final Inventory"],
        "Value": [
            total_cost,
            avg_prod,
            solution.get(f"Inv_P1_{num_months - 1}", 0)
        ]
    }
    summary_df = pd.DataFrame(summary_data)
    summary_df['Value'] = summary_df['Value'].map('$ {:,.2f}'.format)
    return summary_df

def compute_kpis(solution: dict, params: dict) -> pd.DataFrame:
    """
    KPI Calculations:
    - Scenario 1: Basic utilization.
    - Scenario 2: Includes workforce count data.
    - Scenario 3: Includes backlog handling turnover ratios.
    """
    num_months = params['months']
    capacity_per_worker = params['workforce']['capacity_per_worker']
    
    total_prod = sum(solution.get(f"Prod_P1_{t}", 0) for t in range(num_months))
    # Scenario 2 & 3: Uses Workers variable
    total_workers = sum(solution.get(f"Workers_{t}", 0) for t in range(num_months))
    total_capacity = total_workers * capacity_per_worker
    
    utilization = (total_prod / total_capacity) * 100 if total_capacity > 0 else 0
    total_inv = sum(solution.get(f"Inv_P1_{t}", 0) for t in range(num_months))
    turnover = total_prod / (total_inv / num_months) if total_inv > 0 else 0
    
    kpi_data = {
        "Metric": ["Capacity Utilization (%)", "Inventory Turnover Ratio"],
        "Value": [round(utilization, 2), round(turnover, 2)]
    }
    return pd.DataFrame(kpi_data)

def export_to_csv(data_frames: dict, output_dir: str = "output"):
    """Global export function used by Scenarios 1, 2, and 3."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for name, df in data_frames.items():
        df.to_csv(os.path.join(output_dir, f"{name}.csv"), index=False)