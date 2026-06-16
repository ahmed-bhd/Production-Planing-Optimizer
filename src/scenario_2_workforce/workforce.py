def compute_workforce_metrics(solution: dict, params: dict):
    """
    Computes hiring, firing, and total workforce per month.
    """
    months = params["months"]
    metrics = []
    for t in range(months):
        metrics.append({
            "Month": t + 1,
            "Total_Workers": solution.get(f"Workers_{t}", 0),
            "Hiring": solution.get(f"Hiring_{t}", 0),
            "Firing": solution.get(f"Firing_{t}", 0)
        })
    return metrics