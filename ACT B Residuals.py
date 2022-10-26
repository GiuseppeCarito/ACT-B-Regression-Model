# Giuseppe Carito
# ACT B

import math

def f(x, l, k, d, c):
    # Return the function evaluated with the input x and the parameters l, k, d, c
    exponent = -k * (x - d)
    return l / (1 + math.e ** exponent) + c


def fit_calculator(data_lst, l, k, d, c):
    # Return the fit of the data to the given parameters
    total_squares_regression = 0

    for point in data_lst:
        total_squares_regression += (f(point[0], l, k, d, c) - point[1])**2

    return total_squares_regression


def make_parameter_options(lower, upper, step):
    # Return the list of each paramter
    lst = [i for i in range(int(lower//step), int(upper//step), 1)]
    return [val*step for val in lst]
    


# data set
populations = [(0, 16189), (5, 18120), (10, 30386), (15, 67595), (20, 115477), (25, 136892), (30, 190573), (35, 238866), (40, 288301), (45, 306233), (50, 323103)]


# determining the values to be checked for each parameter
l_options = make_parameter_options(350000, 355000, 100)
k_options = make_parameter_options(0, 0.15, 0.002)
d_options = make_parameter_options(28, 29, 0.05)
c_options = make_parameter_options(0, 1, 1) #has no effect on the optimal logistic function

best_fit_parameters = [] # [l,k,d,c]
best_fit = fit_calculator(populations, l_options[0], k_options[0], d_options[0], c_options[0])



# checking every combination of parameters for the best fit
for l in l_options:
    for k in k_options:
        for d in d_options:
            for c in c_options:
                
                fit = fit_calculator(populations, l, k, d, c)

                if fit < best_fit:
                    best_fit_parameters = [l, k, d, c]
                    best_fit = fit


print('Best fit: ' + str(best_fit))
print('L=' + str(best_fit_parameters[0]) + ', k=' + str(best_fit_parameters[1]) + ', d=' + str(best_fit_parameters[2]) + ', c=' + str(best_fit_parameters[3]))
