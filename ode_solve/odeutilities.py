import matplotlib.pyplot as plt
import numpy as np


class Utilities:
    def plot_solution(solution_arrays, fig_name=None, title=None, labels=None):
        """
        Plots multiple solution arrays on the same graph. Either analytical, numerical, or both

        Parameters:
            - solution_arrays: variable number of solution arrays (each as a tuple or list of [t_values,  y_values])
            - fig_name: Name of the figure to plot
            - labels: optional list of labels for each solution

        Returns:
            - None
        """

        # check for non-empty array
        if len(solution_arrays) == 0:
            raise ValueError("At least one solution array must be provided.")

        # initialize figure
        plt.figure(figsize=(10, 6))

        # enumerate over sol. arrays
        for i, (t_values, y_values) in enumerate(solution_arrays):
            # search for and use label if exists

            label = labels[i] if labels else f"Solution {i+1}"

            # plot analytic solution as a line and numerical as scatter
            if "analytic" in label.lower():
                plt.plot(t_values, y_values, label=label, color="orange")
            else:
                plt.scatter(t_values, y_values, label=label, marker="x")

        # print(fig_name)
        plt.xlabel("Time")
        plt.ylabel("y(t)")
        plt.title(title)
        plt.legend()
        plt.grid()
        plt.savefig(fname=fig_name)
        plt.show()


class Validation:
    def validate_equation(eqn):
        try:
            result = eqn(*args, **kwargs)
            return result
        except:
            print(f"An error occured while evaluating the function{e}")
            return None

    def validate_conditions(initial_condition, t_span):

        if not isinstance(initial_condition, (int, float)):
            raise ValueError(
                "Initial condition must be provided as an integer or float."
            )

        if not isinstance(t_span, (np.ndarray)):
            raise ValueError("Time span must be an array")
        if t_span.shape[0] < 2:
            raise ValueError("Time span must contain 2 or more time-stamps.")
        if t_span[0] > t_span[1]:
            raise ValueError("The final time must be greater than the intial time.")

    def validate_params(parameters):
        if not isinstance(parameters, dict):
            raise ValueError("Parameters must be specified with a dictionary.")
