from abc import ABC, abstractmethod


class ODESolver(ABC):
    """
    Abstract base class for numerical solutions of ordinary
    differential equations (ODEs).

    Attributes:
    - equation: ODE to be solved
    """

    def __init__(self, equation):
        """
        Initializes the ODESolver with the given ODE.

        Attributes:
        - equation: ODE to be solved
        """
        self.equation = equation

    @abstractmethod
    def solve(self, initial_condition, t_span, dt):
        """
        Solve the differential equation

        Parameters:
        - initial_condition: Initial conditions of the ODE system
        - t_span: Tuple or list (t0,tf) representing the start and end points of the integration
        - dt: Time-step of time-series from t0 to tf

        Returns:
        - solution: solution of the ODE
        """
        pass

    @abstractmethod
    def set_parameters(self, parameters):
        """
        Set parameters of the ODE system

        Parameters:
        - parameters: DIctionary containing parameters for the ODE system
        """
        pass

    @abstractmethod
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
        pass
