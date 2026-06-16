import pulp
import logging

def solve_model(model: pulp.LpProblem):
    """
    Invokes the CBC solver and logs the result.
    """
    solver = pulp.PULP_CBC_CMD(msg=False)
    status = model.solve(solver)
    
    check_solver_status(status)
    return status

def check_solver_status(status: int):
    """
    Interprets the solver status code.
    """
    status_msg = pulp.LpStatus[status]
    if status_msg == 'Optimal':
        logging.info("Solution found: Optimal")
    else:
        logging.warning(f"Solution not found. Status: {status_msg}")

def extract_solution(model: pulp.LpProblem) -> dict:
    """
    Extracts variable values from the solved model into a dictionary.
    """
    solution = {}
    for var in model.variables():
        solution[var.name] = var.varValue
    return solution

def save_lp_file(model: pulp.LpProblem, path: str):
    """
    Exports the model to an .lp file for debugging purposes.
    The .lp format is human-readable and lists all constraints and variables.
    """
    try:
        model.writeLP(path)
        logging.info(f"Model successfully exported to {path}")
    except Exception as e:
        logging.error(f"Failed to export LP file: {e}")