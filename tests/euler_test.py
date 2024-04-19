import numpy as np
from odesolve_test import EulerMethod


def test_euler_solver():
    # define a simple first-order ODE
    def equation(t, y):
        return -2 * y

    def analytical_solution(t, y0):
        return y0 * np.exp(-2 * t)

    euler_solver = EulerMethod(equation)

    # set initial conditions
    inital_conditions = 1  # y(0) = 1
    t_span = (0, 2)  # integration from t=0 to t=1

    # solve the ODE
    solution, is_converged = euler_solver.solve(inital_conditions, t_span)

    # return solution and convergence at last time stamp.
    if is_converged:
        print(
            "The converged solution to the ODE y'=-2y is %s comapred to the analytical solution %s"
            % (str(solution[-1]), analytical_solution(t_span[1], inital_conditions))
        )
    else:
        print(
            "The solution to y'=-2y is %s but has not converged." % (str(solution[-1]))
        )


test_euler_solver()
