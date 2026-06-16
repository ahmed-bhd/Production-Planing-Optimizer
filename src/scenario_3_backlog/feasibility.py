def check_capacity_feasibility(params: dict):
    """
    Analyzes whether the current workforce capacity can realistically meet demand.
    Includes safe handling for demand lists shorter than the simulation period.
    """
    months = params['months']
    products = params['products']
    wf = params['workforce']
    
    # Calculate Max Possible Production per month
    max_workers = wf.get('max_workers', wf.get('initial_workers', 0))
    max_capacity_per_month = max_workers * wf.get('capacity_per_worker', 0)
    
    feasibility_report = {
        "is_feasible": True,
        "warnings": [],
        "total_capacity_gap": 0
    }
    
    for t in range(months):
        # Safely sum demand for all products, treating missing month data as 0
        total_demand_this_month = sum(
            p['demand'][t] if t < len(p['demand']) else 0 
            for p in products
        )
        
        # Only compare if demand is positive
        if total_demand_this_month > max_capacity_per_month:
            feasibility_report["is_feasible"] = False
            gap = total_demand_this_month - max_capacity_per_month
            feasibility_report["total_capacity_gap"] += gap
            
            feasibility_report["warnings"].append(
                f"Month {t+1}: Total demand ({total_demand_this_month}) exceeds "
                f"max capacity ({max_capacity_per_month}). Gap: {gap} units. Backlog expected."
            )
            
    return feasibility_report

def print_feasibility_summary(report: dict):
    """Helper to display the feasibility findings in the terminal."""
    if report["is_feasible"]:
        print("Feasibility Check: Passed (Demand is within capacity limits).")
    else:
        print("Feasibility Check: Warning - Capacity bottlenecks detected!")
        for warning in report["warnings"]:
            print(f" - {warning}")
        print(f"Total projected backlog/shortfall: {report['total_capacity_gap']} units.")