"""Package is used to solve SEIS model and get results."""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


class SEIS:

    """The Class is for SEIS model."""

    def __init__(self, n_pop, beta, gamma, tspan, alpha=0.2, lambda_rec=1 / 7):

        """The function is used to define the parameters."""

        self.pop = n_pop
        self.alpha = alpha
        self.beta = beta
        self.lambda_rec = lambda_rec
        self.gamma = gamma
        self.tspan = tspan
        self.init_con = None
        self.sol = None

    def input_detail(self):

        """The function is used to print the meaning of the inputs."""

        print(f"The total population is {self.pop} people.")
        print(f"The incubation period is {1 / self.alpha} days.")
        print(f"The recovery period is {1 / self.lambda_rec} days.")

    def initial_condition(self):

        """The function is used to generate initial conditions."""

        e_init = 0
        i_init = 1 / self.pop
        r_init = 0
        s_init = 1 - i_init - e_init - r_init

        self.init_con = np.array([s_init, e_init, i_init, r_init])

        print("The initial conditions for s, e, i, r are")
        print(f"{self.init_con} respectively.")

        return self.init_con

    def ode(self, x_input, time):

        """The function is used to set up ode systems."""

        s_input, e_input, i_input, _ = x_input

        beta = self.beta(time)
        gamma = self.gamma(time)
        dsdt = (-beta * s_input + (1 - gamma) * self.lambda_rec) * i_input
        dedt = beta * s_input * i_input - self.alpha * e_input
        didt = self.alpha * e_input - self.lambda_rec * i_input
        drdt = gamma * self.lambda_rec * i_input
        res = [dsdt, dedt, didt, drdt]

        return res

    def solution(self):

        """The function is used to solve the ode systems."""

        self.sol = odeint(self.ode, self.init_con, self.tspan)

        return self.sol

    def export(self):

        """The function is used to export data."""

        s_exp, e_exp, i_exp, r_exp = self.sol.T

        with open("./result/result.dat", "w", encoding="utf-8") as f_exp:
            for t_out, s_out, e_out, i_out, r_out in zip(
                self.tspan, s_exp, e_exp, i_exp, r_exp
            ):
                f_exp.write(str(t_out))
                f_exp.write("   ")
                f_exp.write(str(s_out))
                f_exp.write("   ")
                f_exp.write(str(e_out))
                f_exp.write("   ")
                f_exp.write(str(i_out))
                f_exp.write("   ")
                f_exp.write(str(r_out))
                f_exp.write("   ")
                f_exp.write("\n")

        print("Export Ready!")

    def plot(self, *args):

        """The function is used to generate plot of SEIS."""

        s_plot, e_plot, i_plot, r_plot = self.sol.T

        plt.figure(figsize=(8, 4), dpi=80)
        plt.title("Continuous SEIS Model")
        plt.ylabel("Fraction")
        plt.xlabel("Time/days")

        arg_set = set()

        for arg in args:

            arg_set.add(arg)

        for arg in arg_set:

            if arg == "s":

                plt.plot(self.tspan, s_plot, lw=3, label="fraction of s")

            elif arg == "e":

                plt.plot(self.tspan, e_plot, lw=3, label="fraction of e")

            elif arg == "i":

                plt.plot(self.tspan, i_plot, lw=3, label="fraction of i")

            elif arg == "r":

                plt.plot(self.tspan, r_plot, lw=3, label="fraction of r")

            else:
                print("Warning: No such argument, " + arg)

        plt.legend()
        plt.show()
