import pulp
import logging

def build_model(params: dict) -> pulp.LpProblem:
    """
    Builds the baseline Single-Product MILP model.
    """
    months = params["months"]
    demand = params["demand"] # This includes the auto-extended data
    
    holding_cost = params["holding_cost"]
    prod_cost = params["production_cost"]
    capacity = params["fixed_workforce"] * params["capacity_per_worker"]
    
    # Initialize Model
    model = pulp.LpProblem("Production_Planning_Baseline", pulp.LpMinimize)
    
    # Decision Variables
    production = pulp.LpVariable.dicts("Prod", range(months), lowBound=0, cat='Continuous')
    inventory = pulp.LpVariable.dicts("Inv", range(months), lowBound=0, cat='Continuous')
    
    # Objective Function
    model += pulp.lpSum([production[i] * prod_cost + inventory[i] * holding_cost for i in range(months)])
    
    # Constraints
    inventory_prev = params.get("initial_inventory", 0)
    
    for i in range(months):
        # 1. Inventory Balance
        model += inventory[i] == inventory_prev + production[i] - demand[i]
        
        # 2. Capacity Constraint
        model += production[i] <= capacity
        
        inventory_prev = inventory[i]
        
    logging.info(f"Baseline model built for {months} months.")
    return model