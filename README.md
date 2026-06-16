# Production-Planing-Optimizer

# Production Planning Optimizer

## 1. Introduction
The **Production Planning Optimizer** is a decision-support tool designed to solve complex supply chain manufacturing problems. By leveraging Linear Programming (PuLP), this project helps operations managers minimize total costs while balancing workforce capacity, production schedules, inventory levels, and customer backlogs across multiple scenarios.

## 2. Technologies Used
* **Language:** Python
* **Optimization Solver:** PuLP (Linear Programming)
* **Data Handling:** Pandas, NumPy
* **Visualization:** Matplotlib
* **Environment:** Designed for modular scenario execution via CLI

## 3. Features
* **Multi-Scenario Support:** Easily switch between baseline (JIT), downsizing, and capacity-constrained planning scenarios.
* **Workforce Dynamics:** Handles complex hiring, firing, and regular wage cost calculations.
* **Constraint-Based Optimization:** Built-in logic for demand fulfillment, capacity limits, and end-of-horizon terminal constraints.
* **Automated Reporting:** Generates CSV exports and performance visualizations (Production vs. Demand, Inventory Levels, Workforce Dynamics) for every run.

## 4. The Process of Solution
The solution follows a structured Linear Programming (LP) workflow:
1. **Parameter Initialization:** Loading demand profiles and cost metrics.
2. **Model Formulation:** Defining decision variables (Prod, Inv, Backlog, Workforce) and the Objective Function.
3. **Constraint Enforcement:** Applying business rules (labor caps, capacity constraints, zero-backlog at term).
4. **Solver Execution:** Solving for global cost minimization using the PuLP library.
5. **Post-Processing:** Extracting results and generating diagnostic plots.

## 5. What I Learned
* **Linear Programming Trade-offs:** Gained deep insight into the cost-benefit analysis of choosing between inventory holding vs. backlog penalties.
* **Bottleneck Management:** Understood the "catch-up" effect in constrained production environments.
* **Constraint Engineering:** Learned how to enforce physical reality (like worker caps) through mathematical formulation.
* **Modular Software Design:** Developed a scalable project structure that separates model logic from data input and visualization.

## 6. How It Could Be Improved
* **Stochastic Demand:** Incorporating uncertainty (Monte Carlo simulation) rather than static demand lists.
* **Heuristic Solvers:** Moving to metaheuristics (e.g., Genetic Algorithms) for non-linear, large-scale industrial problems.
* **Web Integration:** Deploying a front-end UI (e.g., Streamlit) to make the tool accessible to non-technical stakeholders.

## 7. How to Run the Project
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/production-planning-optimizer.git](https://github.com/yourusername/production-planning-optimizer.git)

### Execution Scenario:
   * python main.py --scenario 1 --months 12
   * python main.py --scenario 2 --months 12
   * python main.py --scenario 3 --months 12

## 8. Project Structure
/production-planning-optimizer
│
├── main.py              # Entry point for scenario execution
├── src/
│   ├── scenario_1/      # Baseline scenario logic
│   ├── scenario_2/      # Downsizing scenario logic
│   └── scenario_3/      # Backlog/Constrained scenario logic
│       ├── model.py     # LP model definitions
│       └── run.py       # Execution script and plotter
└── requirements.txt     # Project dependencies
   
