import numpy as np
from odesolve_test import EulerMethod

from ode_solve.odeutilities import Utilities


def test_euler_solver():
    """
    Designed to test the EulerMethod in ODESolve()

    Parameters:
        - None

    Returns
        - None
    """

    # initialize the forward euler method
    euler_solver = EulerMethod(equation)

    # set initial conditions for numerical solution
    inital_conditions = 1  # y(0) = 1
    # integration from t_0=0 to t_f=2
    t_0 = 0
    t_f = 2
    # set time-step resolution
    dt = [0.05, 0.1]
    # convergence tolerance
    tol = 0.01

    # initial conditions for analytic solution
    t_analytic = np.arange(t_0, t_f, 0.1)

    # solve analytically
    analytic_result = analytical_solution(t_analytic, inital_conditions)
    analytic_result = np.array(analytic_result)

    # lists for plotting
    all_results = [(analytic_result, t_analytic)]
    all_labels = ["Analytic Solution"]

    # compute the ODE for list of time-steps
    for dt_i in dt:
        t = np.arange(t_0, t_f, dt_i)
        # solve
        numeric_result, is_converged = euler_solver.solve(inital_conditions, t, tol)
        all_results.append((numeric_result, t))
        all_labels.append("$\Delta t$ = %s" % (str(dt_i)))

        # return numeric_result and convergence at the last time stamp,
        # if is_converged:
        #     print(
        #         "The converged solution to the ODE y'=-2y is %s comapred to the analytical solution %s"
        #         % (str(numeric_result[-1]), analytic_result[-1])
        #     )
        # else:
        #     print(
        #         "The solution to y'=-2y is %s but has not converged." % (str(numeric_result[-1]))
        #     )

    # plot the results
    plot_results = Utilities().plot_solution(
        all_results, "Analytical solution vs. Forward Euler method", all_labels
    )


def equation(t, y):
    """
    Test equation (dy_dt = -2y ). strictly y-dependent

    Parameters:
        - t: t_values
        - y: y_values
    """
    return -2 * y


def analytical_solution(t, y0):
    """
    Analytic solution to dy_dt = -2y

    Parameters:
        - t: t_values
        - y0: inital y
    """
    return y0 * np.exp(-2 * t)


# run the test
test_euler_solver()
