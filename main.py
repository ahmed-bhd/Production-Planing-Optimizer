import argparse
import sys
import os
from pathlib import Path

# Add the project root to path
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# --- SCENARIO 1 ENTRY POINT ---
def run_scenario_1(months):
    os.makedirs("output", exist_ok=True)
    from src.scenario_1_baseline.run import run
    run(months=months)

# --- SCENARIO 2 ENTRY POINT ---
def run_scenario_2(months):
    from src.scenario_2_workforce.run import run
    run(months=months)

# --- SCENARIO 3 ENTRY POINT ---
def run_scenario_3(months):
    from src.data_loader import load_config, validate_data
    from src.scenario_3_backlog.run import run
    
    # 1. Load and Validate
    config_path = PROJECT_ROOT / "config" / "infeasible_demand_config.yaml"
    params = load_config(config_path)
    params['months'] = months
    
    # CRITICAL: This validates that demand, costs, and workforce are properly loaded
    validate_data(params, scenario_type=3)
    
    # 2. Debug logging
    print(f"DEBUG: Successfully validated {len(params['products'])} products.")
    for p in params['products']:
        print(f"DEBUG: Product {p['id']} demand list length: {len(p['demand'])}")
    
    # 3. Execution
    output_dir = PROJECT_ROOT / "src" / "scenario_3_backlog" / "output"
    run(params, output_dir=str(output_dir))

def main():
    parser = argparse.ArgumentParser(description="Production Planning Optimizer")
    parser.add_argument("--scenario", type=int, choices=[1, 2, 3], required=True)
    parser.add_argument("--months", type=int, nargs="?", help="Number of months")
    
    args = parser.parse_args()

    # Default to 12 if not provided
    if args.months is None:
        args.months = 12

    # Routing
    if args.scenario == 3:
        run_scenario_3(args.months)
    elif args.scenario == 1:
        run_scenario_1(args.months)
    elif args.scenario == 2:
        run_scenario_2(args.months)
    else:
        print("Scenario not supported.")

if __name__ == "__main__":
    main()