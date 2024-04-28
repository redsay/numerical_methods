import numpy as np
from odesolve_test import EulerMethod

from ode_solve.odeutilities import Utilities, Validation


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

    t_span = [0, 2]
    # set time-step resolution
    dt = [0.25, 0.05]
    # convergence tolerance
    tol = 0.01

    # initial conditions for analytic solution
    t_analytic = np.arange(t_span[0], t_span[1], 0.1)

    # solve analytically
    analytic_result = analytical_solution(t_analytic, inital_conditions)
    analytic_result = np.array(analytic_result)

    # lists for plotting
    all_results = [(analytic_result, t_analytic)]
    all_labels = ["Analytic Solution"]

    # compute the ODE for list of time-steps
    for dt_i in dt:
        t = np.arange(t_span[0], t_span[1], dt_i)
        # solve
        numeric_result = euler_solver.solve(inital_conditions, t)
        all_results.append((numeric_result, t))
        all_labels.append("$\Delta t$ = %s" % (str(dt_i)))

        yf = numeric_result[-1]
        run_conv = euler_solver.convergence_test(analytic_result[-1], yf, tol)
        print(
            run_conv
            + ": \n Numerical Solution (dt %s): %s \n Analytic Solution: %s"
            % (dt_i, yf, analytic_result[-1])
        )

    # plot the results
    plot_results = Utilities.plot_solution(
        all_results,
        "ForwardEuler-test.pdf",
        "Analytical solution vs. Forward Euler method",
        all_labels,
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
