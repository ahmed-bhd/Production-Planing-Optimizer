import sys
import os
from pathlib import Path

# Fix path to ensure we can reach 'src' from the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from src.data_loader import load_config, validate_data
from src.scenario_1_baseline.model import build_model
from src.solver import solve_model, extract_solution
from src.results_exporter import (build_production_df, 
                                  build_inventory_df, 
                                  build_summary_df, 
                                  export_to_csv)
from src.visualizer import (plot_production, 
                            plot_inventory, 
                            plot_production_vs_demand
                            )

def run(months=None):
    print(f"--- Executing Scenario 1: Baseline ---")
    
    # 1. Define dynamic output directory
    output_dir = PROJECT_ROOT / "src" / "scenario_1_baseline" / "output"
    os.makedirs(output_dir, exist_ok=True)
    
    # 2. Load and validate configuration
    config_path = PROJECT_ROOT / "config" / "base_config.yaml"
    params = load_config(config_path)
    
    if months:
        params['months'] = months
        
    validate_data(params)
    
    # 3. Build and solve model
    model = build_model(params)
    status = solve_model(model)
    
    # 4. Process results if successful
    if status == 1:  # 1 means Optimal in PuLP
        solution = extract_solution(model)
        
        # Build DataFrames
        prod_df = build_production_df(solution, params)
        inv_df = build_inventory_df(solution, params)
        summary_df = build_summary_df(solution, params, model)
        
        # Export to CSV
        dfs = {"production_schedule": prod_df,
               "inventory_levels": inv_df,
               "summary": summary_df
               }
        export_to_csv(dfs, output_dir=str(output_dir))
        
        # Generate Visualizations
        plot_production(prod_df, output_dir=str(output_dir))
        plot_inventory(inv_df, output_dir=str(output_dir))
        plot_production_vs_demand(prod_df, params, output_dir=str(output_dir))
        
        print(f"\nSuccess: CSVs and Charts saved to '{output_dir}'")
        print("Model execution complete.")
    else:
        print("Failed to find optimal solution.")

if __name__ == "__main__":
    run()