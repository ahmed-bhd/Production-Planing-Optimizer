import yaml
import numpy as np
import logging

def load_config(path: str) -> dict:
    """Loads a YAML file and returns the data as a dictionary."""
    with open(path, "r") as file:
        return yaml.safe_load(file)

def validate_data(params: dict, scenario_type: int = 1) -> bool:
    """
    Validates configuration based on the scenario type.
    """
    
    # --- SCENARIO 1: BASELINE VALIDATION ---
    if scenario_type == 1:
        required = ["demand", "holding_cost", "production_cost", "capacity_per_worker", "months"]
        for key in required:
            if key not in params:
                raise ValueError(f"Scenario 1: Configuration is missing: {key}")
        
        if len(params["demand"]) < params["months"]:
            needed = params["months"] - len(params["demand"])
            padding = np.random.randint(50, 150, size=needed).tolist()
            params["demand"].extend(padding)

    # --- SCENARIO 2: COMPLEX VALIDATION ---
    elif scenario_type == 2:
        required_top = ["months", "products", "workforce"]
        for key in required_top:
            if key not in params:
                raise ValueError(f"Scenario 2: Configuration is missing: {key}")
        
        for product in params["products"]:
            if len(product["demand"]) < params["months"]:
                needed = params["months"] - len(product["demand"])
                logging.info(f"Padding {product['id']} with {needed} values.")
                padding = np.random.randint(50, 150, size=needed).tolist()
                product["demand"].extend(padding)
        
        required_wf = ["initial_workers", "capacity_per_worker", "regular_wage"]
        for field in required_wf:
            if field not in params["workforce"]:
                raise ValueError(f"Scenario 2: Workforce missing: {field}")

    # --- SCENARIO 3: BACKLOG EXTENSION VALIDATION ---
    elif scenario_type == 3:
        required_top = ["months", "products", "workforce"]
        for key in required_top:
            if key not in params:
                raise ValueError(f"Scenario 3: Configuration is missing: {key}")
        
        for product in params["products"]:
            # Ensure backlog_cost is defined for each product
            if "backlog_cost" not in product:
                raise ValueError(f"Scenario 3: Product {product['id']} is missing 'backlog_cost'")
            
            # Apply padding if necessary
            if len(product["demand"]) < params["months"]:
                needed = params["months"] - len(product["demand"])
                padding = np.random.randint(50, 150, size=needed).tolist()
                product["demand"].extend(padding)
                
    else:
        raise ValueError(f"Scenario {scenario_type} is not supported.")
        
    return True