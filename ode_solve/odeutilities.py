import matplotlib.pyplot as plt


class Utilities:
    def __init__(self):
        pass

    def plot_solution(self, solution_arrays, fig_name=None, labels=None):
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

        plt.xlabel("Time")
        plt.ylabel("y(t)")
        plt.title(fig_name)
        plt.legend()
        plt.grid()
        plt.savefig("./tests/forward_euler-test.pdf")
        plt.show()
