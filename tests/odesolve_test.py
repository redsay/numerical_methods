import numpy as np

from ode_solve.odesolve import ODESolver


class EulerMethod(ODESolver):
    def __init__(self, equation):
        self.equation = equation

    def solve(self, initial_conditions, t, tol):

        # t0, tf = t_span
        # t = t0

        dt = t[1] - t[0]
        solution = [initial_conditions]
 
        for t_step in range(1, t.shape[0]):
            t_i = t[t_step]
            y_old = solution[-1]
            dy_dt = self.equation(t_i, y_old)
            y_new = y_old + dt * dy_dt
            solution.append(y_new)

        solution = np.array(solution)
        is_converged = self.convergence_test(y_old, y_new, tol)

        return solution, is_converged

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

        is_converged = False

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

        if convergence == True:
            is_converged = True

        return is_converged
