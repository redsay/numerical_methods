import numpy as np

from ode_solve.odesolve import ODESolver
from ode_solve.odeutilities import Validation


class EulerMethod(ODESolver):
    def __init__(self, equation):
        self.equation = equation

    def solve(self, initial_condition, t_span):

        # validate the initial conditions
        Validation.validate_conditions(initial_condition, t_span)

        dt = t_span[1] - t_span[0]
        solution = [initial_condition]

        for t_step in range(1, t_span.shape[0]):
            t_i = t_span[t_step]
            y_old = solution[-1]
            try:
                dy_dt = self.equation(t_i, y_old)
            except:
                print(f"An error occured while evaluating the function{self.equation}")
            y_new = y_old + dt * dy_dt
            solution.append(y_new)

        solution = np.array(solution)

        return solution

    def set_parameters(self, parameters):
        """
        Set parameters of the ODE system

        Parameters:
        - parameters: DIctionary containing parameters for the ODE system
        """
        # Parameters are not required for the EuelerMethod
        pass

    def convergence_test(self, solution_old, solution_new, tolerance):
        """
        Performs a convergence test to check if the solution has converged

        Parameters:
        - solution_old: prvious solution
        - solution_new: current solution
        - tolerance: tolerance level for convergence testing

        Returns:
        - is_converged: boolean indicating whether the solution has converged
        """
        # Handle case where solution_old and solution_new are single floats
        if isinstance(solution_old, (int, float)) and isinstance(
            solution_new, (int, float)
        ):
            convergence = abs(solution_new - solution_old) < tolerance
        else:
            # Check if the difference between two consecutive solutions is within the tolerance
            convergence = (
                max(
                    abs(sol_new - sol_old)
                    for sol_old, sol_new in zip(solution_old, solution_new)
                )
                < tolerance
            )

        if convergence == False:
            msg = "The solution is not converged w.r.t the analytic solution. Try to adjust the resolution"
        else:
            msg = "The solution is converged w.r.t the analytic solution"
        return msg
