import pulp
import pandas as pd
import os
from src.scenario_3_backlog.model import build_model
# Importing the visualizer functions
from src.visualizer import plot_production, plot_inventory, plot_production_vs_demand
# Importing solver utility
from src.solver import save_lp_file

def run(params: dict, output_dir: str):
    # 1. Capture returned variable dictionaries
    model, prod, inv, backlog = build_model(params)
    
    # 2. Export model for debugging
    # This generates an .lp file in your root folder for manual constraint inspection
    save_lp_file(model, "debug_backlog_model.lp")
    
    # 3. Solve
    status = model.solve(pulp.PULP_CBC_CMD(msg=0))
    print(f"Optimization Status: {pulp.LpStatus[status]}")
    
    results = []
    for p in params["products"]:
        for t in range(params["months"]):
            # Access values directly using the full p["id"] string
            results.append({
                "Month": t + 1,
                "Product": p["id"],
                "Production": pulp.value(prod[(p["id"], t)]),
                "Inventory": pulp.value(inv[(p["id"], t)]), # CHANGED: Use p["id"]
                "Backlog": pulp.value(backlog[(p["id"], t)])
            })
    
    # 4. Save CSV
    os.makedirs(output_dir, exist_ok=True)
    df = pd.DataFrame(results)
    output_path = os.path.join(output_dir, "backlog_schedule.csv")
    df.to_csv(output_path, index=False)
    
    print(f"Detailed schedule saved to: {output_path}")
    
    # 5. Generate Visualizations
    # Extract demand from the product list to avoid shape mismatch errors
    p1_demand = params['products'][0]['demand']
    
    plot_production(df, output_dir)
    plot_inventory(df, output_dir)
    
    # Passing the extracted demand as a dict to the plotter
    plot_production_vs_demand(df, {'demand': p1_demand}, output_dir)
    
    print(f"Visualizations generated and saved to: {output_dir}")
    
    # Final check
    total_prod = sum(r["Production"] for r in results)
    if total_prod == 0:
        print("WARNING: Total production is 0. Check capacity constraints.")
    else:
        print(f"Success! Total production scheduled: {total_prod}")