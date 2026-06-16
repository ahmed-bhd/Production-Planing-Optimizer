import pulp

def build_model(params: dict):
    model = pulp.LpProblem("Backlog_Planning", pulp.LpMinimize)
    
    months = params["months"]
    products = params["products"]
    wf = params["workforce"]

    # Decision Variables
    prod = pulp.LpVariable.dicts("Prod", [(p["id"], t) for p in products for t in range(months)], lowBound=0, cat='Integer')
    inv = pulp.LpVariable.dicts("Inv", [(p["id"], t) for p in products for t in range(months)], lowBound=0)
    backlog = pulp.LpVariable.dicts("Backlog", [(p["id"], t) for p in products for t in range(months)], lowBound=0)
    
    workers = pulp.LpVariable.dicts("Workers", range(months), lowBound=0, cat='Integer')
    hiring = pulp.LpVariable.dicts("Hiring", range(months), lowBound=0, cat='Integer')
    firing = pulp.LpVariable.dicts("Firing", range(months), lowBound=0, cat='Integer')

    # Objective Function
    model += pulp.lpSum([
        prod[p["id"], t] * p["production_cost"] + 
        inv[p["id"], t] * p["holding_cost"] + 
        backlog[p["id"], t] * p["backlog_cost"]
        for p in products for t in range(months)
    ]) + pulp.lpSum([
        hiring[t] * wf["hiring_cost"] + 
        firing[t] * wf["firing_cost"] + 
        workers[t] * wf["regular_wage"]
        for t in range(months)
    ])

    # Constraints
    for p in products:
        for t in range(months):
            prev_inv = inv[p["id"], t-1] if t > 0 else 0
            prev_backlog = backlog[p["id"], t-1] if t > 0 else 0
            
            # Demand Fulfillment Constraint
            model += (prod[p["id"], t] + prev_inv + backlog[p["id"], t]) == \
                     (p["demand"][t] + inv[p["id"], t] + prev_backlog)

    for t in range(months):
        if t == 0:
            model += workers[t] == wf["initial_workers"] + hiring[t] - firing[t]
        else:
            model += workers[t] == workers[t-1] + hiring[t] - firing[t]
        
        model += pulp.lpSum([prod[p["id"], t] * p["capacity_usage"] for p in products]) <= \
                 workers[t] * wf["capacity_per_worker"]
        
        model += workers[t] >= 10
        
        # --- STRESS TEST: REDUCED WORKER CAPACITY ---
        # Reducing the cap makes it impossible to meet all demand, 
        # forcing the solver to use the Backlog variable.
        model += workers[t] <= 15 

    # Terminal constraint: Still requires clearing backlog by the end of the year
    for p in products:
        model += backlog[p["id"], months - 1] == 0

    return model, prod, inv, backlog