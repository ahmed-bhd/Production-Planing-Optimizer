import sys
import os
import pandas as pd
from pathlib import Path

# Path Resolver: Ensures 'src' is always discoverable
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# Imports
from src.data_loader import load_config, validate_data
from src.solver import solve_model, extract_solution
from src.scenario_2_workforce.model import build_model
from src.scenario_2_workforce.workforce import compute_workforce_metrics
from src.visualizer import plot_workforce 

def run(months=None):
    print("--- Executing Scenario 2: Multi-Product Workforce Planning ---")
    
    # 1. Setup paths
    output_dir = PROJECT_ROOT / "src" / "scenario_2_workforce" / "output"
    os.makedirs(output_dir, exist_ok=True)
    config_path = PROJECT_ROOT / "config" / "multi_product_config.yaml"
    
    # 2. Load and Validate
    params = load_config(config_path)
    if months:
        params['months'] = months
    validate_data(params, scenario_type=2)
    
    # 3. Build and Solve
    model = build_model(params)
    status = solve_model(model)
    
    # 4. Output, CSV Export, and Visualization
    if status == 1:
        solution = extract_solution(model)
        wf_data = compute_workforce_metrics(solution, params)
        
        # Convert to DataFrame
        wf_df = pd.DataFrame(wf_data)
        
        # Export to CSV
        csv_path = output_dir / "workforce_schedule.csv"
        wf_df.to_csv(csv_path, index=False)
        
        # Visualize
        plot_workforce(wf_df, output_dir=str(output_dir))
        
        print(f"\nOptimization Successful!")
        print(f"Calculated workforce for {params['months']} months.")
        print(f"Full schedule saved to: {csv_path}")
        print(f"Visualization saved to: {output_dir}")
        
        return wf_data
    else:
        print("Model failed to find an optimal solution.")
        return None

if __name__ == "__main__":
    run()