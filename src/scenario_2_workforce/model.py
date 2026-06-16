import pulp

def build_model(params: dict):
    """
    Builds the Multi-Product Workforce Planning model with 
    smoothing constraints to stabilize hiring/firing.
    """
    model = pulp.LpProblem("Multi_Product_Workforce_Planning", pulp.LpMinimize)
    months = params["months"]
    products = params["products"]
    wf = params["workforce"]

    # --- DECISION VARIABLES ---
    prod = pulp.LpVariable.dicts("Prod", [(p["id"], t) for p in products for t in range(months)], lowBound=0)
    inv = pulp.LpVariable.dicts("Inv", [(p["id"], t) for p in products for t in range(months)], lowBound=0)
    workers = pulp.LpVariable.dicts("Workers", range(months), lowBound=0, cat='Integer')
    hiring = pulp.LpVariable.dicts("Hiring", range(months), lowBound=0, cat='Integer')
    firing = pulp.LpVariable.dicts("Firing", range(months), lowBound=0, cat='Integer')

    # --- OBJECTIVE FUNCTION ---
    model += pulp.lpSum([
        prod[p["id"], t] * p["production_cost"] + inv[p["id"], t] * p["holding_cost"]
        for p in products for t in range(months)
    ]) + pulp.lpSum([
        hiring[t] * wf["hiring_cost"] + 
        firing[t] * wf["firing_cost"] + 
        workers[t] * wf["regular_wage"]
        for t in range(months)
    ])

    # --- CONSTRAINTS ---
    
    # 1. Inventory Flow Balance
    for p in products:
        for t in range(months):
            prev_inv = inv[p["id"], t-1] if t > 0 else 0
            model += inv[p["id"], t] == prev_inv + prod[p["id"], t] - p["demand"][t]

    # 2. Capacity Constraint
    for t in range(months):
        model += pulp.lpSum([prod[p["id"], t] * p["capacity_usage"] for p in products]) <= \
                 workers[t] * wf["capacity_per_worker"]

    # 3. Workforce Balance
    for t in range(months):
        prev_workers = workers[t-1] if t > 0 else wf["initial_workers"]
        model += workers[t] == prev_workers + hiring[t] - firing[t]

    # 4. Smoothing Constraints (Added to stabilize the model)
    # Prevents extreme hiring/firing fluctuations (Adjust values based on business needs)
    MAX_HIRING_PER_MONTH = 5
    MAX_FIRING_PER_MONTH = 5
    
    for t in range(months):
        model += hiring[t] <= MAX_HIRING_PER_MONTH
        model += firing[t] <= MAX_FIRING_PER_MONTH

    return model